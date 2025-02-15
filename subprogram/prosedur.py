# Fundamental Prosedur
'''
Dalam KBBI, kata prosedur memiliki makna sebagai tahap kegiatan untuk menyelesaikan suatu aktivitas. Hal ini sama seperti prosedur 
sebagai subprogram yang merupakan pengelompokan instruksi-instruksi yang sering dipakai dalam program. 
kbbi = https://kbbi.kemdikbud.go.id/entri/prosedur

Berbeda dengan fungsi, prosedur tidak mengharuskan adanya parameter input atau output dan dapat dipandang sebagai fungsi yang tidak 
menghasilkan nilai. Dalam Python, prosedur didefinisikan dengan return tanpa ekspresi atau nilai yang dihasilkan di akhir fungsi.
'''

# contoh code
'''

def nama_prosedur (param1,param2, ...):
     # blok kode prosedur
     #tindakan atau perintah yang ingin dilakukan 
     #...

#memanggil prosedur
nama_prosedur (nilai_param1,nilai_param2, ...)

'''

'''
Secara konsep, gambar di atas merupakan kerangka dasar prosedur pada Python. Sekilas memang sangat mirip dengan fungsi, 
hanya saja kita tidak mendefinisikan return dan bahkan return value. 

Berikut adalah contoh prosedur dalam Python.
'''
def greeting(name):
    print("Halo " + name + ", Selamat Datang!")


'''
Pada contoh di atas, kita membuat fungsi bernama "greeting()" untuk menyapa nama siapa pun yang dikirimkan. Perhatikan bahwa kita 
tidak mendefinisikan return dan membuat return value. Konsep ini disebut sebagai prosedur, yakni fungsi Python yang kita buat tidak 
mengeluarkan nilai dari fungsi tersebut.

Kita sebenarnya bisa menambahkan pernyataan return, tetapi kita tidak menyertakan return value setelahnya.
'''

def greeting(name):
    print("Halo " + name + ", Selamat Datang!")
    return

'''
Pada kode di atas, kita membuat prosedur dengan kode yang sama seperti sebelumnya, hanya saja kita mendefinisikan return dan 
tidak memberikan return value setelahnya.
'''


# Mendefinisikan dan Memanggil Prosedur
'''
Untuk memanggil prosedur, caranya serupa seperti Anda memanggil fungsi. Cukup mendefinisikan satu baris instruksi, 
seperti "greeting()". Untuk pemberian argumen dan parameter pada prosedur, kita dapat memakai cara yang sama seperti pada 
fungsi yang telah dijelaskan sebelumnya. 
'''

def greeting(name):
    print("Halo " + name + ", Selamat Datang!")

greeting("Dicoding Indonesia")

'''
Pada contoh di atas, kita mendefinisikan prosedur tanpa adanya return statement. Perhatikan bahwa program tetap menampilkan 
hasil fungsi karena kita langsung menggunakan fungsi "print()" dalam prosedur yang telah dibuat. Jadi, walaupun tidak ada return atau return value, kita tetap mendapatkan output-nya.

Kita juga bisa membuat prosedur yang tidak memiliki parameter input. Ketika kita memanggil prosedur tersebut, program akan langsung 
menjalankannya. Mari kita ubah kode di atas jika tidak memiliki parameter.
'''

def greeting():
    print("Halo Selamat Datang!")

greeting()

'''
Pada contoh di atas, prosedur “greeting” tidak menggunakan parameter sama sekali. Namun, sebab body prosedur tersebut memiliki 
perintah “print()” untuk menampilkan pesan “Halo Selamat Datang!” ke layar, prosedur tersebut akan menampilkan teks ketika kita 
memanggilnya dengan perintah “greeting()”. 
'''