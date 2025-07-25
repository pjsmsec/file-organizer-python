# File Organizer

A Python script to automatically organize files in a specified directory by their file type. This helps keep your directories tidy and easy to navigate.

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
   git clone https://github.com/pjsmsec/file-organizer-python
   cd file-organizer-python
   ```

2. Run the script with the target directory as an argument (optional, defaults to current directory):

   ```bash
   python3 file_organizer.py /path/to/directory
   ```

   Or, if the script has execution permission, you can run it directly:

   ```bash
   ./file_organizer.py /path/to/directory
   ```

   > **Note:** To run the script directly by its name (e.g. `./file_organizer.py`), ensure it has execution permission:
   >
   > ```bash
   > chmod +x file_organizer.py
   > ```
   >
   > Also, make sure the first line of the script contains the shebang:
   >
   > ```python
   > #!/usr/bin/env python3
   > ```

3. The files will be organized into folders based on their extensions.

### Example

**Before:**

```bash
/downloads
├── file1.pdf
├── photo.jpg
└── notes.txt
```

**After:**

```bash
/downloads
├── pdf
│   └── file1.pdf
├── jpg
│   └── photo.jpg
└── txt
    └── notes.txt
```

## Contributing

Contributions are welcome! Feel free to open issues or submit pull requests.
