"""
Задача 2: Найдите сумму цифр трехзначного числа.
123 -> 6 (1 + 2 + 3)
100 -> 1 (1 + 0 + 0)
"""

number = int(input("Введите трехзначное положительное число: "))

if 99 < number < 1000:
    houndreds = number // 100
    tens = number // 10 % 10
    units = number % 10
    result = houndreds + tens + units
    print(f"{number} -> {result} ({houndreds} + {tens} + {units})")

else:
    print("Введено число, не удовлетворяющее условию!")

