n = int(input())
b = list(int(input()) for i in range(n))
bush = int(input())
res = 0
if bush == 1:
    res = b[0] + b[1] + b[-1]
elif bush == n:
    res = b[-2] + b[-1] + b[0]
else:
    res = b[bush-1] + b[bush-2] + b[bush]
print(res)