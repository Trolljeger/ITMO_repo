#Области видимости
#часть кода где имя переменной связано с объектом

# 1) встроенная Builin обоасть видимости
# 2) Глобальнная область видимости Global
# 3) Объемлющая Enclosed (nonlocal)
# 4) Локальная Local


a = 'hello' # global

def say_loudly(text):
    global a # обращение к глобальной переменной
    a = text.upper()
    # новый объект  ОВ - Enclosed
    # внешняя глобальная переменная "а" не меняется

    print(a)

    def say_alarm(alarm_text):
        #nonlocal a
        a = f'\x1b[31;1m{alarm_text}\x1b[0m' #local
        print(a)

    say_alarm(a)

print(a)
say_loudly(a)
print(a)

#say_alarm(a) живет внутри say_loudly
# вызвать из глобальной ОВ нельзя

# в локальной ОВ можно вывести глобальную переменную

#======================================================
#LEGB правило поиска переменной Local->Enclosed->Global->Builtin
#======================================================

# Фунция высшего порядка
# Функция которая принимает на вход или возвращает другую функцию

def save_data(save_func, data):
    save_func(data) # input function
    return print # return - function print

f = save_data(print, '\nHello')
f('Student')


# Замыкание
def create_html_tag(tag_word):
    open_tag = f'<{tag_word}>'
    close_tag = f'</{tag_word}>'

    # замыкание
    # обращается к свободным переменным
    def tag(text):
        print(f'{open_tag} {text} {close_tag}')

    return tag # возвр функцию

create_par = create_html_tag('p')
create_par('Hello world')

create_title = create_html_tag('title')
create_title('Hello world')


# декоратор
# способ модификации фунций (введение доп кода)

# функция декоратор
def add2body(tag):
    open_body = '<body>'
    close_body = '</body>'

    def wraper(text):
        print(open_body)
        tag(text)
        print(close_body)

    return wraper

@add2body # указание декоратора перед вызовом функции
def parag_html(text):
    print(f'<p>{text}</p>')

parag_html('hello')

import sys
print(sys.path)