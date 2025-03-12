# ================================================================
# 1 Fungsi Dasar (Tanpa Parameter)
# ================================================================
print("1 Fungsi Dasar (Tanpa Parameter)")


def sapa_dunia():
    print("Halo, Dunia!")


sapa_dunia()  # Memanggil fungsi
print("")
# ================================================================


# ================================================================
# 2. Fungsi dengan Parameter
# ================================================================
print("2. Fungsi dengan Parameter")


def sapa_nama(nama):
    print("Halo,", nama + "!")


sapa_nama("Budi")  # Memanggil fungsi dengan parameter
print("")
# ================================================================


# ================================================================
# 3. Fungsi dengan Parameter Default
# ================================================================
print("3. Fungsi dengan Parameter Default")


def sapa_orang(nama="Pengunjung"):
    print("Halo,", nama + "!")


sapa_orang()  # Memanggil fungsi tanpa parameter (menggunakan default)
sapa_orang("Siti")  # Memanggil fungsi dengan parameter
print("")
# ================================================================


# ================================================================
# 4. Fungsi dengan Return Value
# ================================================================
print("4. Fungsi dengan Return Value")


def tambah(a, b):
    hasil = a + b
    return hasil


hasil_penjumlahan = tambah(5, 3)
print("Hasil penjumlahan:", hasil_penjumlahan)
print("")
# ================================================================


# ================================================================
# 5. Fungsi Lambda (Fungsi Anonim)
# ================================================================
print("5. Fungsi Lambda (Fungsi Anonim)")
kali_dua = lambda x: x * 2
print(kali_dua(7))
print("")
# ================================================================


# ================================================================
# 6. Fungsi dengan Arbitrary Arguments (*args)
# ================================================================
print("6. Fungsi dengan Arbitrary Arguments (*args)")


def jumlahkan_angka(*angka):
    total = 0
    for n in angka:
        total += n
    return total


print(jumlahkan_angka(1, 2, 3, 4, 5))
print("")
# ================================================================


# ================================================================
# 7. Fungsi dengan Arbitrary Keyword Arguments (**kwargs)
# ================================================================
print("7. Fungsi dengan Arbitrary Keyword Arguments (**kwargs)")


def tampilkan_info(**info):
    for kunci, nilai in info.items():
        print(kunci + ": " + str(nilai))


tampilkan_info(nama="Ani", usia=25, kota="Bandung")
print("")
# ================================================================


# ================================================================
# 8. Fungsi Rekursif
# ================================================================
print("8. Fungsi Rekursif")


def faktorial(n):
    if n == 0:
        return 1
    else:
        return n * faktorial(n - 1)


print(faktorial(5))
print("")
# ================================================================
