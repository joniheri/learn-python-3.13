import math


class Bentuk:
    def hitung_luas(self):
        pass  # Metode ini akan diimplementasikan di subclass

    def hitung_keliling(self):
        pass  # Metode ini akan diimplementasikan di subclass


class Lingkaran(Bentuk):
    def __init__(self, radius):
        self.radius = radius

    def hitung_luas(self):
        return math.pi * self.radius * self.radius

    def hitung_keliling(self):
        return 2 * math.pi * self.radius


class Persegi(Bentuk):
    def __init__(self, sisi):
        self.sisi = sisi

    def hitung_luas(self):
        return self.sisi * self.sisi

    def hitung_keliling(self):
        return 4 * self.sisi


# Membuat objek Lingkaran dan Persegi
lingkaran1 = Lingkaran(5)
persegi1 = Persegi(4)

# Menghitung dan mencetak luas dan keliling
print("Lingkaran:")
print("Luas:", lingkaran1.hitung_luas())
print("Keliling:", lingkaran1.hitung_keliling())

print("\nPersegi:")
print("Luas:", persegi1.hitung_luas())
print("Keliling:", persegi1.hitung_keliling())
