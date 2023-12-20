days = [3, 4, 7, 8, 10, 11, 14, 15, 18, 19, 22, 23, 26, 27, 30, 31]

even_days = [day for day in days if day % 2 == 0]
odd_days = [day for day in days if day % 2 != 0]

print("Четные дни:")
for day in even_days:
    print(day, end=" ")
print()

print("Нечетные дни:")
for day in odd_days:
    print(day, end=" ")
print()

count_threes = len(odd_days)
count_fours = len(even_days)

print(f"\nКоличество троек: {count_threes}")
print(f"Количество четверок: {count_fours}")

if count_fours >= count_threes:
    print("Вася может рассчитывать на оценку 4.")
else:
    print("Вася не может рассчитывать на оценку 4.")
