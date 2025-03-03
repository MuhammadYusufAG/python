# Statement Gabungan
# Saat Anda membuat program dengan banyak statement, usahakan untuk tidak menggabungkan >1 statement pada baris yang sama.

# Disarankan seperti ini.
# if foo == 'blah':
#     do_blah_thing()

# do_one()
# do_two()
# do three()

# tidak disarankan seperti ini
# if foo == 'blah': do_blah_thing()
# do_one(); do_two(); do_three()


'''
Anda diperbolehkan untuk membuat sebuah konten/isi dari if/for/while yang cukup pendek untuk diletakkan dalam satu baris (program tetap berjalan). 
Namun, pastikan tidak melakukannya jika if/for/while Anda bertingkat atau bersifat multi clause, misalnya if-else, try-finally, dan sebagainya.
'''

# tidak disarankan seperti ini
# if foo == 'blah': do_blah_thing()
# for x in lst: total += x
# while t < 10: t = delay()

# sangat tidak disarankan seperti ini
# if foo == 'blah': do_blah_thing()
# else: do_non_blah_thing()
# try: something()
# finally: cleanup()
# do_one(); do_two(); do_three(long, argument,
#                              list, like, this)
# if foo == 'blah': one(); two(); three()



# Penggunaan Trailing Commas
'''
Koma di bagian akhir (trailing commas) umumnya bersifat opsional, satu statement yang bersifat wajib adalah saat kita membuat variabel menggunakan 
tipe tuple dengan satu elemen. Hal ini umumnya diperjelas dengan kurung untuk menghindari penghapusan atau pembersihan.
'''

# disarankan
FILES = ('setup.cfg',)

# tidak disarankan
FILES = 'setup.cfg',

'''
Saat trailing comma bersifat redundan, Anda akan merasakan kemudahannya saat menggunakan VCS (Version Control System), 
atau pada kode yang mungkin ditambahkan dalam beberapa waktu ke depan. Pola yang disarankan adalah meletakkan nilai atau string pada sebuah baris
baru, mengikuti indentasi, menambahkan trailing comma, dan menutup kurung/kurawal/siku pada baris selanjutnya.

Tidak umum jika Anda menempatkan trailing comma pada baris letak Anda menutup kurung/kurawal/siku seperti di bawah ini, 
kecuali dalam tuple dengan satu elemen, seperti yang dijelaskan di atas.
'''

# disarankan
# FILES = [
#     'setup.cfg',
#     'setup.py',
# ]

# initialize(FILES,
#            error = true)


# tidak disarankan
# FILES = ['setup.cfg', 'tox.ini',]
# initialize(FILES, error=True,)


# ANOTASI FUNGSI
'''
Anotasi fungsi adalah fitur yang memungkinkan kita untuk menambahkan informasi tambahan tentang parameter 
dan return value dari sebuah fungsi. Jika sebelumnya kita belajar menambahkan informasi terkait fungsi dengan menambahkan docstring, anotasi 
fungsi lebih spesifik untuk menjelaskan parameter dan return value.

Penggunaan anotasi fungsi sebaiknya menggunakan aturan baku untuk titik dua (:) dan menggunakan spasi untuk penggunaan arah panah atau arrow (->). 
Hal ini disebut sebagai type hints yang merujuk pada PEP 484.

pep 484: https://peps.python.org/pep-0484/
'''

# Yes:
def munge(input: str):
    pass
def munge() -> str:
    pass

# No:
def munge(input:str):
    pass
def munge()->str:
    pass

'''
Pada contoh di atas, kita memberikan informasi bahwa parameter dan return value harus berupa tipe data string. Kita bisa menentukannya dengan tipe 
lain, seperti 'int' untuk integer dan 'float' untuk tipe data float.

Selanjutnya, saat membuat fungsi dan Anda menggabungkan anotasi dengan nilai parameter, sebaiknya tetap menggunakan spasi baik sebelum dan sesudah 
tanda sama dengan (=).
'''

def LuasPersegiPanjang(panjang: int = 2, lebar: int = None ):
    pass

'''
Pada contoh di atas, kita membuat fungsi bernama "LuasPersegiPanjang" untuk mencari luas persegi panjang dengan parameter panjang dan lebar. 
Sintaks berikut menjelaskan bahwa parameter panjang dan lebar harus bertipe data integer.
'''

# panjang: int
'''
Sementara itu, ketika menambahkan variabel setelah sama dengan (=) akan memberikan nilai default. Contohnya sintaks berikut akan memberikan 
nilai default 2 untuk parameter panjang.
'''

# panjang: int = 2

'''Sekarang mari lihat contoh keseluruhan kode dan cara memanggilnya.'''

def LuasPanjangPersegi(panjang: int = 2, lebar: int = None ):
    luas = panjang * lebar
    return luas

luas_satu = LuasPanjangPersegi(lebar=2)
print(luas_satu)


'''
Pada contoh di atas, kita membuat fungsi untuk mencari luas persegi panjang dengan parameter panjang dan lebar. Perlu diingat bahwa pada fungsi 
tersebut kita memberikan nilai default 2 untuk parameter panjang. Hal ini mengakibatkan bahwa ketika memanggil fungsi LuasPersegiPanjang dengan 
hanya memasukkan argumen lebar, program akan tetap berjalan dengan baik.

Namun, perlu diingat bahwa karena type hints bersifat optional dan memberikan petunjuk, jika pada fungsi LuasPersegiPanjang kita memberikan tipe 
data float, program akan tetap berjalan sebagaimana mestinya. 

Sekarang, kita masuk ke skenario baru. Jika pada saat membuat fungsi tanpa adanya anotasi bahwa parameternya menandakan keyword argumen atau nilai 
default, hindari penggunaan spasi di sekitar tanda sama dengan (=).
'''

# Yes:
def LuasPersegiPanjang(panjang=2, lebar=None):
    luas = panjang*lebar
    return luas
 
# No:
def LuasPersegiPanjang(panjang = 2, lebar = None):
    luas = panjang*lebar
    return luas

'''
Pada contoh di atas, kita membuat fungsi luas persegi panjang yang sama seperti sebelumnya. Perhatikan bahwa kita tidak menyertakan anotasi
berupa "panjang:int".

Mari kita simpulkan sedikit. Jika kita membuat fungsi yang menggabungkan anotasi dengan nilai parameter, sebaiknya tetap menggunakan spasi 
sebelum dan sesudah tanda sama dengan (=). Namun, ketika membuat fungsi biasa tanpa adanya anotasi, sebaiknya tidak menggunakan spasi sebelum dan 
sesudah tanda sama dengan (=).
'''

# Yes:
def LuasPersegiPanjang(panjang:int = 2, lebar=None):
    pass
 
# No:
def LuasPersegiPanjang(panjang: int=2, lebar = None):
    pass

'''Pada contoh di atas, kita menggabungkan dalam satu fungsi; parameter panjang menggabungkan anotasi fungsi dan nilai default, sedangkan parameter 
lebar hanya mendefinisikan nilai default tanpa anotasi fungsi. Perhatikan bahwa spasi ditempatkan pada setiap parameternya.'''