def caesar_decrypt(ciphertext, shift):
    plaintext = ""
    for char in ciphertext:
        if char.isalpha():
            ascii_offset = ord('a') if char.islower() else ord('A')
            decrypted_char = chr(
                (ord(char) - ascii_offset - shift) % 26 + ascii_offset)
            plaintext += decrypted_char
        else:
            plaintext += char
    return plaintext


if __name__ == "__main__":
    ciphertext = input("Enter the text to decrypt: ")
    shift = int(input("Enter the shift value: "))
    print(caesar_decrypt(ciphertext, shift))
