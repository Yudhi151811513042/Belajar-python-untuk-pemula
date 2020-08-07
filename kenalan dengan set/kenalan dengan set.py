"""
SETS
"""

orang = {'hilman','boss', 'komen', 'hilman'}
orang.add('alex')
orang.remove('boss')

print(orang)
angka1 = {1,2,3,4,5}
angka2 = {4,5,6,7,8}

print(angka1 & angka2) # mengambil angka yang sama
print(angka1 - angka2) # menampilkan angka yang tidak ada persamaan tergantung urutan
print(angka1 ^ angka2) # tidak ditampilkan angka yang sama
print(angka1 | angka2) # union