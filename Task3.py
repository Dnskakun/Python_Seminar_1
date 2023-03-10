"""
Задача 6: Вы пользуетесь общественным транспортом? Вероятно, вы
расплачивались за проезд и получали билет с номером. Счастливым
билетом называют такой билет с шестизначным номером, где сумма
первых трех цифр равна сумме последних трех. Т.е. билет с номером
385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать
программу, которая проверяет счастливость билета.
385916 -> yes
123456 -> no
"""

number = int(input("Введите шестизначный номер билетика: "))
sumLeft = 0
sumRight = 0

if 99999 < number < 1000000:
    for i in range(3):
        sumLeft += number // 10 ** i % 10
        sumRight += number // 10 ** (i+3) % 10
    if sumLeft == sumRight: print("Вам попался счастливый билетик!!!")
    else: print("Вам попался обычный билетик!")
else: print("Номер билетика должен быть 6-ти значным!")



