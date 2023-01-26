#===============================
#========= Циклы ===============
#===============================

#while
i = 0
while i < 10:
    print(i)
    i += 1


l1 = [1, 3, 5, 7, 9]
i = 0
while i < len(l1):
    print(l1[i])
    i += 1

# принудительный выход
i = 0
while i < 10:
    if i > 5:
        break
    print(i)
    i += 1

# comtinue
i = 0
while i < 10:
    if i < 5:
        i += 1
        continue
    else:
        print(i)
        i += 1

# elipsys ... ничего не делать
i = 0
while i < 10:
    if i > 5:
        i+=1
        ...
    else:
        print(i)
        i += 1

#i = 0
#while i < 3:
#    answ = input ('Write passwd: ')
#    if answ == 'qwerty':
#        print('ok')
#        break
#    else:
#        print('Try again')
#    i += 1
#else: # к else
#    print('Attemtps are finished')


# for
for i in 'Hello':
    print(i)

for item in l1:
    print(item)
# задание диапазона значений
for i in range(0, 7):
    print(i)

str1 = 'abcdefg'
for i in str1[1::2]:
    print(i)

# словари
a = {'a':1, 'b':2}
for i in a:
    print(i) # выводит только ключи

for v in a.values():
    print(v) # вывод значения без ключа

# список из  кортежей
a = [(1, 2, 3, 4), (5, 6, 7, 8)]
for (i, j, k, l) in a:
    print(i, j, k, l)

# все что не входит в i и l упаковыввоется в список k через *
for (i, *k, l) in a:
    print(i, k, l)

l2 = [1, 3, 5, 7, 9]
l3 = []
for i in l2:
    l3.append(i**2)
print(l3)

#цикл можно заменить
# цикл прямо в определении списка
l3 = []
l3 = [i ** 2 for i in l2]
print(l3)

l4 = [el*2 for el in 'qwerty']
print(l4)

# заполнение массива в цикле с условием
# квадраты значений в диапазоне, только для нечеиных  сичел
# одинарное условие пишется после цикла
l5 = [i**2 for i in range(0, 10) if i % 2]
print(l5)

# двойное условие с else пишется перед циклом
l5 = [i**2 if i % 2 else i for i in range(0,10)]
print(l5)

ai = iter(l5)
for i in range(len(l5)):
    print(next(ai))
    i += 1

dict1 = {'a':1, 'b':2}
di = iter(dict1)
print(next(di))
print(next(di))
# print(next(di)) третий  вызов даст StopIteration исключение



#ФУНКЦИИ
# Задача скрытия реализации и исключение повторяющегося кода
# декомпозиция

def calc(par1, par2, par3):
    print(par1, par2, par3) # обработка
    return list[par1, par2, par3] # можно определить выходные данные

print(calc(1,2,3))

def say(phraze, name1 = 'Ann', name2 = 'Dima'):
    print(phraze, name1, name2)

say('Hello')
say('Hello', 'Tom')
say('Hello', name2='Tom')

# упаковка аргументов функции
# вызов через *
params = ['Hello', 'Ann', 'Tom']
say(*params)

#в случае словаря ключи должны повторять имена входных параметров функции
# вызов через **
params = {'phraze':'Hello', 'name1':'Ann', 'name2':'Tom'}
say(**params)


# файлы
# name, mode
fd = open(r'test', 'r')
print(fd.read())
fd.close()