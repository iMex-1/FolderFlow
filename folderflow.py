import os
import shutil

CATEGORIES = {
    "Images": [
        ".png", ".jpg", ".jpeg", ".gif", ".bmp", ".svg", ".webp", ".tiff"
    ],
    "Videos": [
        ".mp4", ".mov", ".avi", ".mkv", ".webm", ".flv"
    ],
    "Documents": [
        ".pdf", ".docx", ".doc", ".txt", ".pptx", ".ppt", ".xlsx", ".csv", ".rtf"
    ],
    "Audio": [
        ".mp3", ".wav", ".ogg", ".flac", ".m4a"
    ],
    "Archives": [
        ".zip", ".rar", ".7z", ".tar", ".gz"
    ],
    "Code": [
        ".py", ".js", ".ts", ".jsx", ".tsx", ".html", ".css",
        ".php", ".java", ".cpp", ".c", ".cs", ".json", ".xml", ".sh"
    ],
    "Design": [
        ".psd", ".ai", ".xd", ".fig", ".sketch"
    ],
    "Apps": [
        ".exe", ".msi", ".bat", ".cmd"
    ],
    "Disk Images": [
        ".iso", ".img"
    ],
    "Fonts": [
        ".ttf", ".otf", ".woff", ".woff2"
    ],
    "DevResources": [
        ".env", ".yml", ".yaml", ".ini", ".cfg"
    ]
}

IGNORE_FOLDERS = {
    "__pycache__", 
    "node_modules", 
    "venv", 
    ".git", 
    ".idea", 
    ".vscode"
}

def organize(path="."):
    for item in os.listdir(path):
        item_path = os.path.join(path, item)

        # Skip directories we shouldn't touch
        if os.path.isdir(item_path):
            if item in IGNORE_FOLDERS:
                continue
            # Also skip folders created by this script
            if item in CATEGORIES.keys() or item == "Others":
                continue
            continue  # do not move directories, only files

        # Get extension
        _, ext = os.path.splitext(item)
        ext = ext.lower()

        moved = False

        # Determine correct category
        for folder, extensions in CATEGORIES.items():
            if ext in extensions:
                folder_path = os.path.join(path, folder)
                os.makedirs(folder_path, exist_ok=True)
                shutil.move(item_path, folder_path)
                print(f"Moved {item}  →  {folder}/")
                moved = True
                break

        # If extension not found, move to Others
        if not moved:
            other_folder = os.path.join(path, "Others")
            os.makedirs(other_folder, exist_ok=True)
            shutil.move(item_path, other_folder)
            print(f"Moved {item}  →  Others/")

if __name__ == "__main__":
    print("Running FolderFlow...")
    organize()
    print("✔ Done! Folder organized successfully.")
