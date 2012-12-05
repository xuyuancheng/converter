# -*- mode: python -*-
a = Analysis([os.path.join(HOMEPATH,'support\\_mountzlib.py'), os.path.join(HOMEPATH,'support\\useUnicode.py'), 'D:\\statistical_new\\converter.py'],
             pathex=['D:\\pyinstaller-1.5.1'])
pyz = PYZ(a.pure)
exe = EXE( pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name=os.path.join('dist', 'converter.exe'),
          debug=False,
          strip=False,
          upx=True,
          console=False , icon='D:\\2.ico')
app = BUNDLE(exe,
             name=os.path.join('dist', 'converter.exe.app'))
