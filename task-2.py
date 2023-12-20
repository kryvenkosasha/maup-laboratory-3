def guess_number(first_digit):
    second_digit = 9
    third_digit = 9 - first_digit
    guessed_number = int(str(first_digit) + str(second_digit) + str(third_digit))
    return guessed_number

first_digit = int(input("Введите первую цифру числа: "))

guessed_number = guess_number(first_digit)
print(f"Отгаданное число: {guessed_number}")
