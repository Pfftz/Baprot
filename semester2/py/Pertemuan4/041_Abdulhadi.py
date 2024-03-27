'''Tugas Harian 3/13/2024'''
kode_brg = 'AI001'
nama_brg = 'Kacamata'
harga_satuan = 150000
stok = 10
print('Tugas Harian Bapro 3/13/2024')
jumlah_beli = int(input(' Masukkan jumlah barang yang dibeli: '))
total_bayar = harga_satuan * jumlah_beli
sisa_stok = stok - jumlah_beli

if jumlah_beli > stok:
    print(' Maaf stok barang tidak mencukupi')
else:
    print('\n Kode Barang = %s \n Nama Barang = %s \n Harga Satuan = Rp. %d \n Stok = %d \n Jumlah Barang = %d \n Total Bayar = %d \n Sisa Barang = %d' %(kode_brg, nama_brg, harga_satuan, stok, jumlah_beli, total_bayar, sisa_stok))
    harga_barang = float(harga_satuan)
    total_bayar = float(total_bayar)
    print('\n Output dalam float 3 angka dibelakang koma \n Harga Satuan Barang = Rp.%.3f \n Total Bayar = Rp.%.3f' %(harga_barang, total_bayar))

# Nama : Abdulhadi Muntashir
# NIM  : 3337230041
