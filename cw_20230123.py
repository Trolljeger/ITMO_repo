#СТРОКИ
# строка неизменяемый объект
# задается чекрез кавычки. одинарные или двойные
# лучше использовать один тип во всем коде
a1 = 'Hello'
a2 = "Hello"
# Dmitry's наличие апострофа
# через экранирование символа обратным слэшем
# или двойные кавычки
b1 = 'Dmitry\'s'
b2 = "Dmitry's"

# вывод символа по коду UNICODE
print('\x41')
# преобразование числа к коду символа
print(chr(65))

# создание блочных строк
# возможность создания большого комментария
str1  = """ A
B
C
"""
print(str1)

# длина строки
print(len("Dmitry"))

# конкатенация строк (объединение)
print("Hello" + "world")
# если строки в переменных то сумма это новая переменная (объект)

# умножение строк на число
print("Hello"*3)

# проверка наличия подстрока в строке
print('ell' in 'Hello') # true or false

a = "Dmitry"
print(a[0]) # прямая индексация первый элемент
print(a[-1]) # обратная индексация последний элемент
b = a[1:5] # заданы обе границы
c = a[:5] # от начала до 5 не включая верх
d = a[2:] # от 2 до конца строки
e = a[::2] # вся строка, третий параметр шаг взятия элементов
print(c, b , d, e) # срез верхняя граница не включается

# преобразование в строку
ss = str(2.55)
print(ss, len(ss))

# преобразование из строки
print(float("2.2"))

# полный перечень методов строк
print(dir(str))
# lstrip удаляет пробелы в начале строки
f = '    gggggg'
print(f.lstrip())

# split('sym') разбиение строк по определенному символу
ff = "sss,sssf,gaggvr,rghqbh"
print(ff.split(","))

# объединение строк через символ
fff = ':'.join(['Hello', 'world'])
print(fff)

#форматные строки
name = 'Ann'
res = f'Hello, {name}'
print(res)
print('Hello, %s' % name)

#=====================================
# БАЙТОВЫЕ СТРОКИ И МАССИВЫ БАЙТОВ
#=====================================
# каждый символ - байт 0-255
h = b'Hello'
print(h[0]) # 72 - содержание первого байта в строке


# СПИСКИ
#=========================================
# Изменяемый, упорядоченный тип данных
l = []
# явное определение
l = [1, 2, 'Dmitry', 'ggg', 2.6]
print(l)
# list
l = list('Hello') # строка это список буквенных литералов
print(l)
print(l[-2]) # второй элемент с конца
print(l[:4:2]) # срез списка с шагом

# объединение списков
k = [0, 'work']
print(l + k)

# умножение на число
kk = k*2
print(kk)

# append добавление в список в конец
k.append('is good')
print(k)

# замена элементов в срезе
l1 = list("qwertyqwerty")
l1[3:6] = [1, 2, 3]
print(l1)

l2 = [1, 2, 3, 4]
l3 = [l2, 66]
print(l2)
l3[0] = 88
print(b)

#++++++++++++++++++++++++++++
#КОРТЕЖ

# неизменяемый список
c = ()
print(type(c))
c = ("hh", 7)
print(c)
c1 = tuple()
c1 = 1, 3, 'hh' # упаковка
print(c1)

# распаковка
d1, e1, f1 = c1
print(d1)
print(e1)
print(f1)


# МНОЖЕСТВО
# коллекция уникальных элементов

m1 = {1, 2, 3}
m2 = {2, 3, 4}
print(m1 & m2) # пересечение
print(m1 | m2) # объединение
print(m1 - m2) # разница (остаток первого множества без пересечения)
print(m1 ^ m2) # отличия

# СЛОВАРЬ
# Хранение элементов по ключам

ddd = {'key1': 'val1', 'key2' : 135}
print(ddd)

# создание словаря с определенными ключами и значениями по умолчанию
ddd = dict.fromkeys(['a', 'b', 'c'], 0)
print(ddd)
print(ddd.get('b'))

ddd['c'] += 5 # изменение значение словаря по ключу
print(ddd)












