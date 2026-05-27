import os 
import shutil 

folder = os.path.join(os.path.expanduser("~"), "Downloads")

file_types = {
    ".pdf": "pdf",
    ".jpg": "images",
    ".jpeg": "images",
    ".png": "images",
    ".md": "markdownFiles",
    ".doc": "wordFiles",
    ".docx": "wordFiles",
    ".xlsx": "excelFiles",
    ".jfif": "images",
    ".zip": "zipFolders",
    ".txt": "textDocuments",
    ".key": "keyFiles",
    ".sql" : "sqlFiles"
}

for file in os.listdir(folder):
    filepath = os.path.join(folder, file)

    if not os.path.isfile(filepath):
        continue
    
    ext = os.path.splitext(file)[1].lower()

    target = file_types.get(ext)
    if not target: 
        continue
    
    if ext in file_types:
        target_folder = os.path.join(folder, file_types[ext])
        os.makedirs(target_folder, exist_ok=True)

    try:
        print(f"Moving {file} to {file_types[ext]}/")
        shutil.move(filepath, os.path.join(target_folder, file))

    except PermissionError:
        print(f"Skipping {file} (file is in use)") 