n = int(input())
av = rev = 0
for i in range(n):
    x = int(input())
    if x == 1: av+=1
    if x == 0: rev+=1
if av>rev: print(rev)
else: print(av)