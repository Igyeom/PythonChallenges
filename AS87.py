word1, word2 = input().split()
for i in range(max(map(len,[word1, word2]))):
    try: print(word1[i], end='')
    except IndexError: pass
    try: print(word2[i], end='')
    except IndexError: pass
