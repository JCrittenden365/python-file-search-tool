# File Search & Delete Tool

A lightweight desktop utility built with Python and Tkinter that allows users to search for files by extension within a selected directory,
open them with the system’s default application, or permanently delete selected files.

This project was created as a hands-on learning exercise to strengthen GUI development, file system operations, and structured programming practices.


## Features

* Search for files by extension within a chosen directory

* Recursive directory scanning using os.walk()

* Scrollable results list for large result sets

* Double-click to open files with the system’s default application

* Cross-platform file opening (Windows, macOS, Linux)

* Permanent file deletion with confirmation prompt

* Status bar feedback for user actions


# Technologies Used

Python 3

Tkinter (GUI framework)

os / sys / subprocess modules

File system operations

Basic error handling and input validation


# How It Works

Select a file extension from the dropdown menu

Choose a directory to scan

View matching files in the results list

Double-click a file to open it

Select a file and click Delete Selected to permanently remove it (confirmation required)


## Important Note

File deletion is permanent and does not move files to the recycle bin.
Users are prompted for confirmation before deletion to prevent accidental removal.


# Purpose of This Project

This tool was built to strengthen practical Python skills, including:

GUI design and layout management

File system traversal

Safe user interaction design

Cross-platform compatibility handling

Structured class-based programming


# Future Improvements

* Add multi-select delete support

* Add file size and date filtering

* Add logging functionality

* Package with an installer

# Author
Josh Crittenden
Aspiring IT professional focused on Linux, automation, and hands-on technical development
