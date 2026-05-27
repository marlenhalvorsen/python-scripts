import os 
import shutil

folder = r"C:\Users\marle\Downloads" 

for file in os.listdir(folder):
    filepath = os.path.join(folder, file)

    if not os.path.isfile(filepath):
        continue

    if file.lower().endswith(".pdf"):
        print(f"Flytter {file} til pdf/")
        os.makedirs(os.path.join(folder, "pdf"), exist_ok=True)
        shutil.move(filepath, os.path.join(folder, "pdf", file))

    elif file.lower().endswith(".jpg"):
        print(f"Flytter {file} til images/")
        os.makedirs(os.path.join(folder, "images"), exist_ok=True)
        shutil.move(filepath, os.path.join(folder, "images", file))

    elif file.lower().endswith(".md"):
        print(f"Flytter {file} til markdownFile/")
        os.makedirs(os.path.join(folder, "markdownFiles"), exist_ok=True)
        shutil.move(filepath, os.path.join(folder, "markdownFiles", file))

    elif file.lower().endswith((".doc", ".docx")):
        
        try:    
            print(f"Flytter {file} til wordFiles/")
            os.makedirs(os.path.join(folder, "wordFiles"), exist_ok=True)
            shutil.move(filepath, os.path.join(folder, "wordFiles", file))
        
        except PermissionError:
            print(f"Skipping {file} (file is in use)")