

import os

DIRPATH = r'D:\Chrome Downloads\Free Faces Pack\Free Faces Pack\x80'
imgs = os.listdir(DIRPATH)

for img in imgs:
    renamed = ''.join( img.split('w') )
    renamed = ''.join( renamed.split('m') )
    os.rename( rf"{DIRPATH}\{img}", rf"{DIRPATH}\{renamed}")

print("DOne")