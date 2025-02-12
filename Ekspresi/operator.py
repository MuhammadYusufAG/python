#  Jenis jenis operator

# Operator Aritmatika

'''
Jenis pertama adalah operator untuk melakukan operasi aritmetika. Perhatikan tabel di bawah ini untuk memahami contoh penerapan operator aritmetika. Asumsikan x bernilai 11 dan y bernilai 5. 

Operator	Deskripsi	Contoh
Penjumlahan (+)
Menambahkan nilai dari kedua operan.
x + y = 16

Pengurangan (-)
Mengurangi nilai dari kedua operan.
x - y = 6

Perkalian (*)
Mengalikan nilai dari kedua operan.
x * y = 55

Pembagian Bulat (//)
Membagi nilai dari kedua operan. Jika operan adalah integer, hasil operasi adalah bilangan bulat.
x // y = 2

Pembagian Riil (/)
Membagi nilai dari kedua operan. Jika operan adalah float, hasil operasi adalah bilangan riil.
x / y = 2.2

Modulo (%)
Sisa hasil pembagian nilai dari dua operan.
x % y = 1

Pangkat (**)
Memangkatkan nilai dari dua operan.
x ** y = 161051

Semua operator aritmetika di atas adalah jenis untuk melakukan operasi aritmetika yang sering dijumpai. Mari lihat penerapannya pada Python.
'''

x = 11
y = 5

print(x + y)
print(x - y)
print(x * y)
print(x // y)
print(x / y)
print(x % y)
print(x ** y)


# Operator Relasional
'''
Operator relasional merupakan operator perbandingan antara dua operan yang berupa 
integer, float, string, ataupun boolean. Hasil akhir dari operator ini adalah nilai bertipe boolean. 
Perhatikan tabel di bawah untuk memahami contoh penerapan operator relasional. Asumsikan kedua variabel bertipe numerik atau float dengan x bernilai 5 dan y bernilai 10. 

Operator	Deskripsi	Contoh
Sama dengan (==)
Menghasilkan True, jika kedua operan bernilai sama.
x == y, menghasilkan False. 

Tidak Sama dengan (!=)
Menghasilkan True, jika kedua operan tidak bernilai sama.
x != y, menghasilkan True.

Lebih Besar dari (>)
Menghasilkan True, jika operan kiri lebih besar dari operan kanan.
x > y, menghasilkan False.

Kurang dari (<)
Menghasilkan True, jika operan kanan lebih besar dari operan kiri.
x < y, menghasilkan True.

Lebih Besar dari Sama dengan (>=)
Menghasilkan True, jika operan kiri lebih besar atau sama dengan operan kanan.
x >= y, menghasilkan False.

Kurang dari Sama dengan (<=)
Menghasilkan True, jika operan kanan lebih besar atau sama dengan operan kiri.
x <= y, menghasilkan True.
'''

x = 5
y = 10

print(x == y)
print(x != y)
print(x > y)
print(x < y)
print(x >= y)
print(x <= y)



# Operasi Logika
'''
Operator logika merupakan jenis operator untuk melakukan operasi logika dengan kedua 
operannya bertipe boolean. Hasil akhir dari operasi ini adalah nilai bertipe boolean. 
Perhatikan kode di bawah ini untuk memahami contoh penerapannya, 
asumsikan bahwa p bernilai True dan q bernilai False.

Operator	Deskripsi	Contoh
"AND" atau "&"
Logika yang hanya menghasilkan True jika kedua operan bernilai True.
p and q = False, p & q = False

"OR" atau "|"
Logika yang menghasilkan True jika salah satu dari kedua operan bernilai True.
p or q = True, p | q = True

NOT
Logika yang bertujuan untuk membalikkan nilai logika dari operannya.
not q = True
'''

# Operator And
print(True and True)
print(True and False)
print(False and True)
print(False and False)

# Operator Or
print(True or True)
print(True or False)
print(False or True)
print(False or False)

# Operator Not
print(not True)
print(not False)



# Operator Assignment
'''
Operator selanjutnya adalah assignment. Operator ini bertujuan untuk melakukan proses 
assignment atau pemberian nilai pada suatu variabel dengan nilai tetap. Perhatikan tabel di 
bawah ini untuk memahami contoh penerapan operator assignment. 
Asumsikan x bernilai 11 dan y bernilai 5.

Operator	Deskripsi	Contoh
+=
Menyederhanakan operasi x = x + y.
x += y, menghasilkan nilai 16.

-=
Menyederhanakan operasi x = x - y.
x -= y, menghasilkan nilai 6.

*=
Menyederhanakan operasi x = x * y.
x *= y, menghasilkan nilai 55.

/=
Menyederhanakan operasi x = x / y.
x /= y, menghasilkan nilai 2.2.

%= 
Menyederhanakan operasi x = x % y.
x %= y, menghasilkan nilai 1.
'''

# +=
x = 11
x += 5
print(x)

# -=
x = 11
x -= 5
print(x)

# *=
x = 11
x *= 5
print(x)

# /=
x = 11
x /= 5
print(x)

#%=
x = 11
x%= 5
print(x)


# contoh dari fungsi operator assignment
x = 11
x += 5
print(x)


x = 11
x = x + 5
print(x)