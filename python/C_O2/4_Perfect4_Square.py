import math
start = 1000
end = 9999
results = []
for n in range(start, end + 1):
    root = int(math.isqrt(n))
    if root * root == n:
        digits = str(n)
        all_even = True
        for d in digits:
            if int(d) % 2 != 0:
                all_even = False
                break
        if all_even:
            results.append(n)
print("4-digit even-digit perfect squares:", results)
