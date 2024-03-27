'''cak kocak'''
import sqlite3

# Fungsi untuk membuat tabel buku jika belum ada
def create_table():
    conn = sqlite3.connect('perpustakaan.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS buku
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                 judul TEXT,
                 pengarang TEXT,
                 tahun_terbit INTEGER)''')
    conn.commit()
    conn.close()

# Fungsi untuk menambahkan buku baru
def tambah_buku(judul, pengarang, tahun_terbit):
    conn = sqlite3.connect('perpustakaan.db')
    c = conn.cursor()
    c.execute("INSERT INTO buku (judul, pengarang, tahun_terbit) VALUES (?, ?, ?)", (judul, pengarang, tahun_terbit))
    conn.commit()
    conn.close()
    
# Fungsi untuk menampilkan semua buku
def tampilkan_semua_buku():
    conn = sqlite3.connect('perpustakaan.db')
    c = conn.cursor()
    c.execute("SELECT * FROM buku")
    rows = c.fetchall()
    conn.close()
    if rows:
        print("{:<5} {:<40} {:<45} {:<10}".format("ID", "Judul", "Pengarang", "Tahun"))
        print("-" * 105)
        for row in rows:
            print("{:<5} {:<40} {:<45} {:<10}".format(row[0], row[1], row[2], row[3]))
            print("-" * 105)
    else:
        print("Tidak ada buku dalam perpustakaan.")

# Fungsi utama
if __name__ == "__main__":
    create_table()

    while True:
        print("\n=== MENU PERPUSTAKAAN ===")
        print("1. Tambah Buku")
        print("2. Tampilkan Semua Buku")
        print("3. Keluar")

        choice = input("Pilih menu: ")

        if choice == '1':
            judul = input("Masukkan judul buku: ")
            pengarang = input("Masukkan nama pengarang: ")
            tahun_terbit = input("Masukkan tahun terbit: ")
            tambah_buku(judul, pengarang, tahun_terbit)
            print("Buku berhasil ditambahkan.")

        elif choice == '2':
            print("\n=== DAFTAR BUKU ===")
            tampilkan_semua_buku()

        elif choice == '3':
            print("Terima kasih!")
            break

        else:
            print("Pilihan tidak valid. Silakan pilih menu yang benar.")
