@echo off
REM -------------------------------------
REM FolderFlow Windows Installer (Fixed)
REM -------------------------------------

SETLOCAL

REM -----------------------------
REM Check Python installation via py launcher
REM -----------------------------
py --version >nul 2>&1
IF %ERRORLEVEL% NEQ 0 (
    echo Python is not installed or not in PATH.
    echo Please install Python 3 before running FolderFlow.
    pause
    exit /b
)

REM -----------------------------
REM Set installation folder
REM -----------------------------
SET FOLDERFLOW_DIR=%USERPROFILE%\FolderFlow
echo Installing FolderFlow to %FOLDERFLOW_DIR%...

mkdir "%FOLDERFLOW_DIR%" 2>nul

REM -----------------------------
REM Copy folderflow.py
REM -----------------------------
IF NOT EXIST folderflow.py (
    echo folderflow.py not found in the current folder.
    echo Please place this installer in the same folder as folderflow.py.
    pause
    exit /b
)

copy folderflow.py "%FOLDERFLOW_DIR%\folderflow.py" /Y

REM -----------------------------
REM Create wrapper batch file using py
REM -----------------------------
(
    echo @echo off
    echo py "%%~dp0folderflow.py" %%*
) > "%FOLDERFLOW_DIR%\folderflow.bat"

REM -----------------------------
REM Add FolderFlow to user PATH safely
REM -----------------------------
REM Get current user PATH from registry
FOR /F "tokens=2*" %%A IN ('reg query "HKCU\Environment" /v PATH 2^>nul') DO SET USER_PATH=%%B

REM If FolderFlow not already in PATH, append it
echo %USER_PATH% | find /I "%FOLDERFLOW_DIR%" >nul
IF %ERRORLEVEL% NEQ 0 (
    setx PATH "%USER_PATH%;%FOLDERFLOW_DIR%" >nul
)

echo.
echo FolderFlow installed successfully!
echo --------------------------------------
echo Open a new Command Prompt or PowerShell and type:
echo folderflow .   to organize the current folder
echo folderflow C:\Path\To\Folder   to organize a specific folder
echo --------------------------------------
pause

ENDLOCAL
