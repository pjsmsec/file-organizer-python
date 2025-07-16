#!/usr/bin/env python3

"""
file_organizer.py

A script to organize files in a given directory based on their file extensions.

Features:
- Automatically detects and categorizes files by type (e.g., .txt, .jpg).
- Creates directories for each file type if not already present.
- Moves files into the corresponding directories.
- Supports optional command-line argument to specify a target directory.
"""

import sys
from pathlib import Path

"""
List all files in the given directory (excluding subdirectories).

Args:
    directory (Path): Target directory to scan.

Returns:
    list[Path]: List of Path objects representing each file found.
"""
def list_files(directory: Path) -> list[Path]:
    return [f for f in directory.iterdir() if f.is_file()]

"""
Organize files into folders based on their file extensions.

For each file in the list:
    - Determine the file extension (without the dot).
    - Create a folder named after the extension if it does not exist.
    - Move the file into the corresponding folder.

Args:
    files (list[Path]): List of Path objects representing files to organize.
    target_dir (Path): The base directory where folders will be created.
"""
def organize_files(files: list[Path], target_dir: Path) -> None:
    for file in files:
        # Get file extension without the leading dot, or 'no_extension' if none
        ext = file.suffix[1:].lower() if file.suffix else 'no_extension'
        folder_path = target_dir / ext

        # Skip if file is already in the correct folder
        if file.parent == folder_path:
            continue

        folder_path.mkdir(exist_ok=True)

        # Define destination and move the file
        destination = folder_path / file.name

        # Handle naming conflict if destination file already exists
        if destination.exists():
            print(f"Conflict: '{destination}' already exists. Skipping '{file.name}'.")
            continue

        file.rename(destination)

"""
Entry point for the script.

    - Parses the target directory from command-line arguments (optional).
    - Defaults to the current working directory if none is provided.
    - Lists all files and organizes them by extension.
"""
def main():
    # Get directory from command line or use current directory
    if len(sys.argv) > 1:
        target_dir = Path(sys.argv[1])
    else:
        target_dir = Path.cwd()

    # Validate the provided path
    if not target_dir.exists() or not target_dir.is_dir():
        print(f"Error: The directory '{target_dir}' does not exist or is not a directory.")
        sys.exit(1)

    print(f"Organizing files in directory: {target_dir}")

    files = list_files(target_dir)
    print(f"Found {len(files)} file(s).")

    if not files:
        print("No files to organize.")
        return

    organize_files(files, target_dir)
    print("Files have been organized by extension.")

if __name__ == "__main__":
    main()
