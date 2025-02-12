# len() untuk menghitung panjang atau banyaknya elemen dari list, set, dan string. Khusus pada string, program akan menghitung jumlah karakternya.

# len() LIST
exam_list = [1, 3, 3, 5, 5, 5, 7, 7, 9]
print(exam_list)
print(len(exam_list))

# len() SET
exam_set = set([1, 3, 3, 5, 5, 5,7,7,9])
print(exam_set)
print(len(exam_set))

# len() STRING
exam_string = "Hello, World!"
print(exam_string)
print(len(exam_string))


# min() dan max()
'''Selain menghitung panjang atau banyaknya elemen, Anda juga dapat mengetahui berapa nilai minimum dan 
maksimum dari suatu list menggunakan fungsi min() dan max().'''
angka = [13, 7, 24, 5, 96, 84, 71, 11, 38]
print(min(angka))
print(max(angka))


# count() digunakan untuk mengetahui berapa kali suatu objek muncul dalam list.
genap = [2, 4, 4, 6, 6, 6, 8, 10, 10]
print(genap.count(10))

string = "Belajar Python di Dicoding sangat menyenangkan"
substring = "a"
print(string.count(substring))


# in and Not in
'''
merupakan operator yang diperuntukkan untuk mengetahui nilai atau 
objek yang ada dalam list. Anda bisa menggunakan operator ini untuk 
memastikan suatu nilai ada dalam list bahkan dalam string. 
Operator in dan not in akan mengembalikan nilai boolean True atau 
False. '''

kalimat = "Belajar Python di Dicoding sangat menyenangkan"
print('Dicoding' in kalimat)
print('tidak' in kalimat)
print('Dicoding' not in kalimat)
print('tidak' not in kalimat)


# memberikan nilai untuk multiple variable
data = ['shirt', 'white', 'L']
# apparel = data[0]
# color = data[1]
# size = data[2]
apparel, color, size = data

print(data)
print(apparel)
print(color)
print(size)


# sort() untuk mengurutkan angka atau urutan huruf.
kendaraan = ['motor', 'mobil', 'helikopter', 'pesawat']
kendaraan.sort()
print(kendaraan)

# tidak bisa mengurutkan yg berisi angka dan string sekaligus didalamnya
# urutan = ['Dicoding', 1, 2, 'Indonesia', 3]
# urutan.sort()

# print(urutan)
# TypeError: '<' not supported between instances of 'int' and 'str'

# Metode sort menggunakan urutan ASCII sehingga nilai huruf kapital (uppercase) akan lebih dahulu dibandingkan huruf kecil (lowercase).

kendaraan = ['motor', 'mobil', 'helikopter', 'Pesawat']
kendaraan.sort()

print(kendaraan)