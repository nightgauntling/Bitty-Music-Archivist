import os
import tkinter as tk
from tkinter import filedialog


def rename_underscores(folder_path, dry_run=True):
    operations = []

    for filename in os.listdir(folder_path):
        old_path = os.path.join(folder_path, filename)

        if not os.path.isfile(old_path):
            continue

        if "_" not in filename:
            continue

        name, ext = os.path.splitext(filename)
        new_filename = name.replace("_", " ") + ext
        new_path = os.path.join(folder_path, new_filename)

        if os.path.exists(new_path):
            print(f"Skipping (exists): '{new_filename}'")
            continue

        operations.append((old_path, new_path))

        if dry_run:
            print(f"[DRY RUN] '{filename}' → '{new_filename}'")
        else:
            os.rename(old_path, new_path)
            print(f"Renamed: '{filename}' → '{new_filename}'")

    return operations


def select_folder():
    root = tk.Tk()
    root.withdraw()
    return filedialog.askdirectory(title="Select Music Folder")


if __name__ == "__main__":
    folder = select_folder()

    if not folder:
        print("No folder selected.")
    elif not os.path.isdir(folder):
        print(f"Invalid folder: {folder}")
    else:
        rename_underscores(folder, dry_run=True)
