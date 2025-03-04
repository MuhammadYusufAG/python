# import unittest

# class TestStringMethod(unittest.TestCase):
#     # Ini adalah test case pertama (1)
#     def test_strip(self):
#         self.assertEqual('www.dicoding.com'.strip('c.mow'), 'dicoding')

#     # Test case kedua (2)
#     def test_isalnum(self):
#         self.assertTrue('c0d1ng'.isalnum())
#         # self.assertTrue('c0d!ng'.isalnum())
#         self.assertFalse('c0d!ng'.isalnum())

    
#     # Test case ketiga (3)
#     def text_index(self):
#         s = 'dicoding'
#         self.assertEqual(s.index('coding'), 2)
#         # cek s.index gagal ketika tidak ditemukan
#         with self.assertRaises(ValueError):
#             s.index('decode')

# if __name__ == '__main__':
#      # Test Runner
#     unittest.main()



'''
Mari kita bahas satu per satu dari kode di atas.

Kelas TestStringMethods adalah sebuah kelas yang merupakan turunan (subclass) dari class unittest.TestCase sehingga proses tes dapat dilangsungkan 
tanpa banyak implementasi lain.

Ada tiga metode pada class tersebut yang semua namanya diawali dengan kata test. Hal ini merupakan konvensi (aturan) yang wajib diikuti untuk 
menginformasikan ke test runner bahwa sejumlah metode tersebut merepresentasikan tes yang akan dioperasikan.

Pada setiap metode, pengujian dilakukan dengan pemanggilan assert. Pada metode test_strip pengecekan kesamaan menggunakan assertEqual dilakukan 
untuk memastikan bahwa 'www.dicoding.com'.strip('c.mow') sama dengan ‘dicoding’.

Pada metode test_isalnum pengecekan bahwa fungsi bernilai benar (True) dilakukan dengan assertTrue untuk memastikan jika 'c0d1ng'.isalnum() 
bernilai benar, yakni ‘cOd1ng’ adalah betul bertipe alfanumerik. Kemudian juga ada pengecekan bahwa fungsi bernilai salah (False) dengan 
assertFalse untuk memastikan jika 'c0d!ng'.isalnum() betul bernilai salah karena ada karakter yang bukan alfanumerik yaitu ‘!’.

Pada metode test_index pengecekan kesamaan dilakukan seperti sebelumnya dengan menggunakan assertEqual bahwa pencarian substring coding 
menempati index sama dengan 2. Kemudian juga ada pengecekan bahwa ValueError akan dibangkitkan dengan menggunakan assertRaises(ValueError), 
jika pencarian index tidak berhasil ditemukan pada string yang sudah ditentukan.

Pada bagian terakhir kode, ada pemanggilan unittest.main() untuk mulai menjalankan test.

Selanjutnya, kita akan membahas hasil keluarannya. Tampak pada keluaran bahwa ada tiga tanda titik (...) yang menyatakan bahwa ketiga fungsi yang 
dites berhasil melewati tes. Dirangkum juga waktu pemrosesan dari total tiga tes tersebut yang berlangsung selama 0.00 detik serta di baris paling 
akhir adalah rangkuman bahwa semua test berlangsung sukses (OK).

Anda bisa mencoba melihat keluaran lain dengan membuat gagal salah satu test. Misalnya pada metode test_isalnum, keduanya akan diubah menggunakan 
assertTrue sehingga salah satu fungsi akan gagal. Kodenya bisa Anda lihat di bawah.
'''

# def test_isalnum(self):
#        self.assertTrue('c0d1ng'.isalnum())  # ini akan berhasil
#        self.assertTrue('c0d!ng'.isalnum())  # ini akan gagal

