# Membuat matriks 2x2
var_mat = [[5, 0],
          [1, -2]]

default_math = [[0 for j in range(2)] for i in range(2)]

# perhitungan
for i in range(len(var_mat)):
    for j in range(len(var_mat[0])):
        default_math [i][j] = var_mat [i][j]*2 #matriks dikali 2
print(default_math)

'''
Perhatikan penjelasan berikut untuk memahami contoh di atas.

Pertama, kita mendeklarasikan variabel "var_mat" dan menginisialisasikannya dengan matriks yang diinginkan. Di sini, matriks yang digunakan berukuran 2x2 atau 2 baris dan 2 kolom.
Kedua, kita perlu mendeklarasikan variabel "def_mat" sebagai matriks default baru dengan nilai (0). Matriks dengan nilai default ini harus berukuran sama dengan matriks yang asli.
Ketiga, kita akan melakukan perulangan berdasarkan dua kondisi. Kondisi pertama adalah perulangan berdasarkan banyaknya list di dalam matriks ([5, 0], [1, -2]) yang merepresentasikan baris. Kondisi kedua adalah perulangan berdasarkan banyaknya elemen pada setiap list (5,0 dan 1,-2).
'''

# lebih simple use numpy

import numpy as np
var_mat = np.array([[5, 0],
                   [1, -2]])

result = var_mat * 2
print(result)

'''
Pada contoh di atas, kita melakukan operasi perkalian matriks dengan konstanta yang sama seperti sebelumnya. Bedanya, kali ini kita menggunakan library NumPy untuk mempermudah pengkodean. Bisa Anda lihat bahwa dengan menggunakan NumPy kita tidak perlu lagi menggunakan nested for dan cukup mengalikan matriks dengan konstanta yang diinginkan. Dalam hal ini ditunjukkan pada kode berikut.

result = var_mat * 2
Anda masih bisa bereksplorasi dengan operasi matriks lainnya seperti transpose matriks, inverse matriks, dan sebagainya. Silakan bereksplorasi.
'''