import os
import shutil

# File type categories
FILE_TYPES = {
    "Images": [".png", ".jpg", ".jpeg", ".gif", ".bmp", ".svg", ".webp"],
    "Videos": [".mp4", ".mov", ".avi", ".mkv", ".webm"],
    "Documents": [".pdf", ".docx", ".doc", ".txt", ".pptx", ".xlsx", ".csv"],
    "Audio": [".mp3", ".wav", ".ogg", ".m4a"],
    "Archives": [".zip", ".rar", ".7z", ".tar", ".gz"],
    "Code": [".py", ".js", ".ts", ".html", ".css", ".php", ".java", ".cpp", ".json"],
    "Design": [".psd", ".ai", ".xd", ".fig"],
}

def organize_folder(path="."):
    for item in os.listdir(path):
        item_path = os.path.join(path, item)

        # Skip directories created by this script
        if os.path.isdir(item_path):
            continue

        # Get file extension
        _, ext = os.path.splitext(item)
        ext = ext.lower()

        moved = False

        # Check in which category this extension belongs
        for folder, extensions in FILE_TYPES.items():
            if ext in extensions:
                folder_path = os.path.join(path, folder)
                os.makedirs(folder_path, exist_ok=True)
                shutil.move(item_path, folder_path)
                print(f"Moved {item} → {folder}/")
                moved = True
                break

        # If no category matches, put it in "Others"
        if not moved:
            other_folder = os.path.join(path, "Others")
            os.makedirs(other_folder, exist_ok=True)
            shutil.move(item_path, other_folder)
            print(f"Moved {item} → Others/")

if __name__ == "__main__":
    organize_folder()
    print("\n✔ All files organized successfully!")
