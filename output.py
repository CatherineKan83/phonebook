def search_output(ser):
    with open('phonebook.csv','r',encoding='utf_8') as book:
        check=0
        for line in book:
            if ser in line:
                print(line)
                check=1
            else: continue
        if check==0: 
            print('Указанного абонента не существует.')
        book.close()

def read_book():
    with open('phonebooktable.csv','r',encoding='utf_8') as book:
        for line in book:
            print(line)
        book.close()