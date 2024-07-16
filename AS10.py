s=""
ans=0
while s!="oiuroieurpyejuvm":
  s=input()
  if "ab" in s or "cd" in s or "pq" in s or "xy" in s: continue
  if sum([s.count(i) for i in "aeiou"]) >= 3:
    for i in range(1, len(s)):
      if s[i-1] == s[i]: break
    else:
      continue
    ans += 1
print(ans)


# note: you must feed the input file into stdin (standard input)
