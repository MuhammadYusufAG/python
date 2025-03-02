# mobil pada umumnya
class Mobil:
    def __init__(self, warna, merek, kecepatan):
        self.warna = warna
        self.merek = merek
        self.kecepatan = kecepatan

    def tambah_kecepatan(self):
        self.kecepatan += 10

# mobil sport
class MobilSport(Mobil):
    def turbo (self):
        self.kecepatan += 50

    def tambah_kecepatan(self): #menambah kecepatan
        # self.kecepatan += 20 #override
        super().tambah_kecepatan() #super
        print("Kecepatan Anda meningkat! Hati-Hati!")

# kelas mobil biasa
mobil_1 = Mobil("Merah", "DicodingCar", 160)
print(mobil_1.kecepatan)

# kelas mobil sport
mobil_sport_1 = MobilSport("Hitam", "DicodingSportCar", 160)
print(mobil_sport_1.kecepatan)

mobil_sport_1.turbo()
print(mobil_sport_1.kecepatan)

# memanggil kecepatan
mobil_sport_1 = MobilSport("Hitam", "DicodingSportCar", 160)
print(mobil_sport_1.kecepatan)
mobil_sport_1.tambah_kecepatan()     # Memanggil metode baru tambah kecepatan()
print(mobil_sport_1.kecepatan)        # Menampilkan kecepatan



