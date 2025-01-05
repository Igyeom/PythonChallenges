# print(__import__("secrets").token_urlsafe(16))

# another simple one-liner (46B/46C)

with open("passphrase.txt", "w") as f:f.write(__import__("secrets").token_urlsafe(16))

# includes file handling (50 bonus points)
