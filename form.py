def person_info():
    i=0
    person=['','','','','']
    while i<5:
        if i==0:
            person[i] = input('Введите фамилию: ')
        elif i==1:
            person[i] = input('Введите имя: ')
        elif i==2:
            person[i] = input('Введите отчество: ')
        elif i==3:
            person[i] = input('Введите номер абонента: ')
        elif i==4:
            person[i] = input('Введите описание контакта: ')
        i+=1
    return person

