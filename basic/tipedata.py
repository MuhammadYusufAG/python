# tipe data
age = 17
salary = 5000000.0

print(type(age))
print(type(salary))

x = 6
print(type(x))

x = "5"
print(type(x))

x = 6.0
print(type(x))

x = 1+2j
print(type(x))

# immutable / nilai didalam tidak dapat diubah
var = 10
print(var)
print(id(var))
var = 11
print(var)
print(id(var))

# boolean
x = True
print(type(x))

x = False
print(type(x))

# string
x = 'Dicoding'
print(type(x))

# multiLine string
multi_line = """Halo!
Kapan terakhir kali kita bertemu?
Kita bertemu hari Jum’at yang lalu."""

print(multi_line)

# indexing/slicing
x = 'Dicoding'
print(x[2:])

# formatted string use f
name = "muhammad yusuf"
print(f"Hello nama saya {name}")

# formatted use %
name = "muhammad yusuf"
print("Hello nama saya %s" % name)

# str.format()
name = "muhammad yusuf"
print("Hello nama saya {}".format(name))


# TIPE DATA COLLECTION or array

x = [1,2.3, "dicoding"]
print(type(x))

# indexing
x = [1, 'Dicoding', True, 1.0]
print(x[2])#output true

# list py bersifat mutable yang bisa diubah nilainya
x = [1, 2.2, 'Dicoding']
x[0] = 'Indonesia'
print(x)
# Output:
# ['Indonesia', 2.2, 'Dicoding']

x = ["laptop", "monitor", "mouse", "mousepad", "keyboard", "webcam", "microphone"]
print(x[0])
print(x[2])
print(x[-1])
print(x[-3])


# slicing
x = ["laptop", "monitor", "mouse", "mousepad", "keyboard", "webcam", "microphone"]

print(x[0:5:2]) #['laptop', 'mouse', 'keyboard']
print(x[1:]) #['monitor', 'mouse', 'mousepad', 'keyboard', 'webcam', 'microphone']
print(x[:3]) #['laptop', 'monitor', 'mouse']

# tuple
x = (1, "Dicoding", 1+3j)
print(type(x))

x = (5, 'program', 1+3j)
print(x[1])
print(x[0:3])

# tuple tidak dapat diubah karna bersifat immutable
# x = (5, 'program', 1+3j)
# x[1] = 'Dicoding'

# set
# x = {1,2,7,2,3,13,3}
# print(x[0])

x = {1, 2, 7, 2, 3, 13, 3}
print(x)
print(type(x))

# OOP
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

union = set1.union(set2)
print("Union:", union)

intersection = set1.intersection(set2)
print("Intersection:", intersection)


# Dictionary / KEY AND VALUE

x = {'name': 'muhammad yusuf', 'age': 18, 'isMarried': False}
print(type(x))
#print(x[0]) #KeyError: 0
print(x['name'])

# menambahkan data Dicti
x ['job'] = 'web dev'
print(x)

# menghapus data Dicti
del x['isMarried']
print(x)

# mengubah data
x['name'] = 'dicoding'
print(x)


# KONVERSI TIPE DATA

# int ke float
print(float(5)) #5.0

# float ke int
print(int(5.6)) #5
print(int(-5.6)) #-5

# int,float,str ke str / dari-dan-ke string
print(int("25"))
print(str(25))
print(float("25"))
print(str(25.6))

# print(int("1p")) #ValueError: invalid literal for int() with base 10: '1p

# Konversi kumpulan data
print(set([1,2,3]))
print(tuple({5,6,7}))
print(list("hello"))

# KONVERSI ke Dictionary
# list ke dict
print(dict([[1,2],[3,4]]))
# tuple ke dict
print(dict([(3,26),(4,44)]))
