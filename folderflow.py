import os
import shutil

# ---------------------------
# TOP-LEVEL CATEGORIES & FILE TYPES
# ---------------------------

CATEGORIES = {
    "Images": [
        ".png", ".jpg", ".jpeg", ".gif", ".bmp", ".svg", ".webp", ".tiff", ".heic", ".raw"
    ],
    "Videos": [
        ".mp4", ".mov", ".avi", ".mkv", ".webm", ".flv", ".wmv", ".mpeg", ".mpg"
    ],
    "Audio": [
        ".mp3", ".wav", ".ogg", ".flac", ".m4a", ".aac", ".wma"
    ],
    "Apps": [
        ".exe", ".msi", ".bat", ".cmd", ".apk", ".lnk", ".url"
    ],
    "Disk Images": [
        ".iso", ".img", ".dmg", ".vhd", ".vhdx"
    ],
    "Fonts": [
        ".ttf", ".otf", ".woff", ".woff2", ".fnt", ".fon"
    ]
}

# ---------------------------
# NESTED CATEGORIES
# ---------------------------

DOCUMENT_SUBCATEGORIES = {
    "PDF": [".pdf", ".xps"],
    "Word": [".doc", ".docx", ".odt"],
    "Excel": [".xls", ".xlsx", ".ods", ".csv"],
    "Presentations": [".ppt", ".pptx", ".odp"],
    "Text": [".txt", ".rtf"]
}

ARCHIVE_SUBCATEGORIES = {
    "ZIP": [".zip"],
    "RAR": [".rar"],
    "7Z": [".7z"],
    "TAR": [".tar", ".gz", ".bz2", ".xz"]
}

CODE_SUBCATEGORIES = {
    "Python": [".py"],
    "JavaScript": [".js", ".ts", ".jsx", ".tsx"],
    "HTML_CSS": [".html", ".css"],
    "Java": [".java"],
    "C_CPP": [".c", ".cpp"],
    "CSharp": [".cs"],
    "Other": [".json", ".xml", ".sh", ".bat", ".pl", ".rb", ".go", ".rs", ".swift", ".kt"]
}

DESIGN_SUBCATEGORIES = {
    "Photoshop": [".psd"],
    "Illustrator": [".ai"],
    "XD": [".xd"],
    "Figma": [".fig"],
    "Sketch": [".sketch"],
    "InDesign": [".indd"],
    "SVG": [".svg"]
}

DEVRESOURCES_SUBCATEGORIES = {
    "Env": [".env"],
    "YAML": [".yml", ".yaml"],
    "Config": [".ini", ".cfg"],
    "Docker": [".dockerfile", "docker-compose"],
    "Git": [".gitignore"]
}

IGNORE_FOLDERS = {
    "__pycache__", "node_modules", "venv", ".git", ".idea", ".vscode",
    "Documents", "Archives", "Code", "Design", "DevResources", "Others"
}

# ---------------------------
# ORGANIZE FUNCTION
# ---------------------------

def move_files(file_path, base_folder, subcategories):
    _, ext = os.path.splitext(file_path)
    ext = ext.lower()
    file_name = os.path.basename(file_path)

    for folder, extensions in subcategories.items():
        if ext in extensions:
            target_folder = os.path.join(base_folder, folder)
            os.makedirs(target_folder, exist_ok=True)
            shutil.move(file_path, target_folder)
            print(f"Moved {file_name} → {base_folder}/{folder}/")
            return True
    return False

def organize(path="."):
    for item in os.listdir(path):
        item_path = os.path.join(path, item)

        # Skip directories we shouldn't touch
        if os.path.isdir(item_path):
            if item in IGNORE_FOLDERS or item in CATEGORIES.keys():
                continue
            continue  # do not move directories, only files

        # -------------------
        # Nested categories first
        # -------------------
        moved = False
        for base_folder, subcategories in [
            ("Documents", DOCUMENT_SUBCATEGORIES),
            ("Archives", ARCHIVE_SUBCATEGORIES),
            ("Code", CODE_SUBCATEGORIES),
            ("Design", DESIGN_SUBCATEGORIES),
            ("DevResources", DEVRESOURCES_SUBCATEGORIES)
        ]:
            moved = move_files(item_path, base_folder, subcategories)
            if moved:
                break
        if moved:
            continue

        # -------------------
        # Top-level categories
        # -------------------
        for folder, extensions in CATEGORIES.items():
            _, ext = os.path.splitext(item)
            ext = ext.lower()
            if ext in extensions:
                target_folder = os.path.join(path, folder)
                os.makedirs(target_folder, exist_ok=True)
                shutil.move(item_path, target_folder)
                print(f"Moved {item} → {folder}/")
                moved = True
                break

        # -------------------
        # Anything else → Others
        # -------------------
        if not moved:
            other_folder = os.path.join(path, "Others")
            os.makedirs(other_folder, exist_ok=True)
            shutil.move(item_path, other_folder)
            print(f"Moved {item} → Others/")

# ---------------------------
# ENTRY POINT
# ---------------------------

if __name__ == "__main__":
    print("Running FolderFlow...")
    organize()
    print("✔ Done! Folder organized successfully.")
