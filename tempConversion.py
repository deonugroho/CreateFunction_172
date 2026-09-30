def konversi_suhu(nilai, satuan):
    satuan = satuan.upper()
    if satuan == 'C':
        return (nilai * 9/5) + 32
    elif satuan == 'F':
        return (nilai - 32) * 5/9
    else:
        return "Satuan tidak valid! Gunakan 'C' untuk Celsius atau 'F' untuk Fahrenheit."

# Contoh penggunaan :
print(f"30°C = {konversi_suhu(30, 'C')}°F")
print(f"86°F = {konversi_suhu(86, 'F')}°C")