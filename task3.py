total_income = 0
citizen_count = 0
while True:
    income = int(input())
    if income == 0:
        break
    total_income += income
    citizen_count += 1
average_income = total_income / citizen_count if citizen_count != 0 else 0
print(average_income)
