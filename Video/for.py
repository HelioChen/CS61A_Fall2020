a = [[1, 2], [3, 4], [4, 4],[5, 5]]

cnt = 0
for x, y in a:
    if x == y:
        cnt += 1

print(cnt)

def sum(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total 

def sum_re(n):
    if n == 0:
        return 0
    else:
        return n + sum_re(n - 1)


