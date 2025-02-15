# Pemrosesan Sekuensial pada Array
'''
Pemrosesan array merujuk kepada operasi-operasi yang dilakukan pada elemen-elemen suatu array. Operasi ini melibatkan manipulasi hingga pengolahan elemen yang ada pada array. 

Adapun pemrosesan sekuensial adalah sebuah pemrosesan setiap elemen array yang dimulai dari elemen pada indeks terkecil hingga terbesar. Pemrosesan sekuensial lebih sering menggunakan pengulangan (loop/iterasi) dalam setiap prosesnya.

Sebab pemrosesan sekuensial melibatkan semua elemen di dalamnya, ada beberapa hal yang perlu diperhatikan.

Setiap elemen array diakses secara langsung melalui indeksnya (metode indexing).
Elemen pertama (first element) adalah elemen array dengan indeks terkecil yang selalu dimulai dari 0. 
Elemen selanjutnya (next element) dicapai melalui suksesor indeks.
Kondisi berhenti dicapai jika indeks yang diproses adalah indeks terbesar yang sudah terdefinisi.
Suatu array tidak boleh kosong, minimal memiliki satu elemen di dalamnya.
Mari bahas lebih lanjut dengan contoh di bawah ini.
'''

var_arr = [1,2,3,4,5]
for i in range(len(var_arr)):
    current_element = var_arr[i] # var_arr[i] motede indexing
    next_index = 1 + i #suksesor array

    if next_index < len(var_arr):
        next_element = var_arr[next_index]
    else:
        next_element = None
    print(f'Current element: {current_element}, next elements: {next_element}')

'''
Pada contoh di atas, kita membuat program untuk melakukan pemrosesan sekuensial array. 
Proses tersebut adalah mencetak setiap elemen yang berada pada variabel array "var_arr" menggunakan perulangan loop. 
'''

'''
Pertama-tama, kita menginisialisasi variabel "var_arr" dengan nilai "[1, 2, 3, 4, 5]". Perulangan for digunakan untuk melakukan iterasi melalui setiap elemen array. Variabel "i" bertindak sebagai indeks saat ini yang digunakan untuk mengakses elemen dalam setiap iterasi atau perulangan.

Kemudian, setiap proses perulangan berlangsung, kita mengambil elemen saat ini menggunakan "var_arr[i]" dan menyimpannya pada variabel "current_element". Selanjutnya adalah mencari indeks berikutnya dengan cara menambahkan nilai "1" pada indeks saat ini atau "i". 

Hasil dari operasi penjumlahan nilai "1" dengan indeks saat ini akan disimpan pada variabel "next_index". "next_index" berperan sebagai "suksesor indeks" yang merujuk pada indeks berikutnya berdasarkan indeks saat ini dengan menambahkan nilai "1". 

Kemudian kita memeriksa "next_index" berada dalam rentang indeks yang valid dalam array atau tidak. Jika iya, artinya masih ada elemen berikutnya, dan kita ambil elemen berikutnya tersebut menggunakan "var_arr[next_index]" serta menyimpannya dalam variabel "next_element". Sebaliknya, jika "next_index" tidak valid atau melebihi rentang array, artinya tidak ada elemen berikutnya sehingga kita menetapkan "next_element" sebagai "None".

Pada langkah terakhir, kita mencetak nilai "current_element" dan "next_element" untuk menunjukkan perbedaan antara elemen sekarang dan selanjutnya.

Mencetak setiap elemen array menggunakan perulangan adalah satu di antara banyaknya contoh-contoh persoalan pemrosesan sekuensial pada array. Contoh lain dari pemrosesan array adalah berikut.

Mengisi array secara sekuensial.
Menghitung nilai rata-rata elemen array.
Mengalikan elemen array dengan suatu nilai.
Mencari nilai terbesar atau terkecil pada array.
Mencari indeks letak suatu nilai ditemukan pertama kali dalam array, dan sebagainya.
Dari sekian banyak contoh pemrosesan tersebut, mari kita pelajari dalam materi berikutnya tentang cara mencari nilai terbesar pada array.
'''