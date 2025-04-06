def perfect(num):
    if num < 2:
        return False
    sum_div = 1 
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            sum_div += i
            if i != num // i:  
                sum_div += num // i
    return sum_div == num

N = int(input("Введите число N: "))
print("Совершенные числа до", N, ":")

for num in range(2, N + 1):
    if perfect(num):
        print(num, end=" ")
