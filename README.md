# File Organizer

A Python script to automatically organize files in a specified directory by their file type and modification date. This helps keep your directories tidy and easy to navigate.

## Features

- Organizes files by their extensions (e.g., `.txt`, `.jpg`, `.pdf`).
- Creates folders for each file type if they don't already exist.
- Moves files into their respective folders.
- Easy to customize and extend.

## Requirements

- Python 3.x

## Usage

1. Clone this repository:

   ```bash
   git clone https://github.com/yourusername/file-organizer.git
   cd file-organizer

2. Run the script with the target directory as an argument (optional, defaults to current directory):

   python file_organizer.py /path/to/directory

3. The files will be organized into folders based on their extensions.

  Example

Before:

/downloads
  file1.pdf
  photo.jpg
  notes.txt

After:

/downloads
  /pdf
    file1.pdf
  /jpg
    photo.jpg
  /txt
    notes.txt
    
Contributing

Contributions are welcome! Feel free to open issues or submit pull requests.
