#!/usr/bin/env python3

"""
file_organizer.py

A script to organize files in a given directory based on their file extensions.

Features:
- Automatically detects and categorizes files by type (e.g., .txt, .jpg).
- Creates directories for each file type if not already present.
- Moves files into the corresponding directories.
- Logs all operations with timestamps and status.
- Supports optional command-line argument to specify a target directory.
"""

import sys
from pathlib import Path
import logging
from datetime import datetime

"""
Setup logging configuration to write logs to a timestamped file inside a 'logs' directory.

Args:
    target_dir (Path): Directory where the 'logs' folder will be created.
"""
def setup_logging(target_dir: Path):
    log_dir = target_dir / "logs"
    log_dir.mkdir(exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    log_file = log_dir / f"file_organizer_{timestamp}.log"

    logging.basicConfig(
        filename=str(log_file),
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )

    print(f"Logging to {log_file}")
    logging.info(f"Logging started. Log file: {log_file}")

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
        ext = file.suffix[1:].lower() if file.suffix else 'no_extension'
        folder_path = target_dir / ext

        if file.parent == folder_path:
            logging.info(f"Skipping '{file.name}' as it is already in the correct folder.")
            continue

        folder_path.mkdir(exist_ok=True)

        destination = folder_path / file.name

        if destination.exists():
            print(f"Conflict: '{destination}' already exists. Skipping '{file.name}'.")
            logging.warning(f"Conflict: '{destination}' already exists. Skipped '{file.name}'.")
            continue

        file.rename(destination)
        print(f"Moved '{file.name}' to '{folder_path}'.")
        logging.info(f"Moved '{file.name}' to '{folder_path}'.")

"""
Entry point for the script.

    - Parses the target directory from command-line arguments (optional).
    - Defaults to the current working directory if none is provided.
    - Sets up logging.
    - Lists all files and organizes them by extension.
"""
def main():
    if len(sys.argv) > 1:
        target_dir = Path(sys.argv[1])
    else:
        target_dir = Path.cwd()

    if not target_dir.exists() or not target_dir.is_dir():
        print(f"Error: The directory '{target_dir}' does not exist or is not a directory.")
        sys.exit(1)

    setup_logging(target_dir)

    print(f"Organizing files in directory: {target_dir}")
    logging.info(f"Starting organization in directory: {target_dir}")

    files = list_files(target_dir)
    print(f"Found {len(files)} file(s).")
    logging.info(f"Found {len(files)} file(s) in directory.")

    if not files:
        print("No files to organize.")
        logging.info("No files found to organize. Exiting.")
        return

    organize_files(files, target_dir)
    print("Files have been organized by extension.")
    logging.info("File organization completed successfully.")

if __name__ == "__main__":
    main()
