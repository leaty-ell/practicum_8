for n in range(1, 10):
    number = ""
    for i in range(1, n + 1):
        number += str(i)
    result = int(number) * 8 + n
    print(f"{number} * 8 + {n} = {result}")
print()

for n in range(1, 10):
    number = ""
    for i in range(1, n + 1):
        number += str(i)
    result = int(number) * 9 + (n + 1)
    print(f"{number} * 9 + {n + 1} = {result}")
print() 

for n in range(1, 10):
    number = "1" * n
    result = int(number) * int(number)
    print(f"{number} * {number} = {result}")
