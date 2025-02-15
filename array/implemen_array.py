# mendeklarasikan array
var_list = [1, 2, 3,]
for element in var_list:
    print(id(element))

# mendefinisikan array
'''
<nama-variable> = [ <val0>, <val1>, <val2>, … , <valn-1>]

<nama-var> merupakan nama variabel array yang dideklarasikan sebanyak n dengan elemen-elemennya adalah <val0>, <val1>, <val2>, … , <valn-1>. 
Perlu diingat bahwa elemen tersebut terurut berdasarkan indeks dari 0 hingga n-1. 
'''

var_arr = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
print(var_arr)


# mendefinisikan nilai default
'''
<nama-variable> = [ <default-value> for in range(<n>)]

Jika Anda merasa familier dengan struktur tersebut, Anda benar. Struktur tersebut merupakan struktur yang sama dengan list comprehension. Anda dapat menginisialisasi variabel array dengan menggunakan list comprehension dan mendefinisikan nilai default. Pada materi List Comprehension, kita menggunakan ekspresi Namun, pada array kita menggunakan default value atau <default-val>.

Berikut adalah penjelasan lebih detail terkait struktur tersebut.

<nama-var> merupakan variabel yang Anda deklarasikan.
<default-val> merupakan nilai default yang Anda definisikan. Umumnya, programmer akan menggunakan nilai di luar range yang telah disepakati sebagai nilai default. Misalnya jika range nilai yang disepakati seharusnya 1 hingga 10, nilai default bisa kita definisikan dengan 0. 
<n> merupakan ukuran panjangnya array.
'''
var_arr = [ 0 for i in range(10) ]
print(var_arr)

var_arr = [ 0 for i in range(10)]
for i in range(10):
    var_arr[i] = i
print(var_arr)


# mengakses element array
'''
<namaVariableArray>[<indeks>]

<namaVariabelArray> merupakan nama variabel array yang sebelumnya telah Anda deklarasikan.
<indeks> merupakan urutan indeks yang ingin Anda akses sehingga nilai atau elemen tersebut dapat diambil atau ditampilkan.
'''
var_arr = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
print(var_arr[4]) # 5