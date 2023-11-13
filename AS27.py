ans = []
with open("words.txt", "r", encoding="utf-8") as f:
    words = f.read().lower().splitlines()
for i in words:
    chain = [i]
    for j in words:
        if j not in chain and j[0] == chain[-1][-1]:
            chain.append(j)
    if len(chain) > len(ans):
        ans = chain

print(ans)

# i used this wordlist: https://gist.githubusercontent.com/ralts00/31415709fb34c1b2ec556c396efc3d80/raw/516ef1179f10f4a0ecb4f50f118e6757fef85243/pokemon_names.txt
