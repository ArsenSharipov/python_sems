n = int(input())
i = res = 0
for i in range(n):
    res = 2**i
    if(res<=n):
        print(res)
    i+=1