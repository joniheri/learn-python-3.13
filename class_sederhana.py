class Mobil:
    def __init__(self, merek, warna):
        self.merek = merek
        self.warna = warna

    def info(self):
        print(f"Mobil ini bermerek {self.merek} dan berwarna {self.warna}")

    def jalan(self):
        print("Mobil sedang berjalan")


# Membuat objek dari class Mobil
mobil_saya = Mobil("Toyota", "Merah")

# Mengakses atribut objek
print(mobil_saya.merek)
print(mobil_saya.warna)

# Memanggil metode objek
mobil_saya.info()
mobil_saya.jalan()

mobil_teman = Mobil("Honda", "Hitam")
mobil_teman.info()
