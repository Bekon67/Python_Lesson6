# Планирую все делать через функции и модули, размещая их в папках рл направлениям
import os
import subprocess
from platform import node

while True:
    print('1. создать папку')
    print('2. удалить папку')
    print('3. Удалить файл')
    print('4. копировать(файл / папку)')
    print('5. просмотр содержимого рабочей директории')
    print('6. посмотреть только папки')
    print('7. посмотреть только файлы')
    print('8. просмотр информации об операционной системе')
    print('9. создатель программы')
    print('10. играть в викторину')
    print('11. мой банковский счет')
    print('12. смена рабочей директории(*необязательный пункт)')
    print('13. выход')

    choice = input('Выберите пункт меню: ')
    if choice == '1':
        print('Ваша текущая директория:', os.getcwd())
        while True:
            name_dir = input('Введите наименование создаваемой папки: ')
            if os.path.exists(name_dir):
                print('Папка с таким именем уже существует')
            else:
                os.mkdir(name_dir)
                break

    elif choice == '2':
        print('Ваша текущая директория:', os.getcwd())
        name_dir = input('Введите наименование удаляемой  папки: ')
        if os.path.exists(name_dir):
            os.rmdir(name_dir)
        else:
            print('Папки с таким именем не существует')

    elif choice == '3':
        print('Ваша текущая директория:', os.getcwd())
        name_file = input('Введите наименование удаляемого  файла: ')
        if os.path.exists(name_file):
            os.remove(name_file)
        else:
            print('Файла с таким именем не существует')

    elif choice == '4':
        print('Ваша текущая директория:', os.getcwd())
        name_file_old = input('Введите наименование копируемого  файла/папки: ')
        if os.path.exists(name_file_old):
            while True:
                name_file_new = input('Введите наименование нового  файла/папки: ')
                if os.path.exists(name_file_new):
                    print('Папка/файл  с таким именем уже существует')
                else:
                    os.rename(name_file_old, name_file_new)
                    break
        else:
            print('Файла с таким именем не существует')

    elif choice == '5':
        print('Ваша текущая директория:', os.getcwd())
        print('Содержимое Вашей директории:', os.listdir(), sep='\n')

    elif choice == '6':
        print('Ваша текущая директория:', os.getcwd())
        folders = []
        for e in os.listdir():
            if os.path.isdir(e):
                folders.append(e)
        print('Папки внутри Вашей директории:', folders, sep='\n')
    elif choice == '7':
        print('Ваша текущая директория:', os.getcwd())
        files = []
        for e in os.listdir():
            if os.path.isfile(e):
                files.append(e)
        print('Файлы внутри Вашей директории:', files, sep='\n')
    elif choice == '8':
        print(os.name)
        print(node())
        # https://codeby.net/threads/poluchaem-informaciju-o-sisteme-s-pomoschju-python-chast-1.79797/
    elif choice == '9':
        print('Автор Константин Бейлин')
    elif choice == '10':
        subprocess.call("D:/Neural_university/Python/Python_Lesson5/victory/victory.py", shell=True)
    elif choice == '11':
        subprocess.call("D:/Neural_university/Python/Python_Lesson5/bank account/bank account.py", shell=True)
    elif choice == '12':
        print('Ваша текущая директория:', os.getcwd())
        folders = []
        for e in os.listdir():
            if os.path.isdir(e):
                folders.append(e)
        print('Папки внутри Вашей директории:', folders, sep='\n')
        name_file = input('Введите  путь к папке, куда Вы хотите перейти:\n ')
        if os.path.exists(name_file):
            os.chdir(name_file)
            print("Новая директория:", os.getcwd())
        else:
            print('Директории с таким именем не существует')
    elif choice == '13':
        exit()
    else:
        print('Неверный пункт меню')
