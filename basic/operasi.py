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


# count()