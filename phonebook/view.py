def all_view():
    f = open('phonebook.csv', 'r', encoding = 'utf-8')
    navigator = ['Имя', 'Фамилия', 'Телефон', 'День рождения', 'Комментарий']
    print(navigator)
    print(*list(f))

