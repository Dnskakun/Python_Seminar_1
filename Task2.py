"""
Задача 4: Петя, Катя и Сережа делают из бумаги журавликов. Вместе
они сделали S журавликов. Сколько журавликов сделал каждый
ребенок, если известно, что Петя и Сережа сделали одинаковое
количество журавликов, а Катя сделала в два раза больше журавликов,
чем Петя и Сережа вместе?
"""

volume = int(input("Введите общее количество сделанных журавликов (кратное 6-ти): "))

if volume % 6 == 0:
    x = volume // 6
    print("Количество журавлей, сделанных детьми:")
    print(f"Петя сделал - {x}, Катя сделала - {x * 4}, Сережа сделал - {x}.")
else:
    print("Введено число, не кратное 6.")


