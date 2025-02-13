# ilustarasi beli dipasar

tersedia = 'daging ayam'
if tersedia == 'daging ayam':
    print('membeli dan memasak ayam')
else:
    print('membeli dan memasak tempe')


# IF

score = 100
if score == 100:
    print('nilai anda sempurna')

#=====================================
x = ""

if x:
    print("Ini True")
    
'''
Pada baris pertama kode program di atas, variabel "x" diinisialisasikan dengan string kosong "". 
Kemudian if statement mengevaluasi variabel "x" dan menghasilkan nilai salah (False). Hal ini terjadi karena variabel "x" berisi string kosong 
dan Python mengevaluasinya sebagai False. Sebab hasil kondisinya adalah False, blok kode dalam if tidak dijalankan.

Beberapa nilai yang dianggap sebagai false oleh Python sebagai berikut.

Nilai yang sudah didefinisikan bernilai salah: None dan False.
Angka nol dari semua tipe numerik: 0, 0.0, 0j, Decimal(0), Fraction(0,1).
Urutan (sequence) dan koleksi (collection) yang kosong: "", (), {}, set(), range(0).
'''
# one line
score = 100

if score == 100: print("Nilai Anda sempurna!")#oneline



# ELSE
berat_badan = 40
if berat_badan > 70:
    print('anda harus cutting')
else:
    print('anda harus bulking\n')


# ELIF

nilai = 75
if nilai >= 80:
    print("Selamat! Anda mendapat nilai A")
    print("Pertahankan!")
elif nilai >= 70:
    print("Selamat! Anda mendapat nilai B")
    print("Teruslah belajar!")
elif nilai>=60:
   print("Hmm.. Anda mendapat nilai C")
   print("Ayo semangat!")
else:
   print("Waduh, Anda mendapat nilai D")
   print("Yuk belajar lebih giat lagi!")


# ELIF USE AND
nilai = 81
perilaku = 'tidak baik'

if nilai>=80 and perilaku == 'baik':
   print("Selamat! Anda mendapat nilai A dan telah berkelakuan baik")
   print("Pertahankan!")
elif nilai>=80 and perilaku != 'baik':
   print("Kamu mendapatkan nilai A, tetapi perilaku Anda kurang baik")
   print("Perbaiki lagi ya!")
else:
   print("Yuk belajar lebih giat lagi!")



# ternary Operator
'''
Ternary operators dibangun dengan menempatkan "blok kode jika benar" pada posisi awal, lalu diikuti oleh "if statement" serta "kondisi"-nya. 
Kemudian "else statement" ditempatkan di akhir beserta dengan "blok kode jika salah".
'''

lulus = False
print('selamat') if lulus else print('ngulang')
# transformasi dari kode diatas
lulus = True
if lulus:
    print("Selamat") 
else:
    print("Perbaiki")


# USE TUPLE
lulus = True
kelulusan = ("Perbaiki, Anda belum lulus.","Selamat, Anda lulus!")[lulus]
print(kelulusan)
# transformasi dar kode diatas
lulus = True
if lulus:
    print("Selamat, Anda lulus!") 
else:
    print("Perbaiki, Anda belum lulus.")
