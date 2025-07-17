import pytest
from pathlib import Path
import tempfile
from file_organizer import list_files, organize_files

@pytest.fixture
def temp_dir():
    with tempfile.TemporaryDirectory() as tmpdirname:
        yield Path(tmpdirname)

def test_list_files(temp_dir):
    # Create temporary folder and files
    (temp_dir / "file1.txt").touch()
    (temp_dir / "file2.jpg").touch()
    (temp_dir / "subdir").mkdir()
    files = list_files(temp_dir)
    assert len(files) == 2
    assert all(f.is_file() for f in files)

def test_organize_files_creates_folders_and_move_files(temp_dir):
    # Create files
    txt_file = temp_dir / "doc.txt"
    jpg_file = temp_dir / "image.jpg"
    txt_file.touch()
    jpg_file.touch()

    files = list_files(temp_dir)
    organize_files(files, temp_dir)

    # Check folder creation
    assert (temp_dir / "txt").is_dir()
    assert (temp_dir / "jpg").is_dir()

    # Check if the files were moved correctly
    assert (temp_dir / "txt" / "doc.txt").exists()
    assert (temp_dir / "jpg" / "image.jpg").exists()
    # The files should no longer be in the root folder
    assert not txt_file.exists()
    assert not jpg_file.exists()

def test_organize_files_handle_conflicts(temp_dir):
    # Create the original file and same named file inside destiny folder
    file1 = temp_dir / "conflict.txt"
    file1.touch()
    (temp_dir / "txt").mkdir()
    conflict_file = temp_dir / "txt" / "conflict.txt"
    conflict_file.touch()

    files = list_files(temp_dir)
    organize_files(files, temp_dir)

    # The orginal file should remain in root
    assert file1.exists()
    # The file inside the destiny folder should remain there
    assert conflict_file.exists()
