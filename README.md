# File Organizer by Extension

This Python script organizes files inside a specified directory by sorting them into folders based on their file extensions.

## Features
- Automatically detects all file extensions in a directory
- Creates a separate folder for each extension
- Moves files into their corresponding folders
- Uses only Python built-in modules

## How It Works
The script:
1. Scans the target directory
2. Groups files by their extension
3. Creates a folder for each extension (e.g., `PNG files`, `TXT files`)
4. Moves the files into their respective folders

## Usage
Set the directory you want to organize:

```python
desktop_path = os.path.expanduser("~/Desktop/Path")
Run the script:

python organize.py
Example Structure

Before:
photo.png
notes.txt
document.pdf
image.png

After:
PNG files/photo.png
PNG files/image.png
TXT files/notes.txt
PDF files/document.pdf

Requirements
Python 3.x
