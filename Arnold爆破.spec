# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['C:\\Users\\Lenovo\\Desktop\\猫脸变换2\\Arnold爆破.py'],
    pathex=[],
    binaries=[],
    datas=[],
    hiddenimports=['pkg_resources', 'tkinter', 'Pillow'],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='Arnold爆破',
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
    icon=['C:\\Users\\Lenovo\\Desktop\\猫脸变换2\\微信图片_20241219191552.ico'],
)
