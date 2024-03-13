# '''variabel py'''
# nama = input("Masukkan nama: ")
# alamat = input("Masukkan alamat: ")
# umur = input("Masukkan umur: ")
# tempatlahir = input("Masukkan tempat lahir: ")
# tgllahir = input("Masukkan tanggal lahir: ")
# ipk = input("Masukkan IPK: ")
# print("Nama: ", nama)
# print("Alamat: ", alamat)
# print("Umur: ", umur)
# print("Tempat Lahir: ", tempatlahir)
# print("Tanggal Lahir: ", tgllahir)
# print("IPK: ", ipk)

# '''eval function'''
# x1 = eval(input("Masukkan nilai x1: "))
# x2 = eval(input("Masukkan nilai x2: "))
# x3 = eval(input("Masukkan nilai x3: "))
# x4 = eval(input("Masukkan nilai x4: "))
# jumlah = x1 + x2 + x3 + x4
# kali = x1 * x2 * x3 * x4
# print("Jumlah: ", jumlah)
# print("Kali: ", kali)
# jumlah = jumlah + 0.5
# print("Jumlah baru: ", jumlah)
# kali = kali * 0.5
# print("Kali baru: ", kali)

'''kode program 3'''
total_harga = 0
kd_barang = input("Masukkan kode barang: ")
nm_barang = input("Masukkan nama barang: ")
harga_satuan = int(input("Masukkan harga barang: "))
jumlah = int(input("Masukkan jumlah barang: "))
harga_beli = harga_satuan * jumlah
total_harga = total_harga + harga_beli
print("total harga yang dibayar Rp.", total_harga)
