'''UTS BAPRO - Caesar Cipher'''
# Fungsi untuk enkripsi teks dengan Caesar Cipher


def caesar_encrypt(plaintext, shift):
    ciphertext = ""
    for char in plaintext:
        # Cek apakah karakter adalah huruf
        if char.isalpha():
            # Tentukan offset ASCII berdasarkan huruf besar atau kecil
            ascii_offset = ord('a') if char.islower() else ord('A')
            # Enkripsi karakter
            encrypted_char = chr(
                (ord(char) - ascii_offset + shift) % 26 + ascii_offset)
            ciphertext += encrypted_char
        else:
            ciphertext += char
    return ciphertext

# Fungsi untuk dekripsi teks dengan Caesar Cipher


def caesar_decrypt(ciphertext, shift):
    # Dekripsi adalah enkripsi dengan shift negatif
    return caesar_encrypt(ciphertext, -shift)

# Fungsi utama


def main():
    while True:
        print("\nProgram Caesar Cipher")
        print(" 1. Enkripsi teks")
        print(" 2. Dekripsi teks")
        print(" 3. Keluar")
        # Minta pengguna untuk memilih opsi
        choice = input("Masukkan Pilihan: ")
        if choice == '1':
            # Enkripsi teks
            plaintext = input("Masukkan teks yang akan di enkripsi: ")
            shift = int(input("Masukkan nilai geseran: "))
            print(caesar_encrypt(plaintext, shift))
        elif choice == '2':
            # Dekripsi teks
            ciphertext = input("Masukkan teks yang akan di dekripsi: ")
            shift = int(input("Masukkan nilai geseran: "))
            print(caesar_decrypt(ciphertext, shift))
        elif choice == '3':
            # Keluar dari program
            print("Terimakasih")
            break
        else:
            # Jika pengguna memasukkan pilihan yang tidak valid
            print("Pilihan Salah. Silahkan Masukkan 1, 2, atau 3.")


if __name__ == "__main__":
    main()
