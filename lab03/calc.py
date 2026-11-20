a = float(input("Первое число: "))
b = float(input("Второе число: "))
print(f"Cложение: {a + b}")
print(f"Вычитание: {a - b}")
print(f"Умножение: {a * b}")

if b == 0:
   print('деление на 0')
else:
   print(f"Деление: {a / b}")