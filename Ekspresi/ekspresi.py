# penerapan ekspresi pada python

x = 10
y =2
result = x - y
print(result) # output: 8


angka = [2,4,6,8]
huruf = ['q','w','e','r','t','y']
mix = angka + huruf
print(mix)

learn = ['P', 'Y', 'T', 'H', 'O', 'N']
replikasi = learn * 2
print(replikasi) 


# Jenis-jenis ekspresi
'''
Jenis dan  Contoh

Ekspresi aritmetika: 
<numerik> <operator> <numerik> = <numerik>
2 + 2 = 4, 2 - 2 = 0

Ekspresi relasional: 
<numerik> <operator> <numerik> = <boolean>
3 < 10 = True, 1 > 10 = False

Ekspresi logika: 
<boolean> <operator> <boolean> = <boolean>
True or False = True

Sebagaimana judulnya, jenis-jenis ini adalah ekspresi yang dikelompokkan berdasarkan tipe data yang dihasilkan. Mari kita bedah satu per satu.

1.Ekspresi aritmetika: jenis ekspresi yang memiliki operan bertipe numerik dan menghasilkan numerik.
2.Ekspresi relasional: jenis ekspresi yang memiliki operan bertipe numerik dan menghasilkan nilai boolean/logika.
3.Ekspresi logika: jenis ekspresi yang memiliki operan bertipe boolean/logika dan menghasilkan nilai boolean/logika.
'''
# contoh ekspresi dari atas
print(2+2)
print(3<10)
print(True or False)


# arity dari operator//ekspresi uner
a = True
a = not a
print(a)#false

b = 6
b -= 1
print(b)#5

c = 6
c += 1
print(c)#7

d = 10
print(-d)#-10

