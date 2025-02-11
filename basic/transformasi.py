# upper()
kata = 'dicoding'
kata = kata.upper()
print(kata)

# lower()
kata = 'DICODING'
kata = kata.lower()
print(kata)


# AWALAN DAN AKHIRAN

# rstrip() untuk menghapus whitespace pada sebelah kanan atau akhir string
print("Dicoding          ".rstrip())

# lstrip() untuk menghapus whitespace pada sebelah kiri atau awal string. 
print("           Dicoding".lstrip())

# strip() untuk menghapus whitespace pada bagian awal dan akhir string.
print("         Dicoding          ".strip())

# menghapus selain whitespace
kata = 'CodeCodeDicodingCodeCode'
print(kata.strip('Code'))

# startswith() untuk menemukan suatu kata pada awal string. Metode ini mengembalikan nilai True.
print('Dicoding Indonesia'.startswith('Dicoding'))

# endswith() untuk menemukan suatu kata pada akhir string. Metode ini juga mengembalikan nilai True jika menemukannya, sedangkan jika tidak menemukan kata yang diinginkan, nilai False dikembalikan.
print('Dicoding Indonesia'.endswith('Dicoding'))#kalau yang dicari Indonesia akan true


#MEMISAHKAN DAN MENGGABUNGKAN STRING

# join() 
print(' '.join(['Dicoding','Indonesia','!']))

# menambahkan delimiter lain
print('123'.join(['Dicoding','Indonesia']))

# split() untuk memisahkan kata/substring berdasarkan delimiter.
print('Dicoding Indonesia !'.split())
# multiline split
print('''Halo,
aku ikan,
aku suka sekali menyelam
aku tinggal di perairan.
Badanku licin dan renangku cepat.
Senang berkenalan denganmu.'''.split('\n'))


# MENGANTI ELEMENT STRING
string = 'Ayo belajar Coding di Dicoding'
print(string.replace("Coding", "Pemrograman"))

# PENGECEKAN STRING

# isupper  akan mengembalikan nilai True jika semua huruf dalam string adalah huruf kapital (uppercase).
kata = 'DICODING'
print(kata.isupper())

# islower() akan mengembalikan nilai True jika semua huruf dalam string adalah huruf kecil (lowercase).
kata = 'dicoding'
print(kata.islower())

# isalpha() untuk mengembalikan nilai True jika semua karakter dalam string adalah huruf alfabet. Jika ada satu huruf lain yang bukan alfabet, seperti angka, nilai False akan dikembalikan.
kata = 'dicoding123'#false karna ada 123
print(kata.isalpha())

# isalnum mengembalikan nilai True jika karakter dalam string adalah alfanumerik, yaitu hanya huruf atau hanya angka atau berisi keduanya. Jika tidak, nilai False akan dikembalikan.
kata = 'dicoding123!'#false karna ada ! unique karakter
print(kata.isalnum())

# isdecimal() akan mengembalikan nilai True jika karakter dalam string berisi hanya angka/numerik. Jika tidak, nilai False akan dikembalikan.
print('123'.isdecimal())

# isspace() akan mengembalikan nilai True jika string hanya berisi whitespace, seperti spasi, tab, newline, atau karakter whitespace lainnya.
print('   '.isspace())

# istitle mengembalikan nilai True jika string berisi huruf kapital pada setiap kata pertamanya. Jika tidak, nilai False dikembalikan.
print('Dicoding Indonesia'.istitle())#true karna D huruf besar

#zfill() untuk menambahkan nilai nol (0) di depan sebuah string dengan panjang tertentu. Tujuan dari metode ini adalah membantu untuk memastikan bahwa sebuah angka atau nilai memiliki panjang tetap, terutama ketika ingin menyimpan nilai dalam format yang konsisten.
print('123'.zfill(5)) ##00123
teks = 'Code'
tambah_number = teks.zfill(5)
print(tambah_number)#0Code

# rjust()  berguna untuk merapikan pencetakan teks. Dengan metode rjust() ini, Anda dapat membuat teks menjadi rata kanan sehingga tampilannya lebih rapi.
print('Dicoding'.rjust(20))
print('Dicoding'.rjust(20, '!'))

# ijust() untuk membuat teks menjadi rata kiri.
print('Dicoding'.ljust(20,'!'))

# center() menjadikan teks rata tengah. Metode ini akan menambahkan whitespace di sebelah kiri dan kanan secara default. Anda juga bisa mengganti whitespace tersebut dengan karakter lain.
print('Dicoding'.center(10,'-'))


# STRING LITERALS
# st1 = 'Jum'at' invalid
# st1 = "Jum'at"
# st1 = 'Jum\'at'
print("Halo!\nKapan terakhir kali kita bertemu?\nKita bertemu hari Jum\'at yang lalu.")


# RAW STRING
'''raw strings. Umumnya, ia digunakan untuk regex atau beberapa implementasi lain yang sangat bergantung pada keberadaan backslash. Untuk mengimplementasikan 
raw strings, sisipkan huruf r sebelum pembuka string.'''

print(r'Dicoding\tIndonesia')