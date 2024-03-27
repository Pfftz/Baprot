# angka = float(input("Masukkan angka: "))

# akar_kuadrat = angka ** 0.5

# print(f"Akar kuadrat dari {angka} adalah {akar_kuadrat}")

# alas = float(input("Masukkan alas: "))
# tinggi = float(input("Masukkan tinggi: "))
# luas_segitiga = 0.5 * alas * tinggi

# print(f"Luas segitiga dengan alas {alas} dan tinggi {tinggi} adalah {luas_segitiga}")

#input tugas, uts, uas
tugas = float(input("Masukkan nilai tugas: "))
uts = float(input("Masukkan nilai UTS: "))
uas = float(input("Masukkan nilai UAS: "))

#menghitung nilai akhir
nilai_akhir = (0.15 * tugas) + (0.35 * uts) + (0.5 * uas)

if nilai_akhir > 80:
    grade = "A"
elif nilai_akhir > 70:
    grade = "B"
elif nilai_akhir > 60:
    grade = "C"
elif nilai_akhir > 50:
    grade = "D"
else:
    grade = "E"
    
#menentukan status kelulusan
if nilai_akhir > 60:
    status = "Lulus"
else:
    status = "Tidak Lulus"
    
print(f"Nilai akhir anda adalah {nilai_akhir} dengan grade {grade} dan status {status}")