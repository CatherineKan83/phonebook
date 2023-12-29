from input import Input_data1
from input import Input_data2
from input import search
from form import person_info
from output import search_output
from output import read_book

def project():
        check=1
        while check ==1:
            print('Какое действие хотите совершить? \n1)Внести данные нового абонента\n2)Вывести телефонную книгу\n3)Найти абонента')
            decision = int(input())
            if decision==1:
                inp=person_info()
                Input_data1(inp)
                Input_data2(inp)
                print('Продолжить операции? \n1)Да      2)Нет')
                check = int(input())
                if check==1:
                    continue
                elif check==2:
                    exit()
                while 1>check or check>2: 
                    print('Ошибка ввода. Попробуйте снова.')
                    check = int(input())
            elif decision==2:
                print(read_book())
                print('Продолжить операции? \n1)Да      2)Нет')
                check = int(input())
                if check==1:
                    continue
                elif check==2:
                    exit()
                while 1>check or check>2: 
                    print('Ошибка ввода. Попробуйте снова.')
                    check = int(input())
            elif decision==3:
                s=search()
                search_output(s)
                print('Продолжить операции? \n1)Да      2)Нет')
                check = int(input())
                if check==1:
                    continue
                elif check==2:
                    exit()
                while 1>check or check>2: 
                    print('Ошибка ввода. Попробуйте снова.')
                    check = int(input())
            else: 
                print('Ошибка ввода. Попробуйте снова.')
        
            
        
