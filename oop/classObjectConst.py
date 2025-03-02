# class

# class Car:
#     pass

# class Car:
#     # Atribute
#     warna = 'blue'


# object

# class Car:
#     warna = 'blue'

# mobil_1 = Car()
# print(mobil_1.warna)

# mobil_1.warna = 'red'
# print(mobil_1.warna)


# Atribute
# class Car:
#     warna = 'blue'

# mobil_1 = Car()
# print(mobil_1.warna)

# mobil_2 = Car()
# print(mobil_2.warna)  # Output: blue

# Car.warna = 'black'

# print(mobil_1.warna)
# print(mobil_2.warna)


# class constructor
# class Car():
#     def __init__(self):
#         self.warna = 'Red'

# mobil_1 = Car()
# mobil_2 = Car()

# print(mobil_1.warna)
# print(mobil_2.warna)

# mobil_1.warna = 'Blue'

# print(mobil_1.warna)
# print(mobil_2.warna)

class Mobil:
    def __init__(self, warna, merek, kecepatan):
        self.warna = warna
        self.merek = merek
        self.kecepatan = kecepatan

mobil_1 = Mobil('Red', 'Toyota', 140)

print(mobil_1.warna)
print(mobil_1.merek)