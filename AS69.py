alphabet = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"
print("This program will read a file named 'encoded.txt' or 'decoded.txt' depending on the mode. Make sure it's in the SAME DIRECTORY as the program.")
mode = input("Encode or Decode? (e/d) ")
if mode.strip().lower() == "d":
    with open("encoded.txt", "r") as f:
        content = f.read()
    arr = ["" for _ in range(26)]
    for k in range(26):
        for i in content:
            arr[k] += alphabet[ord(i.lower())-97+k]
        print(f"{k}. {arr[k]}")
    s = int(input("Choose the number with the correctly decoded message: "))
    with open("decoded.txt", "w") as f:
        f.write(arr[s])
else:
    with open("decoded.txt", "r") as f:
        content = [*f.read()]
    k = int(input("Key: "))
    for i in range(len(content)):
        content[i] = alphabet[ord(content[i].lower())-97+k]
    print("".join(content))
    with open("encoded.txt", "w") as f:
        f.write("".join(content))
