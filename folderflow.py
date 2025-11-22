import os
import shutil
import json
from datetime import datetime

# ===========================
# CONFIGURATION
# ===========================

CATEGORIES = {
    "Images": [".png", ".jpg", ".jpeg", ".gif", ".bmp", ".svg", ".webp", ".tiff"],
    "Videos": [".mp4", ".mov", ".avi", ".mkv", ".webm", ".flv"],
    "Documents": [".pdf", ".docx", ".doc", ".txt", ".pptx", ".ppt", ".xlsx", ".csv", ".rtf"],
    "Audio": [".mp3", ".wav", ".ogg", ".flac", ".m4a"],
    "Archives": [".zip", ".rar", ".7z", ".tar", ".gz"],
    "Code": [".py", ".js", ".ts", ".jsx", ".tsx", ".html", ".css",
             ".php", ".java", ".cpp", ".c", ".cs", ".json", ".xml", ".sh"],
    "Design": [".psd", ".ai", ".xd", ".fig", ".sketch"],
    "Apps": [".exe", ".msi", ".bat", ".cmd"],
    "Disk Images": [".iso", ".img"],
    "Fonts": [".ttf", ".otf", ".woff", ".woff2"],
    "DevResources": [".env", ".yml", ".yaml", ".ini", ".cfg"]
}

IGNORE_FOLDERS = {"__pycache__", "node_modules", "venv", ".git", ".idea", ".vscode"}

UNDO_FILE = "folderflow_undo.json"
LOG_FILE = "folderflow.log"

MAX_FILE_SIZE_MB = 300  # Skip files bigger than this
MAX_FOLDER_SIZE_MB = 1500  # Skip entire folders bigger than this


# ===========================
# HELPERS
# ===========================

def log(message):
    with open(LOG_FILE, "a") as logf:
        logf.write(f"{datetime.now()} - {message}\n")
    print(message)


def folder_size(path):
    total = 0
    for root, _, files in os.walk(path):
        for f in files:
            fp = os.path.join(root, f)
            try:
                total += os.path.getsize(fp)
            except:
                pass
    return total / (1024 * 1024)  # convert to MB


def scan_files_recursively(base_path):
    files_list = []

    for root, dirs, files in os.walk(base_path):
        # Skip ignored dirs
        dirs[:] = [d for d in dirs if d not in IGNORE_FOLDERS]

        # Exclude large directories
        for d in list(dirs):
            folder_path = os.path.join(root, d)
            size_mb = folder_size(folder_path)
            if size_mb > MAX_FOLDER_SIZE_MB:
                log(f"Skipping large folder: {d} ({size_mb:.1f} MB)")
                dirs.remove(d)

        # Add files
        for f in files:
            full_path = os.path.join(root, f)
            files_list.append(full_path)

    return files_list


def show_progress(current, total):
    percent = int((current / total) * 100)
    bar = "=" * (percent // 2) + " " * (50 - percent // 2)
    print(f"\r[{bar}] {percent}% ({current}/{total})", end="")


# ===========================
# MAIN ORGANIZER
# ===========================

def organize(base_path="."):
    moved_files = {}

    all_files = scan_files_recursively(base_path)
    total = len(all_files)
    current = 0

    for file_path in all_files:
        current += 1
        show_progress(current, total)

        if os.path.isdir(file_path):
            continue

        size_mb = os.path.getsize(file_path) / (1024 * 1024)
        if size_mb > MAX_FILE_SIZE_MB:
            log(f"Skipping large file: {os.path.basename(file_path)} ({size_mb:.1f} MB)")
            continue

        ext = os.path.splitext(file_path)[1].lower()
        file_name = os.path.basename(file_path)
        file_dir = os.path.dirname(file_path)

        moved = False

        for folder, extensions in CATEGORIES.items():
            if ext in extensions:
                target = os.path.join(base_path, folder)
                os.makedirs(target, exist_ok=True)

                dest = os.path.join(target, file_name)
                shutil.move(file_path, dest)

                moved_files[dest] = file_path  # store undo info
                log(f"Moved {file_name} → {folder}/")
                moved = True
                break

        if not moved:
            target = os.path.join(base_path, "Others")
            os.makedirs(target, exist_ok=True)

            dest = os.path.join(target, file_name)
            shutil.move(file_path, dest)
            moved_files[dest] = file_path
            log(f"Moved {file_name} → Others/")

    print("\n✔ Organizing complete.")
    with open(UNDO_FILE, "w") as f:
        json.dump(moved_files, f, indent=4)
    log("Undo file saved.")


# ===========================
# UNDO SYSTEM
# ===========================

def undo():
    if not os.path.exists(UNDO_FILE):
        print("❌ No undo file found!")
        return

    with open(UNDO_FILE, "r") as f:
        moves = json.load(f)

    total = len(moves)
    current = 0

    for new_path, old_path in moves.items():
        current += 1
        show_progress(current, total)

        if os.path.exists(new_path):
            os.makedirs(os.path.dirname(old_path), exist_ok=True)
            shutil.move(new_path, old_path)
            log(f"Restored {os.path.basename(new_path)}")

    print("\n✔ Undo complete.")
    os.remove(UNDO_FILE)


# ===========================
# ENTRY POINT
# ===========================

if __name__ == "__main__":
    import sys
    log("\n=== FolderFlow Run Started ===")

    if len(sys.argv) < 2:
        print("Usage:")
        print("  python folderflow.py run   → organize files")
        print("  python folderflow.py undo  → undo last run")
        exit()

    if sys.argv[1] == "run":
        organize()
    elif sys.argv[1] == "undo":
        undo()
    else:
        print("Unknown command.")
