import os
import shutil

# ---------------------------
# CATEGORIES & FILE TYPES
# ---------------------------

CATEGORIES = {
    "Images": [
        ".png", ".jpg", ".jpeg", ".gif", ".bmp", ".svg", ".webp", ".tiff", ".heic", ".raw"
    ],
    "Videos": [
        ".mp4", ".mov", ".avi", ".mkv", ".webm", ".flv", ".wmv", ".mpeg", ".mpg"
    ],
    "Documents": [
        ".pdf", ".docx", ".doc", ".txt", ".pptx", ".ppt", ".xlsx", ".xls", ".csv", ".rtf", ".odt", ".ods", ".odp"
    ],
    "Audio": [
        ".mp3", ".wav", ".ogg", ".flac", ".m4a", ".aac", ".wma"
    ],
    "Archives": [
        ".zip", ".rar", ".7z", ".tar", ".gz", ".bz2", ".xz"
    ],
    "Code": [
        ".py", ".js", ".ts", ".jsx", ".tsx", ".html", ".css",
        ".php", ".java", ".cpp", ".c", ".cs", ".json", ".xml", ".sh", ".bat", ".pl", ".rb", ".go", ".rs", ".swift", ".kt"
    ],
    "Design": [
        ".psd", ".ai", ".xd", ".fig", ".sketch", ".indd", ".svg"
    ],
    "Apps": [
        ".exe", ".msi", ".bat", ".cmd", ".apk", ".lnk", ".url"
    ],
    "Disk Images": [
        ".iso", ".img", ".dmg", ".vhd", ".vhdx"
    ],
    "Fonts": [
        ".ttf", ".otf", ".woff", ".woff2", ".fnt", ".fon"
    ],
    "DevResources": [
        ".env", ".yml", ".yaml", ".ini", ".cfg", ".dockerfile", ".gitignore", ".docker-compose"
    ],
    "PDFs": [
        ".pdf", ".xps"
    ],
    "Spreadsheets": [
        ".xls", ".xlsx", ".ods", ".csv"
    ],
    "Presentations": [
        ".ppt", ".pptx", ".odp"
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

# ---------------------------
# ORGANIZE FUNCTION
# ---------------------------

def organize(path="."):
    for item in os.listdir(path):
        item_path = os.path.join(path, item)

        # Skip directories we shouldn't touch
        if os.path.isdir(item_path):
            if item in IGNORE_FOLDERS:
                continue
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

# ---------------------------
# ENTRY POINT
# ---------------------------

if __name__ == "__main__":
    print("Running FolderFlow...")
    organize()
    print("✔ Done! Folder organized successfully.")
