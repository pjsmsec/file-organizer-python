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

