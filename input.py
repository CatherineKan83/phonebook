def Input_data1(person_info):
    with open('phonebook.csv', 'a', encoding='utf_8') as book:
        book.write(f'\nФамилия: {person_info[0]}, имя: {person_info[1]}, отчество: {person_info[2]}, номер абонента: {person_info[3]}, описание контакта: {person_info[4]}')
        book.close()
def Input_data2(person_info):
    with open('phonebooktable.csv', 'a', encoding='utf_8') as book:
        i=0
        while i<5:
            if i==0:
                book.write(f'Фамилия: {person_info[i]} \n')
                i+=1
            elif i==1:
                book.write(f'Имя: {person_info[i]} \n')
                i+=1
            elif i==2:
                book.write(f'Отчество: {person_info[i]} \n')
                i+=1
            elif i==3:
                book.write(f'Номер абонента: {person_info[i]} \n')
                i+=1
            elif i==4:
                book.write(f'Описание контакта: {person_info[i]} \n \n')
                i+=1
        book.close()
def search():
    ser=input('Введите фамилию, имя, отчество или номер для поиска контакта: ')
    return ser

