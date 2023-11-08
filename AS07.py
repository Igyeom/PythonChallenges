mode = input("Encrypt or Decrypt? [e/d] ")

if mode == "e":
    alphabet = list("ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ")
    decrypted = list(input("Decrypted Plaintext: ").upper())
    key = int(input("Key: "))
    for j in decrypted:
        print(alphabet[alphabet.index(j)+key], end='')
    print()
elif mode == "d":
    alphabet = list("abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz")
    encrypted = list(input("Encrypted Ciphertext: ").lower())
    
    for i in range(26):
        for j in encrypted:
            print(alphabet[alphabet.index(j)+i], end='')
        print()
else:
    print("Invalid mode.")
