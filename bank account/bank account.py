"""
Программа "Личный счет"
Описание работы программы:
Пользователь запускает программу у него на счету 0
Программа предлагает следующие варианты действий
1. пополнить счет
2. покупка
3. история покупок
4. выход
1. пополнение счета
при выборе этого пункта пользователю предлагается ввести сумму на сколько пополнить счет
после того как пользователь вводит сумму она добавляется к счету
снова попадаем в основное меню
2. покупка
при выборе этого пункта пользователю предлагается ввести сумму покупки
если она больше количества денег на счете, то сообщаем что денег не хватает и переходим в основное меню
если денег достаточно предлагаем пользователю ввести название покупки, например (еда)
снимаем деньги со счета
сохраняем покупку в историю
выходим в основное меню
3. история покупок
выводим историю покупок пользователя (название и сумму)
возвращаемся в основное меню
4. выход
выход из программы
При выполнении задания можно пользоваться любыми средствами
Для реализации основного меню можно использовать пример ниже или написать свой
"""
import datetime

current_date_time = datetime.datetime.now()

balance = 0
history = []

while True:
    print('1. пополнение счета')
    print('2. покупка')
    print('3. история покупок')
    print('4. выход')

    sum_transaction = 0
    tran_in = 'Пополнение'
    choice = input('Выберите пункт меню: ')
    if choice == '1':
        sum_transaction = int(input('Введите сумму пополнения счета: '))
        balance += sum_transaction
        history.append([current_date_time, 1, sum_transaction, 'Поступление'])
        continue

    elif choice == '2':
        sum_transaction = int(input('Введите сумму покупки: '))
        if sum_transaction <= balance:
            expenditure_item = input('Введите статью расходов: ')
            balance -= sum_transaction
            history.append([current_date_time, 2, -sum_transaction, expenditure_item])
        else:
            print(f'У Вас недостаточно средств. Остаток {balance}')
        continue

    elif choice == '3':
        for i in range(len(history)):
            print(*history[i])
            print(f'Остаток на счету: {balance}')
        continue

    elif choice == '4':
        break
    else:
        print('Неверный пункт меню')
