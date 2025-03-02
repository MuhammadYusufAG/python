def my_decoration (func):
    def wrapper():
        print("Sebelum fungsi dieksekusi.")
        func()
        print("Setelah fungsi dieksekusi.")
    return wrapper

# dekorasi fungsi dengan decoration
@my_decoration
def say_hello():
    print('Hello, World')

# memanggil fungsi dari decoration
say_hello()

# documentasi
# https://docs.python.org/id/3.8/glossary.html#term-decorator


# Object Method
class Mobil:
    def __init__(self, warna, merek, kecepatan):
        self.warna = warna
        self.merek = merek
        self.kecepatan = kecepatan

    def tambah_kecepatan(self):
        self.kecepatan += 10

# Mobil.tambah_kecepatan()
'''
  Mobil.tambah_kecepatan()
    ~~~~~~~~~~~~~~~~~~~~~~^^
TypeError: Mobil.tambah_kecepatan() missing 1 required positional argument: 'self'
'''

mobil_1 = Mobil('Red', 'Audi', 250)
print('sebelum ditambhkan kecepatan')
print(mobil_1.kecepatan)

mobil_1.tambah_kecepatan()

print('setelah ditambah kecepatan')
print(mobil_1.kecepatan)



# method static

class Car:
    def __init__(self,merek):
        self.merek = merek

    @staticmethod
    def intro_car():
        print("Ini adalah metode dari kelas Mobil")

Car.intro_car()

car_1 = Car('Audi')
car_1.intro_car()


# class method

class Mobil:
    def __init__(self,merek):
        self.merek = merek
        
    @classmethod
    def intro_mobil(cls):
        print("Ini adalah metode dari kelas Mobil")

Mobil.intro_mobil()

mobil_1 = Mobil('Mcleren')
mobil_1.intro_mobil()

# cls diubah ke *arg
class Mobil:
    def __init__(self,merek):
        self.merek = merek
        
    @classmethod
    def intro_mobil(*args):
        print(args)

Mobil.intro_mobil()

mobil_1 = Mobil('Mcleren')
mobil_1.intro_mobil()