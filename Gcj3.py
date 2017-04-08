from sortedcontainers import SortedDict
def divide(n):
    return int((n-1)/2), int(n/2)

def ans(n, k):
    m = SortedDict()
    m[n] = 1
    bg = None
    while k > 0:
        bg, slots = m.popitem()
        k -= slots
        x, y = divide(bg)
        m[x] = m[x]+slots if x in m else slots
        m[y] = m[y]+slots if y in m else slots

    return ' '.join([str(x) for x in reversed(sorted(split(bg)))])


T = int(input())
for i in range(T):
    N, K = [int(x) for x in raw_input().split()]
    print"Case #" + str(i+1) + ":", ans(N, K)