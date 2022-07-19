def get_date(date):
    day_list = ['первое', 'второе', 'третье', 'четвёртое',
                'пятое', 'шестое', 'седьмое', 'восьмое',
                'девятое', 'десятое', 'одиннадцатое', 'двенадцатое',
                'тринадцатое', 'четырнадцатое', 'пятнадцатое', 'шестнадцатое',
                'семнадцатое', 'восемнадцатое', 'девятнадцатое', 'двадцатое',
                'двадцать первое', 'двадцать второе', 'двадцать третье',
                'двадацать четвёртое', 'двадцать пятое', 'двадцать шестое',
                'двадцать седьмое', 'двадцать восьмое', 'двадцать девятое',
                'тридцатое', 'тридцать первое']
    month_list = ['января', 'февраля', 'марта', 'апреля', 'мая', 'июня',
                  'июля', 'августа', 'сентября', 'октября', 'ноября', 'декабря']
    date_list = date.split('.')
    return (day_list[int(date_list[0]) - 1] + ' ' +
            month_list[int(date_list[1]) - 1] + ' ' +
            date_list[2] + ' года')


def date_answers(name, date_in, date_true, flag='', min_date=-100000, max_date=100000):
    flag_result = True
    if flag == 'year':
        min_date, max_date = 0, 2022
    elif flag == 'month':
        min_date, max_date = 1, 12
    elif flag == 'day':
        min_date, max_date = 1, 31
    if date_in != date_true:
        if date_in < min_date or date_in > max_date:
            print('Ты ошибся. Такой даты  нет. Попробуй еще раз!')
        elif date_in < date_true:
            print(f'Ты ошибся. {name} родился позже. Попробуй еще раз!')
        else:
            print(f'Ты ошибся. {name} родился раньше. Попробуй еще раз!')
        flag_result = False
    return flag_result


def month_convert(answer_str_in):
    dict_month = {'январь': 1, 'февраль': 2, 'март': 3, 'апрель': 4, 'май': 5, 'июнь': 6,
                  'июль': 7, 'август': 8, 'сентябрь': 9, 'октябрь': 10, 'ноябрь': 11, 'декабрь': 12}
    digital_month = 0
    answer_str = answer_str_in.lower()
    if answer_str in dict_month:
        digital_month = dict_month[answer_str]
    return digital_month
