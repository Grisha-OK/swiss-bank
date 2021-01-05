import random  #Добавляем модуль random
import json    #Добавляем модуль json

#пишет меню
def menu_show():
    '''
    Выводит подсказку по меню
    '''
    menu_view = ['1 - Вывести данные по счету', '2 - Вывести все счета', '3 - Провести операцию со счетом',
    '4 - Добавить пользователя', '5 - Удалить пользователя по номеру счета','6 - Выход', '----------------------------------------']                                                
    for i in range (0, 7): #для каждой i в диапазоне (0, 7)
        print (menu_view[i])
    
#взаимодействие с меню
def specific_user_output():   #вывод конкретного пользователя_1
    '''
    при введении числа 1 вывод конкретного пользователя _1_
    '''
    print ('Ведите номер счета')
    o = input()   # o присваивается введённый текст
    for q in data_base:   #перебрать элементы списка data_base, q = один из элементов списка
        if q['account_number'] == int(o):   #проверяем номер счета ведёный в консоль
               print('Фамилия:       ', q['surname'])
               print('Имя:           ', q['name'])
               print('Дата рождения: ', q['date_of_birth'])
               print('Баланс счета:  ', q['account_balance'])
               print('Номер счета:   ', q['account_number'])

def all_user_output():    #вывод всех пользователя_2
    '''
    при введении числа 2 вывод всех пользователя _2_
    '''
    for q in data_base:   #для каждой q из списка data_base (дословный перевод)
        print (q['surname'], '|',
               q['name'], '|',
               q['date_of_birth'], '|',
               q['account_balance'], '|',
               q['account_number'])

def conduct_an_operation_with_an_account():  #провести операцию со счетом_3
    '''
    при введении числа 3 провести операцию со счетом _3_
    '''    
    print ('Ведите номер счета')
    y = input() #пьросим ползователя вести номер счета
    print ('Ведите сумму')
    x = input() #просим пользователя вести сумму
    for q in data_base: #перебрать элементы списка data_base, q = один из элементов списка
        if q['account_number'] == int(y): #роверяем номер счета ведёный в консоль
            q['account_balance'] = q['account_balance'] + float(x) #выполняем математическую операцыю
            print ('Операцыя выполнена')

def add_new_user():  #добавить нового пользователя_4
    '''
    при введении числа 4 добавить нового пользователя _4_
    '''    
    print('Ведите фамилию')
    s = input()
    print('Ведите имя')
    n = input()
    print('Ведите дату рождения')
    d = input()
    print ('Пользователь создан')
    u = (account_prefix * 10000 + random.randint(1, 9999))
    data_base.append({'surname': s, #Добавляем элемент в список
          'name': n,
          'date_of_birth': d,                                                    
          'account_balance': 0.00,
          'account_number': u}) #Объединяем число 4457 с рандомным числом
    print(u)

def delete_user(): #удалить пользователя_5
    '''
    при введении числа 5 удолить пользователя _5_
    '''    
    del_index = None
    print ('Ведите номер счета для удаления')
    f = input()
    for i in range(len(data_base)): #для каждой i в диапазоне, длина (data_base), i = порядковому номеру
        q = data_base[i]            #приравневаем q к отдельно взятым элементам, как в конструкции < for q in data_base: >
        if q['account_number'] == int(f):
            del_index = i
    if del_index != None:   
        del data_base[del_index]
        print("Пользователь удалён")
    else:
        print("Пользователь не найден")

def exit_the_program(): #выход_6
    '''
    при введении числа 6 выйти из программы _6_
    '''    
    with open("data_base_file.json", "w") as write_file: #Открываем файл в режиме записи
        json.dump(data_base, write_file)  #Конвертирует данные из переменной data в строку json и записывает в файл

    print ('Выход выполнен')
    exit(0)

def debugger(): #отлодчик_666
    '''
    при введении числа 666 выводиться заготовленные действия из функции отладчика _666_
    '''    
    print("you entered debug mode")
    print(" ")
    print(" ")
    print(data_base)

data_base = []             #переменная хранящая данные из файла и не добавленные в файл

try:                                                     #если произойдёт исключение выполнится except
    with open("data_base_file.json", "r") as write_file: #фаил открыт только в конструкции with open
        variable_with_read = write_file.read()           #Читает строку из файла
        data_base = json.loads(variable_with_read)       #Преобразует строку в python объект.
except FileNotFoundError:                                #выполнется если произойдёт ошибка в try
    print("Создаю новую базу")

account_prefix = 4457

menu_show()

menu_program = ''
while menu_program != '6': #до тех пор пока выполняется условие (в данном случаи menu_program НЕ РАВНО 6)
    menu_program = input()
    
    if menu_program == '1':    #если выполняется условие...
        specific_user_output() #то вызывается функция вывода конкретного пользователя
        
    elif menu_program == '2':  #иначе, если не одно из условий if или (elif) не выполнено...
         all_user_output()     #то вызывается функция вывода всех пользователей
         
    elif menu_program == '3':  #иначе, если не одно из условий if или (elif) не выполнено...
        conduct_an_operation_with_an_account() #то вызывается функция проведения операции со счетом 

    elif menu_program == '4':  #иначе, если не одно из условий if или (elif) не выполнено...
       add_new_user()          #то вызывается функция добавления нового пользователя

    elif menu_program == '5':  #иначе, если не одно из условий if или (elif) не выполнено...
        delete_user()          #то вызывается функция удоления пользователя
  
    elif menu_program == '6':  #иначе, если не одно из условий if или (elif) не выполнено...
        exit_the_program()     #то вызывается функцию выхода

    elif menu_program == '666':#иначе, если не одно из условий if или (elif) не выполнено...
        debugger()             #то вызывается за резервирования функция под отладку.
    
    else:
        menu_show()
