'''creating table and inserting data into it using sqlite3'''
import sqlite3

# Fungsi untuk membuat tabel jika belum ada


def create_table():
    conn = sqlite3.connect('AbdulHadi.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS data
                 (id INTEGER PRIMARY KEY, name TEXT, age INTEGER)''')
    conn.commit()
    conn.close()

# Fungsi untuk menyisipkan data ke dalam tabel


def insert_data(name, age):
    conn = sqlite3.connect('AbdulHadi.db')
    c = conn.cursor()
    c.execute('''INSERT INTO data (name, age) VALUES (?, ?)''', (name, age))
    conn.commit()
    conn.close()

# Fungsi untuk meminta input pengguna dan menyimpannya ke dalam database


def input_and_save_data():
    name = input("Masukkan nama: ")
    age = int(input("Masukkan usia: "))
    insert_data(name, age)
    print("Data telah disimpan!")


# Membuat tabel jika belum ada
create_table()

# Meminta input dari pengguna dan menyimpannya ke dalam database
input_and_save_data()
