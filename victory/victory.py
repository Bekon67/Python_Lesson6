# Викторина "Год рождения знаменитости"
#
# Джо́зеф Робине́тт Ба́йден-мла́дший (20 ноября 1942) президент США
# Ма́рио Дра́ги (3 сентября 1947) председатель совета министров Италии
# Хан Док Су (18 июня 1949) премьер-министр  Южной Кореи
# Наре́ндра Дамодарда́с Мо́ди (17 сентября 1950) премьер-министр Индии
# Влади́мир Влади́мирович Пу́тин (7 октября 1952) президент России
# Си Цзиньпи́н (15 июня 1953) председатель КНР
# Жаи́р Месси́ас Болсона́ру (21 марта 1955) президент Бразилии
# Фумио Кисида (29 июля 1957) премьер-министр Японии
# О́лаф Шольц (14 июня 1958) федеральный канцлер Германии
# Алекса́ндер Бо́рис де Пфе́ффель Джо́нсон (19 июня 1964) премьер-минимтр Великобритании
# Джа́стин Пьер Джеймс Трюдо́ (25 декабря 1971) премьер-министр Канады
# Эмманюэ́ль Жан-Мише́ль Фредери́к Макро́н (21 декабря 1977) президент Франции
#
#
# Даты вводятся в строковом типе, чтобы не было вылета программы
# функция перевода даты в текстовый формат с учётом склонения взята с https://ru.stackoverflow.com/

import random

from functions_victory import date_answers, month_convert, get_date

person_list = [
    {'position': 'президент США', 'name': 'Джозеф Робинетт Байден-младший', 'year': 1942, 'month': 11, 'day': 20},
    {'position': 'председатель совета министров Италии', 'name': 'Марио Драги ', 'year': 1947, 'month': 9, 'day': 3},
    {'position': 'премьер-министр  Южной Кореи', 'name': 'Хан Док Су', 'year': 1949, 'month': 6, 'day': 18},
    {'position': 'премьер-министр Индии', 'name': 'Нарендра Дамодардас Моди', 'year': 1950, 'month': 9, 'day': 17},
    {'position': 'президент России', 'name': 'Владимир Владимирович Путин', 'year': 1952, 'month': 10, 'day': 7},
    {'position': 'председатель КНР', 'name': 'Си Цзиньпин', 'year': 1953, 'month': 6, 'day': 15},
    {'position': 'президент Бразилии', 'name': 'Жаир Мессиас Болсонару', 'year': 1955, 'month': 3, 'day': 21},
    {'position': 'премьер-министр Японии', 'name': 'Фумио Кисида', 'year': 1957, 'month': 7, 'day': 29},
    {'position': 'федеральный канцлер Германии', 'name': 'Олаф Шольц', 'year': 1958, 'month': 6, 'day': 14},
    {'position': 'премьер-министр Великобритании', 'name': 'Александер Борис де Пфеффель Джонсон', 'year': 1964,
     'month': 4, 'day': 19},
    {'position': 'премьер-министр Канады', 'name': 'Джастин Пьер Джеймс Трюдо', 'year': 1971, 'month': 12, 'day': 25},
    {'position': 'президент Франции', 'name': 'Эмманюэль Жан-Мишель Фредерик Макрон', 'year': 1977, 'month': 12,
     'day': 21}]
dict_questions = {'year': 'Ты знаешь в каком году родился он родился?\n',
                  'month': 'Правильно! А какой месяц рождения?\n',
                  'day': 'Правильно! А какого числа?\n'}
number_leaders = 5

ans = input('Привет! Хочешь проверить, знаешь ли ты даты рождения руководителей'
            ' крупнейших экономик мира? (да/нет):\n')
while ans == 'да':
    counter = 0
    quiz = random.sample(person_list, number_leaders)
    for i in range(number_leaders):
        flag_mistake = False
        print(f'Тебе достался {quiz[i]["position"]} {quiz[i]["name"]}...')
        for key in dict_questions:
            answer = input(f'{dict_questions[key]}')
            flag_answer = False
            while not flag_answer:
                if key == 'month':
                    while month_convert(answer) == 0:
                        answer = input('Такого названия месяца не существует. Повтори, пожалуйста:\n')
                    answer = month_convert(answer)
                else:
                    while not answer.isdigit():
                        answer = input('Введи, пожалуйста, число:\n')
                if date_answers(quiz[i]["name"], int(answer), quiz[i][key], key) is True:
                    break
                flag_mistake = True
                answer = input()
        if flag_mistake:
            counter += 1
        born_date = '.'.join([str(quiz[i]["day"]),
                              str(quiz[i]["month"]),
                              str(quiz[i]["year"])])
        print('Bерно,', 'ты ответил без ошибок' * (not flag_mistake))
        print(f'{get_date(born_date)} - в этот день родился {quiz[i]["position"]} {quiz[i]["name"]}\n')

    print(f'Ты ответил правильно на {number_leaders - counter} вопроса')
    print(f'Ты ответил неправильно на {counter} вопроса')
    print(f'Ты ответил правильно на {(number_leaders - counter) / number_leaders * 100}% вопросов')
    print(f'Ты ответил неправильно на {counter / number_leaders * 100}% вопросов')
    ans = input('Хочешь сыграть еще?\n')
print('До свидания!')
