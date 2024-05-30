def calculate_score(v1, t1, s1):
    major_card = -1

    if len(set(t1)) == 1:
        s1 = max(s1, 5)

    for i in range(2, 11):
        if v1 == [i, i+1, i+2, i+3, i+4]:
            if len(set(t1)) == 1:
                if i == 10:
                    s1 = max(s1, 9)
                s1 = max(s1, 8)
            s1 = max(s1, 4)
    
    cnt = [[] for _ in range(16)]

    for i in range(5):
        cnt[v1[i]].append(i)
    
    lengths = [*map(len, cnt)]

    major_card = lengths.index(max(lengths))

    if max(lengths) == 4:
        s1 = max(s1, 7)

    if max(lengths) == 3:
        if 2 in lengths:
            s1 = max(s1, 6)
        s1 = max(s1, 3)
    if lengths.count(2) == 2:
        s1 = max(s1, 2)
    if lengths.count(2) == 1:
        s1 = max(s1, 1)
    return s1, major_card

ans = 0
hands = []
key = {"2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "T": 10, "J": 11, "Q": 12, "K": 13, "A": 14}

with open("0054_poker.txt", "r") as f:
    content = f.read().splitlines()

for line in content:
    hands.append([[], []])
    cards = line.split()

    p1 = hands[-1][0]
    p2 = hands[-1][1]

    for card in cards[:5]:
        value = key[card[0]]
        suit = "SCHD".index(card[1])
        p1.append([value, suit])
    for card in cards[5:]:
        value = key[card[0]]
        suit = "SCHD".index(card[1])
        p2.append([value, suit])
    
    p1.sort()
    p2.sort()
    
    v1 = [*map(lambda x: x[0], p1)]
    v2 = [*map(lambda x: x[0], p2)]

    t1 = [*map(lambda x: x[1], p1)]
    t2 = [*map(lambda x: x[1], p2)]
    
    s1, mj_1 = calculate_score(v1, t1, 0)
    s2, mj_2 = calculate_score(v2, t2, 0)

    #print(s1, s2)

    if s1 > s2:
        ans += 1
    elif s1 == s2:
        if mj_1 == mj_2:
            if mj_1 == -1 and mj_2 == -1:
                for i in range(1,6):
                    if v1[-i] == v2[-i]: continue
                    mj_1 = v1[-i]
                    mj_2 = v2[-i]
                    break
            if mj_1 == -1:
                for i in range(1,6):
                    if v1[-i] == v2[-i]: continue
                    mj_1 = v1[-i]
                    break
            if mj_2 == -1:
                for i in range(1,6):
                    if v1[-i] == v2[-i]: continue
                    mj_2 = v2[-i]
                    break
        if s1 == 0 and s2 == 0:
            for i in range(1,6):
                if v1[-i] == v2[-i]: continue
                mj_1 = v1[-i]
                break
            for i in range(1,6):
                if v1[-i] == v2[-i]: continue
                mj_2 = v2[-i]
                break
        
        if mj_1 > mj_2:
            ans += 1
        elif mj_1 == mj_2:
            for i in range(1,6):
                if v1[-i] == v2[-i]: continue
                mj_1 = v1[-i]
                break
            for i in range(1,6):
                if v1[-i] == v2[-i]: continue
                mj_2 = v2[-i]
                break
            if mj_1 > mj_2:
                ans += 1


print(ans)
