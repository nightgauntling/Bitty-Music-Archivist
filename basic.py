import os

folder_path = r"H:\02 Archive Audio\Music\Files Ready to Commit\EPIC_(FULL_Official_Concept_Album)-320-mp3-(1_40)"

for filename in os.listdir(folder_path):
    old_path = os.path.join(folder_path, filename)

    # Skip folders
    if not os.path.isfile(old_path):
        continue

    # Skip files without underscores
    if "_" not in filename:
        continue

    # Replace underscores with spaces
    new_filename = filename.replace("_", " ")
    new_path = os.path.join(folder_path, new_filename)

    # Skip if target already exists
    if os.path.exists(new_path):
        print(f"Skipping, file name in use: '{new_filename}'")
        continue

    # Rename the file
    os.rename(old_path, new_path)

    print(f"Renamed: '{filename}' → '{new_filename}'")