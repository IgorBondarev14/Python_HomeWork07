from create import create_new_record
from search import searching
from view import all_view

k = 1

def choice_start():  
    print('Для начала работы выберите пункт меню:\n\
1. Создать контакт\n2. Найти контакт\n3. Просмотреть все контакты')
    choice = 0
    while choice < 1 or choice > 3:
        choice = int(input('Введите номер пункта меню: '))
    if choice == 1:
        create_new_record()
    elif choice == 2:
        searching() 
    else:
        all_view()

while k == 1:
    choice_start()
    k = int(input('Если хотите продолжить работу - нажмите 1,\nДля остановки - нажмите 0\n'))

print("Работа завершена. До свиданья")


