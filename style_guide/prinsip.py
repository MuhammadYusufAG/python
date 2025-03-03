from typing import TypeVar

VT_co = TypeVar('VT_co', covariant=True)
KT_contra = TypeVar('KT_contra', contravariant=True)

# Nama Exception
'''Untuk pengecualian (exception), Anda juga menerapkan konvensi penamaan kelas pada exception karena ia seharusnya bertipe kelas. Bedanya, 
tambahkan "Error" atau nama deskriptif lain pada nama exception Anda. Contoh kodenya sebagai berikut.'''

class DevideByZeroError(Exception):
    def __init__(self, message="Division by zero is not allowed"):
        super().__init__(message)

def devide_number(a, b):
    if b == 0:
        raise DevideByZeroError("Cannot divide by zero")
    return a / b

try:
    result = devide_number(10, 0)
except DevideByZeroError as e:
    print(f'Error: {e}')



# selalu persiapan untuk inheritence
'''
Saat membangun metode dan variabel dalam sebuah kelas, sebaiknya Anda dapat langsung mengetahui atribut pada metode dan variabel tersebut, entah 
publik atau non-publik. Jika Anda ragu, jadikan atributnya non-publik. Sebab, lebih mudah menjadikan sebuah variabel/method bersifat non-publik 
menjadi publik, dibandingkan sebaliknya.

Variabel atau method bersifat non-publik adalah suatu variabel atau method yang hanya digunakan untuk lingkup tertentu dan tidak diakses secara 
langsung di luar. Contohnya berikut
'''
class Myclass:
    def __init__(self):
        self._private_var = 42 #Variabel non publik dengan awalan satu garis bawah
        self._secret_list = [1, 2, 3] #Variabel non publik lainnya

    def _private_method (self):
        print("Ini adalah method non publik")
    
    def publik_method(self):
        print("Ini adalah method publik")
        self._private_method() # Method publik dapat memanggil method non publik


'''
Pada contoh di atas, method '_private_method' merupakan jenis fungsi yang tidak diakses secara langsung. Anda bisa melihat pada method 
'public_method', tempat kita menggunakan method private di sana. Selain itu, variabel seperti '_private_var' atau '_secret_list' merupakan 
variabel non_publik yang tidak digunakan secara langsung ketika kelas dipanggil.

Method/Variabel publik dipersiapkan untuk pihak eksternal menggunakan kelas Anda. Anda juga otomatis berkomitmen untuk menghindari adanya 
incompatible backward changes atau suatu kode yang tidak dapat berjalan kembali setelah adanya perubahan. 

Sebaliknya, method/variabel dengan atribut non-publik hanya digunakan oleh Anda sebagai developer. Itu juga tidak memberikan garansi kepada 
siapa pun bahwa Anda takkan mengubah atau menghapusnya. Di sini kita tidak menggunakan atribut private karena dalam Python tidak ada atribut yang 
benar-benar private.

Kategori lain dari atribut adalah "subclass API", umumnya disebut protected pada bahasa lain. Sebuah kelas dapat didesain untuk diwariskan 
(inherited-from), misalnya untuk memodifikasi atau menjadi ekstensi dari perilaku (behavior) kelas. Dalam mendesain kelas-kelas sejenis, 
pastikan untuk membuat keputusan eksplisit, variabel/method yang memiliki atribut publik, bagian dari subclass API, dan yang hanya anda gunakan 
secara internal.

Saat mendeklarasikan variabel/method tersebut, ikuti panduan Pythonic berikut.

Atribut publik tidak menggunakan awalan garis bawah.
Jika nama sebuah method/variabel publik sama dengan reserved keyword, tambahkan akhiran garis bawah. Hindari menyingkat atau mengurangi huruf.
Pada data publik yang bersifat simpel, hindari nama yang terlalu panjang. Cukup dengan nama atribut sependek mungkin. Ingatlah bahwa pada masa 
depan Anda akan mungkin mengembangkan skema atau data ini sehingga nama sependek apa pun mungkin akan menguntungkan Anda.
Jika Anda berniat untuk mewariskan atau membuat subclass dari kelas dan menginginkan sebuah variabel hanya digunakan di kelas utama saja, 
tambahkan awalan dua garis bawah. Ini akan memudahkan Anda karena Python mengenalinya sebagai konvensi kelas, untuk menghindari kemungkinan 
kesamaan nama atau implementasi.
Sekali lagi, semua materi style guide kali ini mengacu pada PEP8 yang dapat Anda baca lebih lanjut dalam link berikut.
link: https://peps.python.org/pep-0008/
'''
