def konversi_suhu(nilai, satuan):
    satuan = satuan.upper()
    if satuan == 'C':
        return (nilai * 9/5) + 32
    elif satuan == 'F':
        return (nilai - 32) * 5/9
    else:
        return None

# Eksekusi Program
print("=== PROGRAM KONVERSI SUHU ===")
try:
    nilai_input = float(input("Masukkan nilai suhu: "))
    satuan_input = input("Masukkan satuan asal ('C' untuk Celsius, 'F' untuk Fahrenheit): ").strip()

    hasil = konversi_suhu(nilai_input, satuan_input)

    if satuan_input.upper() == 'C':
        print(f"Hasil: {nilai_input}°C = {hasil:.2f}°F")
    elif satuan_input.upper() == 'F':
        print(f"Hasil: {nilai_input}°F = {hasil:.2f}°C")
    else:
        print("Error: Satuan tidak valid! Gunakan huruf 'C' atau 'F'.")
except ValueError:
    print("Error: Harap masukkan nilai angka yang valid.")