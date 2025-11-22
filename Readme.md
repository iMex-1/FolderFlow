# FolderFlow

FolderFlow is a **lightweight and powerful file organizer** for Windows. It automatically sorts files in a folder into categorized subfolders based on their type, helping you keep your Desktop, Downloads, and other directories clean and organized.

---

## Features

- **Organizes files by type**: Images, Videos, Audio, Documents, Archives, Code, Design files, Apps, Fonts, and more.
- **Nested subfolders for Documents and Archives**: PDF, Word, Excel, Presentations, ZIP, RAR, 7Z, etc.
- **Apps support**: EXE, MSI, BAT, CMD, shortcuts, and more.
- **Others folder**: Moves uncategorized files to `Others`.
- **Cross-folder command**: Run FolderFlow on any folder with a simple command.
- **Windows installer included**: Automatically sets up FolderFlow in your PATH so you can run `folderflow .` anywhere.

---

## Installation

### Windows

1. Download `folderflow.py` and `install_folderflow.bat`.
2. Place both files in the same folder.
3. Double-click **`install_folderflow.bat`** and follow the instructions.
4. Open a new Command Prompt or PowerShell.

Now you can run:

```cmd
folderflow .
```

to organize the current folder, or:

```cmd
folderflow C:\Path\To\Folder
```

to organize a specific folder.

---

## Usage

Simply run FolderFlow in the folder you want to organize:

```cmd
folderflow .
```

FolderFlow will automatically:

- Move files to the appropriate folder based on their type.
- Create subfolders for documents, archives, code, and design files when needed.
- Move unknown file types to the `Others` folder.

---

## File Categories

**Top-level folders:**

- Images, Videos, Audio, Apps, Disk Images, Fonts

**Nested folders for Documents:**

- PDF, Word, Excel, Presentations, Text

**Nested folders for Archives:**

- ZIP, RAR, 7Z, TAR

**Nested folders for Code:**

- Python, JavaScript, HTML_CSS, Java, C_CPP, CSharp, Other

**Nested folders for Design:**

- Photoshop, Illustrator, XD, Figma, Sketch, InDesign, SVG

**Nested folders for DevResources:**

- Env, YAML, Config, Docker, Git

---

## Notes

- Requires **Python 3** installed on Windows.
- The installer uses the **Windows Python launcher (`py`)** to run FolderFlow, so it works even if Python is not in PATH.
- Designed for **Windows only**.

---

## License

This project is licensed under the MIT License.
Feel free to use, modify, and distribute.

---

## Contributing

If you find bugs or want to suggest improvements:

1. Fork the repository
2. Create a new branch
3. Submit a pull request

Your contributions are welcome!

---
