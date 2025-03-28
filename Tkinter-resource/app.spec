 #app.spec

from PyInstaller.utils.hooks import collect_data_files

# Define paths to your directories
tesseract_dir = 'Tesseract-OCR'
ffmpeg_dir = 'ffmpeg-v1/bin'

# Analysis section
a = Analysis(
    ['app.py'],
    pathex=['.'],
    binaries=[],
    datas=[
        (tesseract_dir, 'Tesseract-OCR'),  # Include all files and subdirectories in Tesseract-OCR
        (ffmpeg_dir, 'ffmpeg-v1/bin'),     # Include all files and subdirectories in ffmpeg-v1/bin
    ],
    hiddenimports=[],
    hookspath=[],
    runtime_hooks=[],
    excludes=[],
)

# PYZ section
pyz = PYZ(a.pure, a.zipped_data)

# EXE section
exe = EXE(
    pyz,
    a.scripts,
    exclude_binaries=True,
    name='Tkinter-app',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,
)

# COLLECT section
coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    name='Tkinter-app',
)
