"""
Shinrin CS — PyInstaller Build Script.

Oyunu tek dosyalık .exe'ye paketler.
Kullanım: py build.py
"""

import subprocess
import sys
import os

def build():
    """PyInstaller ile .exe oluşturur."""
    print("=" * 50)
    print("Shinrin CS — Build başlıyor...")
    print("=" * 50)

    cmd = [
        sys.executable, "-m", "PyInstaller",
        "--onefile",
        "--windowed",
        "--name", "ShinrinCS",
        "--add-data", "settings.json;.",
        "--icon", "NONE",
        "main.py"
    ]

    # Eğer data klasörleri varsa ekle
    data_dirs = ["saves", "assets", "data"]
    for d in data_dirs:
        if os.path.exists(d):
            cmd.extend(["--add-data", f"{d};{d}"])

    print("Komut:", " ".join(cmd))
    result = subprocess.run(cmd, cwd=os.path.dirname(os.path.abspath(__file__)))

    if result.returncode == 0:
        print("\n" + "=" * 50)
        print("Build başarılı! → dist/ShinrinCS.exe")
        print("=" * 50)
    else:
        print("\nBuild BAŞARISIZ!")
        sys.exit(1)


if __name__ == "__main__":
    build()
