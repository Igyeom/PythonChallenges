option = input("Type 'e' for encryption, type 'd' for decryption: ").lower()

if option.lower() == 'e':
    key = input("Key (string): ")
    plaintext = input("Plaintext: ")
    ciphertext = ""
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for i in range(len(plaintext)):
        ciphertext += alphabet[alphabet.index(plaintext[i].upper()) + alphabet.index(key[i%len(key)].upper())]
    print("Ciphertext:", ciphertext)
elif option.lower() == 'd':
    key = input("Key (string): ")
    ciphertext = input("Ciphertext: ")
    plaintext = ""
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for i in range(len(ciphertext)):
        plaintext += alphabet[alphabet.index(ciphertext[i].upper()) - alphabet.index(key[i%len(key)].upper())]
    print("Plaintext:", plaintext.lower())
else:
    print("Please enter a valid mode.")
