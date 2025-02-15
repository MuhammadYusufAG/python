# deklarasi matrik


# Deklarasi sekaligus inisialisasi nilai matriks.
'''
<nama-var> = [[<value-11>,<val-12>, ..., <val-1m>],[<val-21>,<val-22>, ..., <val-2m>],... [<val-n1>,<val-n2>, ..., <val-nm>]]
'''
matriks = [[1, 0, 0, 0, 0],
            [0, 1, 0, 0, 0],
            [0, 0, 1, 0, 0],
            [0, 0, 0, 1, 0],
            [0, 0, 0, 0, 1]]
print(matriks)


# deklarasi dengan default

'''

'''

matriks = [[0 for j in range(4)] for i in range(3)]

print(matriks)

# akses elementmatriks

var_mat = [[1, 2, 3, 4, 5],
           [6, 7, 8, 9, 10],
           [11, 12, 13, 14, 15],
           [16, 17, 18, 19, 20],
           [21, 22, 23, 24, 25]]
           
print(var_mat[2][1])