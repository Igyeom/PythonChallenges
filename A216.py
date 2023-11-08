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

# may need this word list: https://gist.githubusercontent.com/jamesabela/d956da0889582e5c5c8fc34ed72b97c3/raw/5a559a4efeb4050438c52c5b3a919d5065de51a8/wordlist.txt
