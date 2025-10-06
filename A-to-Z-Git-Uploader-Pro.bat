@echo off
title 🚀 A-to-Z Git Uploader PRO v2 by Sadik
echo ===================================================
echo   🚀  A-to-Z Git Uploader PRO v2  (Auto + Smart)
echo ===================================================
echo.

REM === Step 1: Go to your repo folder ===
cd /d "C:\Users\Sadik Khan\Desktop\Git Uploads\youtube-stream-video1"

REM === Step 2: Initialize Git LFS ===
git lfs install

REM === Step 3: Track large file types ===
git lfs track "*.mp4"
git lfs track "*.zip"
git lfs track "*.rar"
git lfs track "*.exe"
git lfs track "*.iso"

REM === Step 4: Check for new changes ===
for /f "tokens=*" %%i in ('git status --porcelain') do set CHANGED=1

if not defined CHANGED (
    echo ⚠️  No new files to commit or upload.
    echo (Nothing new to push)
    pause
    exit /b
)

REM === Step 5: Add, Commit and Push ===
git add .
git commit -m "Auto-upload detected files with Git LFS"
git push origin main

if %errorlevel%==0 (
    echo.
    echo ✅ Upload completed successfully!
    echo 🌐 Opening your GitHub repository page...
    start https://github.com/whatashort51-cmd/youtube-stream-video1
) else (
    echo ❌ Upload failed! Please check your internet or Git settings.
)

echo.
echo Press any key to close...
pause >nul
