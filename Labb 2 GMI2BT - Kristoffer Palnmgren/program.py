import module

def menu():
    print("\n 1. Läs in orginalfil \n 2. Visa json-data \n 3. Lägg till person \n 4. Ta bort person \n 5. Spara fil \n 6. Avsluta")
    answer = input()
    while True:
        if answer == '1':
            module.ReadCsv('personer.csv')
            print('File Loaded!')
            menu()
        elif answer == '2':
            module.ReadJson('personer.json')
            menu()
        elif answer == '3':
            module.ReadJson('personer.json')
            module.AddPerson()
            module.ToJson('personer.json')
            menu()
        elif answer == '4':
            module.ReadJson('personer.json')
            module.RemovePerson()
            module.ToJson('personer.json')
            menu()
        elif answer == '5':
            print('File Saved!')
            module.ToJson('personer.json')
            menu()
        else:
            print('Exiting')
        break


menu()
