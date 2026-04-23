@echo off
chcp 65001 > nul
cd /d "%~dp0"

echo ============================================================
echo    GelirGider Uygulama - EXE Build Araci
echo ============================================================
echo.

:: ---- PyInstaller kontrol / kur ----
echo [1/3] PyInstaller kontrol ediliyor...
".venv\Scripts\python.exe" -m pip install pyinstaller==6.12.0 --quiet
if errorlevel 1 (
    echo HATA: PyInstaller kurulamadi!
    pause & exit /b 1
)
echo     OK

:: ---- Ana uygulamayi derle (onedir) ----
echo.
echo [2/3] Ana uygulama tek exe olarak derleniyor (bu 2-5 dakika surebilir)...
".venv\Scripts\python.exe" -m PyInstaller fatura_masaustu.spec --noconfirm --clean
if errorlevel 1 (
    echo HATA: Ana uygulama derlenemedi!
    pause & exit /b 1
)
echo     OK - dist\fatura_masaustu.exe olusturuldu

:: ---- Sonuc ----
echo.
echo [3/3] Temizlik yapiliyor...
if exist "build" rmdir /s /q "build"
echo     OK

echo.
echo ============================================================
echo  TAMAMLANDI!
echo.
echo  Dagitim dosyasi:
echo    dist\fatura_masaustu.exe
echo.
echo  Bu tek dosyayi kullanicilara gonderin.
echo  Ilk calistirmada exe kendini ve veri klasorlerini sunuraya kurar:
echo    %%LOCALAPPDATA%%\GelirGiderApp\
echo  Sonraki acilislarda ayni kurulu exe uzerinden calisir.
echo ============================================================
echo.
pause
