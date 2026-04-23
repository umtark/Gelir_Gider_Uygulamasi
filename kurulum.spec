# -*- mode: python ; coding: utf-8 -*-
#
# kurulum.spec
# Bu spec, main app (dist/fatura_masaustu/) klasorunu icine gomup
# tek bir GelirGiderApp_Kurulum.exe uretir.

block_cipher = None

a = Analysis(
    ['kurulum.py'],
    pathex=[],
    binaries=[],
    datas=[
        # Derlenmis main app klasorunu bundle'a ekle
        ('dist/fatura_masaustu', 'fatura_masaustu'),
    ],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='GelirGiderApp_Kurulum',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=None,
)
