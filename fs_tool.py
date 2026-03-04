# Search by extension, open/delete

import os
import sys
import subprocess
import tkinter as tk
from tkinter import ttk, filedialog, messagebox


class FileSearchTool:
    def __init__(self, root):
        self.root = root
        self.root.title("File Search Tool")
        icon_path = os.path.join(os.path.dirname(__file__), "Folder.png")
        icon_image = tk.PhotoImage(file=icon_path)
        self.root.geometry("550x440")
        self.root.resizable(False, False)
        self.root.iconphoto(False, icon_image)

        self._build_ui()

    # Assemble the interface
    def _build_ui(self):
        # Top row - extension selector, search button
        tk.Label(self.root, text="File Extension:").grid(
            row=0, column=0, padx=10, pady=1, sticky="w")
        self.extension_menu = ttk.Combobox(
            self.root, values=[".jpg", ".jpeg", ".txt", ".py", ".pdf", ".docx"], width=10
            )
        self.extension_menu.set(".txt")
        self.extension_menu.grid(row=0, column=1, padx=5, pady=10)

        tk.Button(self.root, text="Search", command=self.search_files).grid(
            row=0, column=2, padx=10, pady=10
        )

        # "Body" - Scrollbars, Listbox
        self.scrollbar_y = tk.Scrollbar(self.root)
        self.scrollbar_y.grid(row=1, column=3, sticky="ns", pady=10)

        self.scrollbar_x = tk.Scrollbar(self.root, orient=tk.HORIZONTAL)
        self.scrollbar_x.grid(row=2, column=0, columnspan=3, sticky="ew", padx=(10, 0))

        self.results_list = tk.Listbox(
            self.root,
            width=80,
            height=15,
            yscrollcommand=self.scrollbar_y.set,
            xscrollcommand=self.scrollbar_x.set,
        )
        self.results_list.grid(row=1, column=0, columnspan=3, padx=(10, 0), pady=10)
        self.results_list.bind("<Double-1>", self.open_selected_item)

        self.scrollbar_y.config(command=self.results_list.yview)
        self.scrollbar_x.config(command=self.results_list.xview)

        # Delete button
        tk.Button(
            self.root,
            text="Delete Selected",
            fg="white",
            bg="#c0392b",
            command=self.delete_selected,
        ).grid(row=3, column=0, padx=10, pady=(5, 10), sticky="w")

        # Search tool active status
        self.status_var = tk.StringVar(value="Ready.")
        tk.Label(self.root, textvariable=self.status_var, anchor="w", fg="gray").grid(
            row=4, column=0, columnspan=4, padx=10, sticky="ew"
        )

    # -----------------------------------------------------------------------------------

    def search_files(self):
        folder = filedialog.askdirectory()
        if not folder:
            return
        ext = self.extension_menu.get().strip()
        if not ext.startswith("."):
            ext = "." + ext
        
        self.results_list.delete(0, tk.END)

        matches = [
            os.path.join(root, file)
            for root, _, files in os.walk(folder)
            for file in files
            if file.endswith(ext)
        ]

        if matches:
            for path in matches:
                self.results_list.insert(tk.END, path)
            self.status_var.set(f"{len(matches)} file(s) found.")
        else:
            self.results_list.insert(tk.END, f" No '{ext}' files found in {folder}")
            self.status_var.set("No results.")
    
    def open_selected_item(self, event):
        """Opens the double-clicked file with the system default application"""
        selection = self.results_list.curselection()
        if not selection:
            return
        
        filepath = self.results_list.get(selection[0])

        # Protect from "no results" being double-clicked
        if not os.path.isfile(filepath):
            return
        
        # Detect OS
        if sys.platform == "win32":
            os.startfile(filepath)
        elif sys.platform == "darwin":
            subprocess.run(["open", filepath])
        else:
            subprocess.run(["xdg-open", filepath])

    
    def delete_selected(self):
        """Prompts for confirmation then permanently deletes the selected file"""
        selection = self.results_list.curselection()
        if not selection:
            messagebox.showinfo("No selection", "Please select a file to delete.")
            return
        
        filepath = self.results_list.get(selection[0])

        if not os.path.isfile(filepath):
            return
        
        # Double-check deletion
        confirmed = messagebox.askyesno(
            "Confirm Delete",
            f"Permanently delete this file?\n\n{filepath}",
        )
        if confirmed:
            try:
                os.remove(filepath)
                self.results_list.delete(selection[0])
                self.status_var.set(f"Deleted: {os.path.basename(filepath)}")
            except OSError as e:
                messagebox.showerror("Error", f"Could not delete file:\n{e}")

# ---------------------------------------------------------------------------------------


if __name__ == "__main__":
    root = tk.Tk()
    app = FileSearchTool(root)
    root.mainloop()