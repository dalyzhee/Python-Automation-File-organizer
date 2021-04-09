import os
import sys
from shutil import move
from pathlib import Path
from sys import argv


def get_dir(filename):
    ext = filename.suffix[1:]
    return dirs.get(ext, "Miscellaneous")


dirs = {
    # Images
    "jpeg": "Images",
    "jpg": "Images",
    "png": "Images",
    "gif": "Images",
    "tiff": "Images",

    # Videos
    "mp4": "Videos",
    "mkv": "Videos",
    "avi": "Videos",
    "webm": "Videos",
    "mov": "Videos",
    "flv": "Videos",

    # Music
    "mp3": "Music",
    "ogg": "Music",
    "wav": "Music",
    "flac": "Music",

    # Program files
    "py": "Program Files",
    "js": "Program Files",
    "cpp": "Program Files",
    "html": "Program Files",
    "css": "Program Files",
    "c": "Program Files",
    "sh": "Program Files",

    # Documents
    "pdf": "Documents",
    "doc": "Documents",
    "docx": "Documents",
    "txt": "Documents",
    "ods": "Documents",
    "ppt": "Documents",
    "csv": "Documents",
}

if len(argv) != 2:
    print("=" * 35)
    print("[ERROR] Invalid number of arguments were given")
    print(f"[Usage] python {Path(__file__).name} <dir_path>")
    print("=" * 35)
    exit(1)

PATH = Path(argv[1])

for filename in PATH.iterdir():

    path_to_file = filename.absolute()

    if path_to_file.is_file():
        destination = PATH / get_dir(filename)

        if not destination.exists():
            destination.mkdir()

        move(str(path_to_file), str(destination))
