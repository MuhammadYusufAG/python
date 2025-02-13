# FOR
#  for <var> in <iterable>:
#      <statement(s)>

var_list = [1,2,3,4,5,6,7,8,9,10]
for i in var_list:
    print(i)

for i in range(10):
    print(i)

# range(start,stop,step)
'''
Berikut adalah penjelasan detail terkait fungsi "range()".

"Start" merupakan nilai awal dari urutan bilangan yang bersifat opsional, jika Anda tidak memasukkannya, nilai awal akan dianggap 0. 
"Stop" merupakan nilai batas yang wajib dimasukkan. Urutan akan berhenti sebelum mencapai nilai "stop" (eksklusif). 
"Step" merupakan nilai penambahan antara setiap dua bilangan dalam urutan yang bersifat opsional. 
Jika nilai tersebut tidak diberikan, secara default nilai yang dimasukkan adalah 1.
'''
for i in range(1,10,2):
    print(i)



# WHILE
counter = 1
while counter <= 5:
    print(counter)
    counter += 1 #jika tidak ada ini akan looping


#FOR Bersarang
for i in range(1,3):
    for j in range(1,3):
        print(i,j)

# Kontrol Loop

# break
for i in range(2): #perulangan tingkat pertama
    print('perulangan luar:',i)
    for j in range(10): #perulangan tingkat kedua
        print('perulangan dalam:',j)
        if j == 1:
            break #menghentikan perulangan dalam jika j = 1

for huruf in 'Dico ding':
    if huruf == ' ':
        break
    print(f'Huruf saat ini: {huruf}')

# continue
for huruf in 'Dico ding':
    if huruf == ' ':
        continue
    print(f'Huruf saat ini: {huruf}')

"""
Output:
Huruf saat ini: D
Huruf saat ini: i
Huruf saat ini: c
Huruf saat ini: o
Huruf saat ini: d   # Perhatikan bahwa harusnya sebelum ini ada spasi, namun dilewati.
Huruf saat ini: i
Huruf saat ini: n
Huruf saat ini: g
"""


#   ELSE after FOR
numbers = [1,2,3,4,5]

for i in numbers:
    if i == 6:
        print("Angka ditemukan! Program berhenti!")
        break
else:
    print("Angka tidak ditemukan!")


# ELSE after WHILE
count = 0
while count < 3:
    print('Dicoding Indonesia')
    count += 1
else:
    print('Blok else dieksekusi karena kondisi pada while salah (3<3 == False).')


n = 11
while n > 0:
    n = n - 1
    if n == 7: #jadi jika pengurangan udah selesai sampe angka 7 bakal dikeluarin yang udah dikurangin
        break
    print(n)
else:
    print("Loop selesai")


# PASS
x = 10

if x > 5: #jika x lebih besar dari 5 diakan jalanin pass
    pass
else:
    print("Nilai x tidak memenuhi kondisi")


# LIST Comprehension
angka = [1,2,3,4]
pangkat = []
for n in angka:
    pangkat.append(n**2) #append untukuntuk menambahkan nilai baru ke dalam variabel "pangkat"
print (pangkat)

# dipersingkat
angka = [1,2,3,4]
pangkat = [n**2 for n in angka]
print(pangkat)

# new_list = [expression for_loop_one_or_more_conditions]
'''
Mari bedah satu per satu struktur tersebut.

new_list merupakan variabel yang dideklarasikan oleh Anda.
expression merupakan ekspresi yang akan dijalankan seiring perulangan bernilai benar.
for_loop_one_or_more_conditions merupakan perulangan for yang Anda definisikan. Misalnya "for n in angka" yang ada pada contoh sebelumnya.
'''