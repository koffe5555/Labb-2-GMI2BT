import json

dictionary = [] 

#ReadCsv öppnar upp csv fieln och lägger in i listor. Meny val: 1

def ReadCsv(filename): 
    global dictionary
    container = []
    try:
        with open(filename, encoding='utf-8') as f_obj:
            for line in f_obj:
                container.append(line)
        for line in container:
            info = line.rstrip('\n').split(';')
            dictionary.append({'Name:': info[0], 'Ename:': info[1], 'Username:': info[2], 'Email:': info[3]})
    except FileNotFoundError as error:
        print(error)

#Converterar vår lista med dictionarys till json Meny val: 5

def ToJson(filename):
    global dictionary
    try:
        with open(filename, "w", encoding="utf-8") as jf_dump:
            json.dump(dictionary, jf_dump, ensure_ascii=False, indent=4)
    except FileNotFoundError as error:
        print(error)

#Visar json filens innehåll, Meny val: 2

def ReadJson(filename):
    global dictionary
    with open(filename, "r", encoding="utf-8") as rj_obj:
        dictionary = json.load(rj_obj)
        for i in dictionary:
            print(i)

#Lägger till en person i våran lista, Meny val: 3

def AddPerson():
    global dictionary
    try:
        name = input('Enter firstname: ')
        ename = input('Enter Lastname: ')
        username = input('Enter Username:')
        mail = input('Enter Email: ')
        dictionary.append({
            'Name:': name,
            'Ename:': ename,
            'Username:': username,
            'Email:': mail
            })
    except ValueError as error:
        print(error)
        
#Tarbort person ur våran lista, Meny val: 4

def RemovePerson():
    global dictionary
    try:
        remove = input('Enter username to delete: ')
        info = 0
        for line in dictionary:
            if remove == line['Username:']:
                dictionary.pop(info)
            info += 1
    except ValueError as error:
        print(error)

