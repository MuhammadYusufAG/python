# Syntak Error

# if 9>10:
# print("Hello World!") #IndentationError: expected an indented block after 'if' statement on line 1

# i = 1
# while i < 3
#     print('dicoding')
#     i+= 1
'''
while i < 3
            ^
SyntaxError: expected ':'
'''

'''
File "<nama file>", line <nomor baris>
    <baris kode dengan kesalahan>
                ^
    <tipe kesalahan>: <pesan kesalahan>

Mari bedah satu per satu poin di atas.

"<nama file>" merupakan file Python yang Anda eksekusi. Jika Anda menggunakan mode script melalui lokal komputer dan program Anda menghasilkan Error, pesan ini akan memunculkan nama script atau file Python Anda. 
<nomor baris> merupakan nomor baris kode dalam file Anda yang mengalami kesalahan. 
<baris kode> merupakan kode yang mengalami kesalahan dalam file Anda. 
<tipe kesalahan> merupakan kelompok atau tipe kesalahan yang Anda alami, contohnya SyntaxError dan IndentationError.
<pesan kesalahan> merupakan pesan detail kesalahan atau keterangan yang diberikan oleh program. Contohnya adalah “invalid syntax” dan “expected an indented block”.
'''

# Pengecualian (Exceptions)

# print(angka) #NameError: name 'angka' is not defined

# bukan_angka = '1'
# bukan_angka + 2
'''
  bukan_angka + 2
    ~~~~~~~~~~~~^~~
TypeError: can only concatenate str (not "int") to str
'''

# Penanganan Pengecualian

# z = 0
# print(1/z)
'''
    print(1/z)
          ~^~
ZeroDivisionError: division by zero
'''

# use try except
z = 0 
try:
    print(1/z)
except ZeroDivisionError:
    print("Tidak dapat membagi dengan nol")


# use try except else finally
var_dict = {'rata-rata': '1,0'}

try:
    print(f"rata-rata adalah {var_dict['rata_rata']}")  # ini akan berhasil dan akan mencetak nilai rata-rata
except KeyError:  # ini akan diabaikan karena tidak ada KeyError
    print("Kunci tidak ditemukan")  # ini tidak akan dicetak
except TypeError:  # ini juga akan diabaikan karena tidak ada TypeError
    print("Anda tidak bisa membagi nilai dengan tipe data string")  # ini tidak akan dicetak
else:  # ini akan dijalankan karena tidak ada pengecualian
    print("Kode ini dieksekusi jika tidak ada exception.")
finally:
    print("Kode ini dieksekusi terlepas dari ada atau tidaknya exception.")


# Raise Exception
var = -1
if var < 0:
    raise ValueError("Nilai tidak boleh negatif")
else:
    for i in range(var):
        print(i)