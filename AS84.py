alphabet = list("abcdefghijklmnopqrstuvwxyz abcdefghijklmnopqrstuvwxyz ")
encrypted = list(input("Encrypted Ciphertext: ").lower())
possible = []
prob = []
with open('likely.txt', 'r') as f:
    likely = f.read().splitlines()

for i in range(27):
    possible.append([])
    for j in encrypted:
        possible[i].append(alphabet[alphabet.index(j)+i])

score = [0 for _ in range(27)]

for i in range(len(possible)):
    for j in range(len(likely)):
        if likely[j] in "".join(possible[i]):
            score[i] += 10000-j

print("Sorted in descending order by likeliness:")
for i in sorted(possible, key=lambda x: score[possible.index(x)], reverse=True):
    print(''.join(i))
