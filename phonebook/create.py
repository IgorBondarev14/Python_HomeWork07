def create_new_record():
    new_record = []
    data = open('phonebook.csv', 'a', encoding = 'utf-8') 
    print('Введите имя: ')
    new_record.append(input())
    print('Введите фамилию: ')
    new_record.append(input())
    print('Введите телефон: ')
    new_record.append(input())
    print('Введите день рождения: ')
    new_record.append(input())
    print('Введите комментарий: ')
    new_record.append(input())
    new_record = str(new_record)
    data.write(new_record)
    data.write('\n')
    data.close()
