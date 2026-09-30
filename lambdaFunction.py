import math

luas_lingkaran = lambda r: math.pi * (r ** 2)

# Eksekusi Program
print("=== PROGRAM HITUNG LUAS LINGKARAN ===")
try:
    r = float(input("Masukkan panjang jari-jari lingkaran: "))
    if r < 0:
        print("Error: Jari-jari lingkaran tidak boleh bernilai negatif.")
    else:
        hasil = luas_lingkaran(r)
        print(f"Luas lingkaran dengan jari-jari {r} adalah: {hasil:.2f}")
except ValueError:
    print("Error: Harap masukkan nilai angka yang valid.")