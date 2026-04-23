"""
GelirGider Kurulum Launcher
----------------------------
- Ilk calistirmada: dist/fatura_masaustu/ klasorunu
  %LOCALAPPDATA%\GelirGiderApp\ altina kopyalar, masaustu kisayolu olusturur.
- Sonraki calistirmalarda: dogrudan kurulu exe'yi baslatir.
"""

import sys
import os
import shutil
import subprocess
from pathlib import Path


APP_NAME     = "GelirGiderApp"
EXE_NAME     = "fatura_masaustu.exe"
VERSION      = "1.0.0"
VERSION_FILE = "version.txt"


def get_bundle_dir() -> Path:
    """PyInstaller frozen exe ise _MEIPASS, degil ise proje koku."""
    if getattr(sys, "frozen", False):
        return Path(sys._MEIPASS)
    return Path(__file__).parent / "dist"


BUNDLE_APP_DIR = get_bundle_dir() / "fatura_masaustu"
INSTALL_DIR    = Path(os.environ.get("LOCALAPPDATA", str(Path.home()))) / APP_NAME
MAIN_EXE       = INSTALL_DIR / EXE_NAME


# ------------------------------------------------------------------ helpers --

def _msgbox(title: str, text: str, icon: int = 0x40) -> None:
    """Windows MessageBox (ctypes, bagimsiz)."""
    import ctypes
    ctypes.windll.user32.MessageBoxW(0, text, title, icon)


def _create_shortcut(target: Path, shortcut_path: Path) -> None:
    """PowerShell ile .lnk kisayolu olusturur (ekstra paket gerekmez)."""
    ps = (
        f'$s=(New-Object -ComObject WScript.Shell).CreateShortcut("{shortcut_path}");'
        f'$s.TargetPath="{target}";'
        f'$s.WorkingDirectory="{target.parent}";'
        f'$s.Save()'
    )
    subprocess.run(
        ["powershell", "-NoProfile", "-NonInteractive", "-Command", ps],
        capture_output=True,
    )


def _needs_install() -> bool:
    ver_file = INSTALL_DIR / VERSION_FILE
    if not MAIN_EXE.exists():
        return True
    if not ver_file.exists():
        return True
    return ver_file.read_text(encoding="utf-8").strip() != VERSION


# ------------------------------------------------------------------ install --

def install() -> None:
    _msgbox(
        "GelirGider — Kurulum",
        f"Uygulama ilk kez kuruluyor.\n"
        f"Hedef klasor: {INSTALL_DIR}\n\n"
        f"Tamam'a tiklayin, kurulum birkaç saniye sürecek.",
    )

    # Eski kurulumu temizle
    if INSTALL_DIR.exists():
        shutil.rmtree(str(INSTALL_DIR), ignore_errors=True)

    # Dosyalari kopyala
    shutil.copytree(str(BUNDLE_APP_DIR), str(INSTALL_DIR))

    # Versiyon dosyasi
    (INSTALL_DIR / VERSION_FILE).write_text(VERSION, encoding="utf-8")

    # Masaustu kisayolu
    desktop = Path(os.environ.get("USERPROFILE", str(Path.home()))) / "Desktop"
    shortcut = desktop / f"{APP_NAME}.lnk"
    _create_shortcut(MAIN_EXE, shortcut)

    _msgbox(
        "GelirGider — Kurulum Tamamlandi",
        f"Kurulum basariyla tamamlandi!\n"
        f"Masaustunuze '{APP_NAME}' kisayolu eklendi.\n\n"
        f"Uygulama simdi acilacak.",
    )


# --------------------------------------------------------------------- main --

def main() -> None:
    if _needs_install():
        if not BUNDLE_APP_DIR.exists():
            _msgbox(
                "Hata",
                f"Uygulama dosyalari bulunamadi:\n{BUNDLE_APP_DIR}\n\n"
                "Lutfen kurulum dosyasini yeniden indirin.",
                0x10,  # MB_ICONERROR
            )
            return
        install()

    if not MAIN_EXE.exists():
        _msgbox("Hata", f"Uygulama exe bulunamadi:\n{MAIN_EXE}", 0x10)
        return

    subprocess.Popen(
        [str(MAIN_EXE)],
        cwd=str(INSTALL_DIR),
    )


if __name__ == "__main__":
    main()
