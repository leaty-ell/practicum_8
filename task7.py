while True:
    user_input = input("Введите число: ")
    if user_input.isdigit():
        print(f"Введено целое число: {user_input}")
        break
    else:
        print("Ошибка. Попробуйте еще раз.")
