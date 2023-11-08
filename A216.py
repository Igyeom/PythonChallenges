from itertools import permutations

word = input()

with open("wordlist.txt","r") as f:
    words = f.read().splitlines()

total = 0
for p in permutations(word):
    if ''.join(p) in words:
        print(''.join(p))
        total += 1

print(total-1, "anagram(s) found [note: there are duplicates in the word list given by Mr. Abela]")
