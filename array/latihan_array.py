'''
Latihan Array
Pada materi sebelumnya, kita telah memahami bahwa array adalah salah satu jenis dari struktur data linear. Array mengumpulkan elemen-elemen berdasarkan indeks secara berurutan atau linear.

Pemrosesan array merujuk pada operasi-operasi yang dilakukan pada elemen-elemen suatu array. Salah satu operasinya adalah pemrosesan sekuensial yang merupakan sebuah pemrosesan setiap elemen array, dimulai dari elemen pada indeks terkecil hingga indeks terbesar.

Dari sekian banyaknya contoh pemrosesan sekuensial pada array, mari kita pelajari salah satunya, yakni mencari nilai terbesar dalam array.

Mari kita asumsikan memiliki sebuah array seperti pada gambar berikut.
'''

# posisi index [0, 1, 2, 3, 4]
# posisi elemen[1, 7, 2, 89, 3]

'''
Kita memiliki array yang beranggotakan nilai integer dengan elemen indeks ke-0 adalah 1, elemen indeks ke-1 adalah 7, elemen indeks ke-2 adalah 2, elemen indeks ke-3 adalah 89, elemen indeks ke-4 adalah 3.

Kita akan mencari nilai atau elemen terbesar dari array tersebut menggunakan algoritma two pointers. Algoritma adalah serangkaian langkah-langkah terstruktur yang dirancang untuk menyelesaikan suatu masalah atau mencapai suatu tujuan. Dalam hal ini, tujuan yang ingin dicapai adalah mencari nilai terbesar pada array.

Algoritma two pointers adalah algoritma yang memiliki pendekatan dengan cara memanipulasi atau memproses urutan data menggunakan dua penanda atau dua pointer secara bersamaan. Kedua pointer tersebut bisa kita sebut sebagai "left" dan "right".
'''

'''
Untuk memahami algoritma ini, perhatikan beberapa informasi berikut.

Pointer "left" akan berada pada indeks pertama dan menyatakan bahwa pointer "left" selalu menunjukkan nilai terbesar dalam array.
Pointer "right" akan selalu berada pada elemen selanjutnya dan membandingkannya dengan elemen pointer "left".
Sekarang, mari kita mulai proses pencarian nilai terbesar. Simak gambar bergerak (GIF) berikut untuk ilustrasinya. 
'''

'''
Mari kita bedah satu per satu setiap langkah-langkahnya, simak penjelasan berikut.

Pertama, kita memulai dengan dua pointer: pointer "left" pada elemen pertama (1) dan pointer "right" pada elemen berikutnya (7). Kita membandingkan nilai 7 dengan nilai 1. Sebab 7 lebih besar dari 1, kita mengganti nilai pointer "left" dari 1 menjadi 7.
Sekarang, pointer "left" berada pada elemen 7 dan pointer "right" berada pada elemen berikutnya (2). Kita membandingkan nilai 7 dengan 2. Sebab 2 tidak lebih besar dari 7, pointer "left" tetap pada nilai 7.
Pointer "right" berpindah ke elemen berikutnya (89), sementara pointer "left" tetap pada nilai 7. Kita membandingkan nilai 89 dengan 7. Sebab 89 lebih besar dari 7, pointer "left" berpindah ke nilai 89.
Sekarang, pointer "left" berada pada elemen 89 dan pointer "right" berada pada elemen berikutnya (3). Kita membandingkan nilai 89 dengan 3. Sebab 3 tidak lebih besar dari 89, pointer "left" tetap pada nilai 89.
Proses berakhir, nilai pada pointer "left" ditetapkan sebagai nilai terbesar dalam array.
Dengan demikian, kita menggunakan dua pointer untuk membandingkan dan mengganti nilai pointer "left" jika ada nilai yang lebih besar saat melintasi array. Pada akhirnya, nilai pada pointer "left" adalah nilai terbesar dalam array.

Sekarang Anda sudah paham secara teoretis cara algoritma two pointers bekerja untuk memproses array dalam mencari nilai terbesar. Selanjutnya, mari kita ubah penjelasan tersebut ke dalam program Python. 
'''

var_arr = [1, 7, 2, 89, 3]
left_pointer = var_arr[0]

for i in range(1,len(var_arr)):
    right_pointer = var_arr[i]
    if right_pointer > left_pointer:
        left_pointer = right_pointer
print(left_pointer)


'''
Pada program di atas, hal pertama yang dilakukan adalah menginisialisasi variabel "var_arr" dengan array "[1, 7, 2, 89, 3]". Kedua, kita menginisialisasi variabel "left_pointer" dengan nilainya adalah indeks pertama variabel "var_arr" (var_arr[0]).  

Kita menggunakan perulangan "for" untuk mengakses semua indeks dari indeks ke-1 hingga panjang array. Untuk mengetahui panjang array, kita menggunakan fungsi "len()", yang  bertujuan menghitung panjang atau banyaknya elemen dari list, set, dan string. 

Dalam perulangan "for" tersebut kita mendeklarasikan variabel "right_pointer" yang akan terus berpindah dari indeks ke-1 hingga indeks terakhir (akhir panjang array). Setelah memiliki "left_pointer" dan "right_pointer", kita membandingkan nilai keduanya. Jika "right_pointer" lebih besar dari "left_pointer", kita akan memperbarui nilai "left_pointer" dengan nilai "right_pointer".

Proses tersebut terjadi secara berulang sampai nilai yang tersimpan dalam "left_pointer" dijadikan sebagai nilai maksimal dari array. Lalu, kita mencetak nilai tersebut dengan perintah "print(left_pointer)".
'''