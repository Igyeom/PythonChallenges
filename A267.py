n = int(input())
l = [*map(int,input().split())]
target = int(input())

lo = 0
hi = n-1

while lo <= hi:
	mid = (lo+hi)//2
	if l[mid] == target:
		print(mid)
		break
	if l[mid] > target:
		hi = mid-1
		continue
	if l[mid] < target:
		lo = mid+1
		continue
else:
	l.sort()
	while lo <= hi:
		mid = (lo+hi)//2
		if l[mid] == target:
			print(mid)
			break
		if l[mid] > target:
			hi = mid-1
			continue
		if l[mid] < target:
			lo = mid+1
			continue
	else:
		print(-1)