'''
Berikut penjelasannya.

Layaknya yang sudah Anda duga bahwa akan ada pengujian yang gagal sehingga tertulis .F. yang menggambarkan bahwa pengujian metode kedua gagal 
(FAIL).

Berikutnya dijelaskan bahwa kegagalan ada dalam metode test_isalnum, yaitu sebuah metode dari class __main__.TestStringMethods.
Lebih jauh, diinformasikan bahwa test_isalnum yang gagal berada pada baris ke-10 pada kode Anda, yakni pada pengecekan 
self.assertTrue('c0d!ng'.isalnum()) yang memang tadi kita ubah dari assertFalse. Sistem pengujian juga melaporkan bahwa pembandingannya tidak 
sesuai, yakni False tidak bernilai benar seperti yang diharapkan dengan adanya pengujian assertTrue.

Rekap totalnya ada tiga tes yang dilakukan dalam 0.01 detik. Kemudian secara umum tes menghasilkan satu buah kegagalan (failure).

Cukup mudah dimengerti, bukan? Kita dapat melihat sendiri bahwa pengujian hasilnya gagal. Namun, kali ini gagalnya memang sesuai dengan ekspektasi
kita.

Sekarang kita coba pengujian dengan contoh yang lebih nyata, misalnya kita memiliki class User dan kita akan menguji aktif atau tidaknya user 
dengan melihat bahwa dia terkoneksi ke basis data (db) atau tidak.

Untuk menyederhanakan kodenya dan lebih fokus pada pengujiannya, tulis simulasinya dalam satu file kode sebagai berikut.
'''

# Terkoneksi ke database
import unittest

def koneksi_ke_db():
    print("[terhubung ke db]")

def putus_koneksi_db(db):
    print("[tidak terhubung ke db {}]".format(db))

class User:
    username = ""
    aktif = False

    def __init__(self, db, username):
        self.username = username

    def set_aktif(self):
        self.aktif = True

class TestUser(unittest.TestCase):

    #Test Fixture Tambahan dari penjelasan dibawah
    def setUp(self):
        self.db = koneksi_ke_db()
        self.dicoding = User(self.db, 'dicoding')

    def tearDown(self):
        putus_koneksi_db(self.db)


    #Test Case 1
    def test_user_defaut_not_Active(self):
        self.assertFalse(self.dicoding.aktif)
        # db = koneksi_ke_db()
        # dicoding = User(db, 'dicoding')
        # self.assertFalse(dicoding.aktif)
        # putus_koneksi_db(db)

    #Test Case 2
    def test_user_is_active(self):
        self.dicoding.set_aktif()
        # db = koneksi_ke_db()
        # dicoding = User(db, 'dicoding')
        # dicoding.set_aktif()
        # self.assertTrue(dicoding.aktif)
        # putus_koneksi_db(db)

if __name__ == '__main__':
    #test runner
    unittest.main()


'''
Sama seperti sebelumnya, kita akan membuat sebuah class TestUser yang merupakan turunan dari class unittest.TestCase, kemudian menulis dua metode 
untuk pengujian kali ini.

Jika Anda perhatikan kembali semua kode di atas, kita melakukan beberapa tindakan yang berulang ketika kita menjalankan fungsi koneksi ke basis 
data dan membuat User dicoding setiap kali proses tes. Hal ini karena setiap tes itu dioperasikan secara terpisah sehingga perlu melakukan 
tindakan yang disebutkan secara berulang. Tindakan ini juga dianggap bukan praktik yang baik karena memakan lebih banyak memori apalagi jika 
program yang kita uji berukuran besar.

Lantas, kita bisa memperbaikinya dengan menerapkan konsep test fixture. Konsep ini merepresentasikan persiapan yang dibutuhkan untuk melakukan '
satu pengujian atau lebih serta proses pembersihannya (cleanup). 

Kita akan menggunakan metode bawaan dari class TestCase, yakni metode setUp() dan tearDown().

Metode setUp(), sesuai namanya, bertujuan untuk mempersiapkan pengujian. Metode ini akan dipanggil untuk menyiapkan tes sehingga pemanggilannya 
akan dilakukan tiap sebelum metode tes dilaksanakan.

Metode tearDown() akan dipanggil setiap metode tes selesai dilaksanakan dan bertindak untuk membersihkan, meskipun terjadi kesalahan (exception) 
pada proses tes.

Kode sebelumnya akan kita ubah dengan implementasi kedua metode setUp() dan tearDown(). Kita cukup melakukan perubahan pada class TestUser saja 
seperti di bawah.
'''


# class TestUser(unittest.TestCase):
#     # Test Fixture
#     def setUp(self):
#         self.db = koneksi_ke_db()
#         self.dicoding = User(self.db, "dicoding")
 
#     def tearDown(self):
#         putus_koneksi_db(self.db)
 

'''
Terlihat bahwa setiap kali melakukan pengujian, metode setUp() dipanggil. Begitu juga setelah selesai pengujian, metode tearDown() dipanggil.

Dengan kemampuan pengujian ini, aplikasi yang Anda buat jadi lebih teruji atau biasa disebut dengan istilah lebih tahan banting (robust).
'''