@echo off
cd /d "%~dp0"

set QT_LOGGING_RULES=qt.multimedia.*=false

if exist ".venv\Scripts\pythonw.exe" (
    start "" ".venv\Scripts\pythonw.exe" "%~dp0fatura_masaustu.py"
) else (
    echo .venv bulunamadi. Lutfen once kurulum yapin.
    pause
    exit /b 1
)
exit /b 0
