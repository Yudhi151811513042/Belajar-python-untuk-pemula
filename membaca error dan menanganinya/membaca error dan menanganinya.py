"""
Exceptions
"""

name = "hilman"

# metode raise -> raise Exception("stop ada kesalahan")
"""
Metode try except
try:
    print(i + name)
except:
    print("wow ada yang salah")
"""
import sys
print(sys.platform)

def is_it_windows():
    assert ('win64' in sys.platform), "fungsi ini hanya untuk windows"

is_it_windows()
print('finish')