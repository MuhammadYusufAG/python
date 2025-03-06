import re

pola = '^a...s$'
string_test = 'abyss'
hasil = re.match(pola, string_test)

if hasil:
    print("Pencarian berhasil.")
else:
    print("Pencarian gagal.") 