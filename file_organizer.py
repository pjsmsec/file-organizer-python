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

import os
import sys
import shutil
from pathlib import Path

"""
List all files in the given directory (not including subdirectories).

Args:
    directory (Path): Target directory to scan.

Returns:
    list: List of Path objects for each file found.
"""
def list_files(directory: Path) -> list:
    return [f for f in directory.iterdir() if f.is_file()]

def main():
    """
     Main function to get the target directory from command line arguments.

    - If a directory path is provided as the first argument, use it.
    - Otherwise, default to the current working directory.
    - Validates if the provided path exists and is a directory.
    """
    # Check if user passed a directory path argument
    if len(sys.argv) > 1:
        target_dir = Path(sys.argv[1])
    else:
        # Default to current directory
        target_dir = Path.cwd()
    
    # Validate the target directory
    if not target_dir.exists() or not target_dir.is_dir():
        print(f"Error: The directory '{target_dir}' does not exist or is not a directory.")
        sys.exit(1)

    print(f"Organizing files in directory: {target_dir}")

    files = list_files(target_dir)
    print(f"Found {len(files)} files:")
    for f in files:
        print(f" - {f.name}")

if __name__ == "__main__":
    main()
