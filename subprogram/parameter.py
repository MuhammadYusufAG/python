# documentasi = https://docs.python.org/3/glossary.html#term-parameter

# 1.Positional-or-Keyword
'''
Jenis ini merupakan parameter default dalam Python. Dengan jenis ini, kita dapat menggunakan positional maupun keyword argument 
ketika memanggil fungsi.
'''

def greeting (nama,pesan):
    return f"Halo, {nama}!, {pesan}"

print(greeting('Yusuf','selamat pagi'))
print(greeting(pesan="Selamat sore!", nama="Dicoding"))

'''
Pada contoh di atas, kita membuat fungsi untuk menyapa dengan parameternya adalah “nama” dan “pesan”. Ketika memanggil fungsi 
tersebut, kita bisa menggunakan dua jenis argumen, yakni positional dan keyword.
'''


# 2.Positional-Only
'''
Parameter ini hanya dapat dimanfaatkan dengan menggunakan jenis argumen posisi saat pemanggilan fungsi. Parameter ini ditentukan 
menggunakan sintaks "/".
'''
def penjumlahan (a,b,/):
    return a + b    
print(penjumlahan(12,3))
'''
Pada contoh di atas, kita memanggil fungsi yang telah didefinisikan menggunakan positional argument. Perhatikan juga bahwa 
kita mendefinisikan parameter fungsi dengan sintaks "/".

Silakan ganti kode pemanggil fungsi dengan kode berikut untuk mengetahui hal yang terjadi jika kita menggunakan keyword argument.

'''
# print(penjumlahan(a=3, b=5))
'''
print(penjumlahan(a=3, b=5))
          ~~~~~~~~~~~^^^^^^^^^^
TypeError: penjumlahan() got some positional-only arguments passed as keyword arguments: 'a, b'
'''


# 3.keyword-only
'''
Jenis ketiga adalah kebalikan dari yang sebelumnya. Kita harus menggunakan keyword argument untuk memanggil fungsi dengan jenis 
parameter ini. Ia ditentukan dengan sintaks "*" (asterisk).
'''

def greeting (*,nama,pesan):
    return f"Halo, {nama}!, {pesan}"
print(greeting(pesan="Selamat sore!",nama="Dicoding"))
'''
Pada contoh di atas, kita menggunakan keyword argument untuk memanggil fungsi yang telah dibuat. Perhatikan bahwa kita menggunakan 
sintaks "*" untuk mendefinisikan bahwa parameter fungsi ini hanya bisa dipanggil menggunakan keyword argument.

Silakan ganti baris pemanggil kode dengan kode di bawah ini untuk mengetahui hal yang terjadi jika kita menggunakan positional 
argument.
'''
# print(greeting("Selamat sore!","Dicoding"))
'''
 print(greeting("Selamat sore!","Dicoding"))
          ~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: greeting() takes 0 positional arguments but 2 were given
'''


# 4.Var-Positional (Variadic Positional Parameter)
'''
Parameter ini menampung jumlah argumen posisi yang bervariasi saat pemanggilan fungsi. Parameter ini ditentukan
dengan menggunakan sintaks *args.
'''

def hitung_total(*args):
    print(type(args))
    total = sum(args)
    return total

print(hitung_total(1,23,3))
'''
Pada contoh di atas, parameter *args mengumpulkan semua argumen posisi yang diberikan saat pemanggilan fungsi 
dan membungkusnya menjadi tuple "args". Dalam situasi ini, Anda bisa memasukkan angka sebanyak apa pun dalam argumen fungsi.

Silakan tambahkan integer lainnya sebanyak yang Anda mau pada kode pemanggil fungsi di atas untuk mengetahui perbedaannya. 
Contohnya Anda bisa memasukan kode berikut.
'''
print(hitung_total(1, 2, 3, 4, 5, 6, 7, 8))


# var-keyword(Variadic Keyword Parameter)
'''
Parameter ini dapat menampung jumlah keyword argument yang bervariasi saat pemanggilan fungsi. Parameter ini ditentukan dengan 
menggunakan sintaks **kwargs yang berperan sebagai dictionary (seperti tipe datanya). Argumen pada pemanggil fungsi akan berperan
sebagai value dan parameter (identifier) berperan sebagai key.
'''

