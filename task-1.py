def square_number_ending_in_5(number):
    result = number // 10 * (number // 10 + 1)
    result = int(str(result) + "25")
    return result

num = int(input("Введите число, оканчивающееся на 5: "))

if num % 10 != 5:
    print("Ошибка: число не оканчивается на 5.")
else:
    result = square_number_ending_in_5(num)
    print(f"Результат возведения в квадрат: {result}")
