from logger import *
def interface():
    with open('phonebook.txt', 'a'):
        pass
        command = -1
    while command !=5:
        print('Доступные команды: \n1)Внести данные нового абонента\n2)Вывести телефонную книгу\n3)Найти абонента\n4)Скопировать данные абонента\n5)Закрыть телефонную книгу\n')
        while command not in ('1','2','3','4','5'):
            command=input('Введите номер действия:')    
            if command not in ('1','2','3','4','5'):
                print('Ошибка ввода. Попробуйте снова.')

        match command:
            case '1':
                add_contact()
            case '2':
                read_book()
            case '3':
                search_contact()
            case '4':
                copy_contact()
            case '5':
                print('Хорошего дня!')
                exit()
        command = -1