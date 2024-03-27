import sqlite3

# Fungsi untuk membuat tabel ktp jika belum ada


def create_table():
    conn = sqlite3.connect('ktp.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS ktp
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                 nik TEXT,
                 nama TEXT,
                 ttl TEXT,
                 jenis_kelamin TEXT,
                 alamat TEXT,
                 agama TEXT,
                 status_perkawinan TEXT,
                 pekerjaan TEXT,
                 kewarganegaraan TEXT,
                 belaku_hingga TEXT DEFAULT "seumur hidup")''')
    conn.commit()
    conn.close()

# Fungsi untuk menambahkan data ktp baru


def tambah_ktp(nik, nama, ttl, jenis_kelamin, alamat, agama, status_perkawinan, pekerjaan, kewarganegaraan):
    conn = sqlite3.connect('ktp.db')
    c = conn.cursor()
    c.execute("INSERT INTO ktp (nik, nama, ttl, jenis_kelamin, alamat, agama, status_perkawinan, pekerjaan, kewarganegaraan) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)",
              (nik, nama, ttl, jenis_kelamin, alamat, agama, status_perkawinan, pekerjaan, kewarganegaraan))
    conn.commit()
    conn.close()

# Fungsi untuk menampilkan semua data ktp


def tampilkan_semua_ktp():
    conn = sqlite3.connect('ktp.db')
    c = conn.cursor()
    c.execute("SELECT * FROM ktp")
    rows = c.fetchall()
    conn.close()
    if rows:
        print("{:<3} {:<15} {:<25} {:<15} {:<15} {:<25} {:<15} {:<18} {:<15} {:<18} {:<15}".format("ID", "NIK", "Nama",
              "TTL", "Jenis Kelamin", "Alamat", "Agama", "Status Perkawinan", "Pekerjaan", "Kewarganegaraan", "Belaku Hingga"))
        print("-" * 190)
        for row in rows:
            print("{:<3} {:<15} {:<25} {:<15} {:<15} {:<25} {:<15} {:<18} {:<15} {:<18} {:<15}".format(
                row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10]))
            print("-" * 190)
    else:
        print("Tidak ada data KTP.")


# Fungsi utama
if __name__ == "__main__":
    create_table()

    while True:
        print("\n=== MENU KTP ===")
        print("1. Tambah Data KTP")
        print("2. Tampilkan Semua Data KTP")
        print("3. Keluar")

        choice = input("Pilih menu: ")

        if choice == '1':
            nik = input("Masukkan NIK: ")
            nama = input("Masukkan Nama: ")
            ttl = input("Masukkan TTL: ")
            jenis_kelamin = input("Masukkan Jenis Kelamin: ")
            alamat = input("Masukkan Alamat: ")
            agama = input("Masukkan Agama: ")
            status_perkawinan = input("Masukkan Status Perkawinan: ")
            pekerjaan = input("Masukkan Pekerjaan: ")
            kewarganegaraan = input("Masukkan Kewarganegaraan: ")
            tambah_ktp(nik, nama, ttl, jenis_kelamin, alamat, agama,
                       status_perkawinan, pekerjaan, kewarganegaraan)
            print("Data KTP berhasil ditambahkan.")

        elif choice == '2':
            print("\n=== DAFTAR DATA KTP ===")
            tampilkan_semua_ktp()

        elif choice == '3':
            print("Terima kasih!")
            break

        else:
            print("Pilihan tidak valid. Silakan pilih menu yang benar.")
