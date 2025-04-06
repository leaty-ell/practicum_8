X = int(input())
current_sum = 0
for i in range(1, X + 1):
    current_sum += i
    print(" + ".join(map(str, range(1, i + 1))), "=", current_sum)
