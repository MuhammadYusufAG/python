# matriks
matriks = [[1,2,3,],
           [4,5,6],
           [7,8,9]]
print(matriks)


# implementasi numpy

'''
Silakan periksa bahwa library NumPy tersedia di komputer Anda dengan menjalankan kode berikut di terminal Anda.

pip show numpy

Jika dalam komputer Anda belum memiliki NumPy, silakan buka kembali terminal Anda dan jalankan perintah berikut.

pip install numpy

Mari lanjutkan dengan implementasi matriks menggunakan NumPy.
'''

import numpy

matriks = numpy.array([[1,2,3,],[4,5,6],[7,8,9]])
print(matriks)


# bandingkan ukuran memori yang digunakan jika kita menggunakan matriks Python dan matriks NumPy.
import numpy
import sys

var_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
var_array = numpy.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

print("Ukuran keseluruhan elemen list dalam bytes = ",sys.getsizeof(var_list)*len(var_list))
print("Ukuran keseluruhan elemen NumPy dalam bytes = ",var_array.size*var_array.itemsize)