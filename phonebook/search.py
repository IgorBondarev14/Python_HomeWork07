def searching():
    f = open('phonebook.csv', 'r', encoding = 'utf-8')
    search_query = input('Введите поисковый запрос - ')
    print('Вот что нашлось:')
    print(*list(filter(lambda x: search_query in x, f)))
    
