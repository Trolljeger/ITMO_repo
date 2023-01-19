a = 1
b = 2
c = a + b
print(c)

print(type(1))  # вывод типа переменнной type(name)
print((1).__sizeof__())  # вывод размера переменной (name).__sizeof__()
print(dir(a))  # вывод списка атрибутов переменной dir(name)
print(id(a))  # вывод идентификатора переменной id(name)

# операции над  числами
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b)
print(4 % 3)

# побитовые операции
print("\n")
print(1 & 2)  # и
print(2 | 1)  # или
print(2 << 1)  # смещение влево
print(2 >> 1)  # смещение вправо
print(0b00110)  # запись в бинарном формате

# операторы сравнения
print("\n")
print(2 > 1)  # результат операции типа bool (true/false)
print(1 > 2)

# логические опреаторы
print("\n")
print(a < 1000 and a > 5)  # and
print(a < 1000 or a > 5)  # or
print(not a < 1000)  # инверсия результата

# комплекные числа
print("\n")
cn = 1 + 2j
print(type(cn))  # комплексное число
print(cn.imag)
print(cn.real)

# числа  плавающей точкой
print("\n")
print(0.1 + 0.1 - 0.2)

# для точных вычислений
import decimal

a = decimal.Decimal(0.1)
b = decimal.Decimal(0.2)
print(a + a - b)
