from input import *

def create_contact():
    surname = input_surname()
    name = input_name()
    patronymic = input_patronymic()
    phone = input_phone()
    address = input_address()
    return f'{surname} {name} {patronymic} {phone}\n{address}\n\n'

def add_contact():
    contact = create_contact()
    with open('phonebook.txt', 'a', encoding='utf_8') as book:
        book.write(contact)
        book.close()

def read_book():
    with open('phonebook.txt','r',encoding='utf_8') as book:
        contacts_list = book.read().rstrip().split('\n\n')
        for contact in enumerate(contacts_list,1):
            print(f'\n',*contact)
    book.close()

def search_contact():
    print('Выберите вариант поиска:\n1) По фамилии\n2) По имени\n3) По отчеству\n4) По номеру телефона\n5) По адресу\n')
    var_search=-1
    while var_search not in ('1','2','3','4','5'):
        var_search=input()
        if var_search not in ('1','2','3','4','5'):
            print('Ошибка ввода. Попробуйте снова.')

    index_var = int(var_search)-1

    search=input('Введите данные для поиска: ').strip().lower()
    
    with open('phonebook.txt','r',encoding='utf_8') as book:
        contacts_list = book.read().rstrip().split('\n\n')
    for contact_str in contacts_list:
        contact_lst=contact_str.replace('\n', ' ').split()
        if search in contact_lst[index_var].strip().lower():
            print(f'\n{contact_str}')
    book.close()

def copy_contact():
    con_search=-1
    with open('phonebook.txt','r',encoding='utf_8') as book:
        ran=book.read().rstrip().split('\n\n')
    while int(con_search)>len(ran) or 0>=int(con_search):
        con_search=input('Введите порядковый номер, под которым хранится ваш контакт: ')
        if int(con_search)>len(ran) or 0>=int(con_search):
            print('Ошибка ввода. Попробуйте снова.')

    ind_var = int(con_search)-1

    with open('phonebook.txt','r',encoding='utf_8') as book:
        with open('phonebook_2.txt','a',encoding='utf_8') as book_2:
            sourse = book.read().rstrip().split('\n\n')
            book_2.write(f'{sourse[ind_var]}\n\n')
            
