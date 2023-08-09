n = int(input())
m = int(input())
print(n, m)
N = set()
M = set()
for i in range(n):
    N.add(int(input()))
for i in range(m):
    M.add(int(input()))
print(N)
print(M)
print(sorted(N.intersection(M)))