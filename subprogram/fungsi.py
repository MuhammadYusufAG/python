# docstring
'''
Terakhir, untuk membuat fungsi lebih mudah dipahami oleh programmer lain, kita bisa membuat dokumentasi berupa docstring. 
Docstring adalah akronim dari documentation string, bertujuan untuk membuat dokumentasi terhadap fungsi yang dibuat. Umumnya, 
dokumentasi yang dijelaskan berupa argumen, return, deskripsi fungsi, dan sebagainya.

Mari lihat contoh penerapannya di bawah ini.
'''

def mencari_luas_persegi_panjang(panjang,lebar):
    """
    Fungsi ini digunakan untuk menghitung luas persegi panjang.

    Args:
        panjang (int): Panjang persegi panjang.
        lebar (int): Lebar persegi panjang.

    Returns:
        int: Luas persegi panjang hasil perhitungan.
    """

    luas_persegi_panjang = panjang*lebar
    return luas_persegi_panjang

persegi_panjang_pertama = mencari_luas_persegi_panjang(5,10)
print(persegi_panjang_pertama)

'''
Pada kode di atas, kita mendefinisikan docstring dengan memberikan blok komentar dengan tiga double quote (""") tepat di 
bawah "def" keyword. Hal ini untuk menegaskan sebelum kode dibaca, kita harus memahami dokumentasi di bawahnya terlebih dahulu.

Dokumentasi di atas memiliki tiga elemen, yakni berikut.

Deskripsi: Teks yang menjelaskan tujuan dari fungsi yang dibuat. Pada contoh di atas, kita mendefinisikan teks "Fungsi ini 
digunakan untuk menghitung luas persegi panjang" yang artinya fungsi ini ditujukan untuk menghitung luas persegi panjang. 
Argumen: bagian yang menjelaskan argumen yang diterima oleh fungsi. Dalam contoh di atas, argumen yang diterima adalah panjang 
dan lebar dengan keduanya termasuk bilangan bulat atau bertipe data integer. 
Return: Bagian ini menjelaskan nilai yang akan dikembalikan oleh fungsi. Dalam contoh di atas, fungsi akan mengembalikan nilai 
luas persegi panjang hasil perhitungan yang termasuk bilangan bulat atau bertipe data integer.
'''

# argument dan parameter
'''
Ingat bahwa argumen dan parameter adalah hal yang berbeda, sering kali programmer tertukar akan kedua istilah tersebut. 
Sederhananya, Anda bisa bayangkan parameter seperti black box yang akan menampung nilai dan nilai tersebut adalah argumen.

Contohnya, saat Anda membuat fungsi berikut.
'''
# def fungsi_saya(a,b,c):
    # function body
'''
Ketika Anda membuat fungsi di atas, a, b, c merupakan parameter. Namun pada saat Anda memanggilnya, 
nilai 1, b=50,  c='Dicoding' menjadi argumen.
'''
# fungsi_saya(1,b=50,c='dicoding')


# argument
'''
Argumen adalah nilai yang akan diberikan kepada fungsi. Setidaknya ada dua jenis argumen yang dikenal dalam Python.
'''

#1.Keyword Argument
'''
Keyword Argument adalah jenis argumen yang disertai dengan nama parameter (identifier) dan secara eksplisit disebutkan. 
Ketika nama parameter dalam sebuah argumen secara langsung disebutkan, artinya kita menggunakan keyword argument.
'''
def mencari_luas_persegi_panjang(panjang,lebar):
    luas_persegi_panjang = panjang*lebar
    return luas_persegi_panjang

persegi_panjang_pertama = mencari_luas_persegi_panjang(panjang=5, lebar=10)

print(persegi_panjang_pertama)

'''
Ketika kita memanggil fungsi "mencari_luas_persegi_panjang" dengan menuliskan nama parameter diikuti tanda sama dengan (=) 
dan nilai yang ingin diberikan, itu disebut keyword argument.

Pada contoh di atas, keyword argument "panjang=5" dan "lebar=10" diberikan saat pemanggilan fungsi.

Kelebihan dari jenis argumen ini adalah walaupun kita harus menuliskan lebih banyak kata, urutan parameter fungsi tidak perlu 
dipikirkan.
'''

def mencari_luas_persegi_panjang(panjang,lebar):
    luas_persegi_panjang = panjang*lebar
    return luas_persegi_panjang

persegi_panjang_pertama = mencari_luas_persegi_panjang(lebar=10, panjang=5)

print(persegi_panjang_pertama)

'''
Contohnya pada kode di atas, kita menuliskan "lebar=10" terlebih dahulu dan diikuti oleh "panjang=5". Padahal, dalam 
fungsi yang kita buat urutan parameternya adalah panjang dan lebar.
'''


# 2.Positional Argument
'''
Kebalikan dari keyword adalah positional, artinya Anda tidak menyebutkan nama parameter (identifier) secara eksplisit. 
Ketika memanggil fungsi, Anda hanya harus memasukkan nilai yang ingin diberikan. Namun, Anda harus mengikuti urutan dari 
parameter fungsi tersebut.
'''

def mencari_luas_persegi_panjang(panjang,lebar):
    luas_persegi_panjang = panjang*lebar
    return luas_persegi_panjang

persegi_panjang_pertama = mencari_luas_persegi_panjang(5,10)

print(persegi_panjang_pertama)

'''
Pada contoh di atas, kita memanggil fungsi "mencari_luas_persegi_panjang" dengan argumen 5 dan 10. Masing-masing nilai
tersebut merepresentasikan parameter panjang dan lebar. Jika kita menukar urutan nilai tersebut yang awalnya "5, 10" 
menjadi "10, 5", program akan menganggap panjangnya 10 dan lebarnya 5.
'''

# Fungsi anonim (Lambda Expression)
# documentasi = https://www.w3schools.com/python/python_lambda.asp

'''
Terakhir, mari kita pelajari cara membuat fungsi tanpa mendeklarasikan def. Cara ini dikenal dengan ekspresi lambda yang 
digunakan untuk membuat fungsi tanpa perlu menyebutkan def ketika membuatnya. Anda bisa mengasumsikan fungsi anonim ini sebagai 
fungsi one-liner. Secara umum, struktur fungsi anonim sebagai berikut.
'''

# func = lambda args: ret_val
''' Kita akan menggunakan ekspresi lambda untuk melakukan operasi layaknya def didefinisikan. Keterkaitan antara def dan lambda 
dapat dilihat pada gambar bergerak (GIF) berikut.
'''

# def func (args):
#     return ret_val

# func = lambda args: ret_val

'''
Nama fungsi (func) setara dengan nama variabel yang digunakan untuk menyimpan ekspresi lambda, args adalah argumen yang dibutuhkan 
untuk dioperasikan, dan ret_val merupakan nilai yang kita kembalikan (return).

Perhatikan contoh di bawah ini. Mari kita ubah contoh fungsi mencari luas persegi panjang menjadi fungsi anonim.
'''

mencari_luas_persegi_panjang = lambda panjang, lebar: panjang*lebar
print(mencari_luas_persegi_panjang(5,10))


'''
Pada contoh kode di atas, kita membuat fungsi dengan nama "mencari_luas_persegi_panjang" yang menjadi nama variabel. Argumen yang 
digunakan adalah panjang dan lebar, kita mendefinisikan ini tepat setelah pernyataan lambda. Lalu, kita menambahkan isi fungsi, 
yaitu panjang*lebar dan hasilnya merupakan return value. Terakhir, pemanggilan pada fungsi anonim sama seperti biasanya.

Isi fungsi dalam lambda dapat Anda ganti menjadi sebuah nilai, alih-alih variabel. Hal ini karena umumnya bertujuan untuk melakukan 
operasi sederhana dan perlu melibatkan fungsi yang tidak terlalu kompleks hingga perlu menggunakan def. 

Silakan ganti panjang*lebar dengan nilai integer yang Anda mau untuk mengetahui maksud dari pernyataan di atas. 

Sebuah fungsi lambda dapat menerima argumen dalam jumlah berapa pun, tetapi hanya mengembalikan satu nilai ekspresi. Dalam contoh 
di atas, Anda bisa menambahkan argumen selain panjang dan lebar, tetapi hanya bisa menggunakan satu operasi, yaitu panjang*lebar.

Variabel Global dan Lokal
Dalam Python, ada konsep "scope" yang mengatur jangkauan variabel dan fungsi dalam suatu program. Konsep ini lebih dikenal 
sebagai scope variable yang mengacu pada wilayah di dalam program tempat variabel dapat diakses dan digunakan.

Ada dua jenis scope yang umum dijumpai, khususnya ketika Anda membuat fungsi dan program yang lebih kompleks.
'''

# 1.variable global
'''
uatu variabel yang didefinisikan di luar fungsi atau blok kode apa pun dan dapat diakses dari seluruh bagian program. Mari lihat 
penerapannya di bawah ini, asumsikan bahwa kita membuat sebuah fungsi penjumlahan dengan satu nilai yang sudah ditetapkan, yaitu 10.
'''
a = 10 #global

def add(b): 
    result = a+b
    return result

bilanganPertama = add(20)
print(bilanganPertama)
'''
Pada contoh di atas, kita mendeklarasikan variabel a dan menginisialisasikannya dengan nilai 10. Pada tahap ini, kita menetapkan bahwa 
variabel a merupakan variabel global dan dapat digunakan pada seluruh bagian program yang kita buat.

Selanjutnya, fungsi penjumlahan didefinisikan dan akan menjumlahkan variabel a yang telah dibuat dengan bilangan yang dapat kita 
tentukan. Pada contoh di atas, kita menambahkan variabel a bernilai 10 dengan nilai 20 dan hasilnya adalah 30.
'''

# 2.variable lokal
'''
Variabel ini didefinisikan dalam suatu fungsi atau blok kode tertentu. Jenis ini hanya dapat diakses dari dalam fungsi atau blok 
kode tempat variabel tersebut didefinisikan. Mari lihat contohnya di bawah ini, asumsikan bahwa kita membuat fungsi untuk 
penjumlahan yang menerima dua bilangan untuk dijumlahkan. Namun, kali ini setiap dua bilangan tersebut dioperasikan akan dikurangi 
oleh lokal variabel bernilai 5.
'''
def add(a, b):
    lokal_var = 5 #local var
    result = a+b-lokal_var
    return result

bilanganPertama = add(10,20)
print(bilanganPertama)

'''
Pada contoh di atas, kita mendefinisikan fungsi penjumlahan bernama "add" dengan dua parameter, yakni a dan b. Dalam fungsi tersebut,
kita mengoperasikan penjumlahan antara a dan b lalu dikurangi variabel lokal bernama "lokal_var" dengan nilai 5.

Ingat bahwa variabel lokal hanya dapat diakses dari dalam fungsi atau blok kode tempat variabel tersebut didefinisikan. Silakan coba 
cetak ke layar "lokal_var" menggunakan fungsi print(). Salin dan tempel kode berikut ke dalam program di atas tepat setelah perintah 
print(bilanganPertama).
'''
# print(lokal_var)
'''
Apa output yang dikeluarkan? Program akan menampilkan pesan error bahwa "lokal_var is not defined". Hal ini karena variabel tersebut 
kita definisikan dalam fungsi dan hanya dapat digunakan dalam fungsi tersebut.
'''

