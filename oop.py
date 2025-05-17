import json

def display_list(options):
    for key, value in options.items():
        print(f"{key}: {value}")

def get_data(json_file):
    while True:
        id_found = False
        id = input('id: ')
        with open(json_file, 'r')as file:
            content = json.load(file)
        for person in content:
            if id == person['id']:
                id_found = True
        if not id.replace(" ", "").isdigit():
            print('it should be a number')
        elif id_found:
            print('already taken')
        else:
            while True:
                name = input('name: ')
                if name.replace(" ", "").isalpha():
                    while True:
                        age = input('age: ')
                        if age.replace(" ", "").isdigit():
                            entry = {
                                "id": id,
                                "name": name,
                                "age": age,
                            }
                            return entry
                        else:
                            print('digit only')
                else:
                    print('alpha only')
        
def add_entry(json_file):
    with open(json_file, 'r')as file:
        content = file.read()
    data = []
    new_entry = False
    if not content:
        with open(json_file, 'w')as file: 
            json.dump(data, file, indent=4)
    else:
        new_entry = True
    
    get_entry = get_data(json_file)
    with open(json_file, 'r')as file:
        content2 = json.load(file)
    content2.append(get_entry)
    with open(json_file, 'w')as file:
        json.dump(content2, file, indent=4)
    if not new_entry:
        print('first entry was successfully saved')   
    else:
        print('new entry was successfully saved') 

def find_entry(json_file):
    try:
        with open(json_file, 'r')as file:
            content = json.load(file)
        count = 0
        option = input('press 1 to find entry | press 2 to display all entries: ')
        if option == '1':
            ask = input('enter id or name: ')
            if ask.replace(" ", "").isdigit():
                for person in content:
                    if person['id'] == ask or person['name'] == ask:
                        print()
                        print(f"id: {person['id']}")
                        print(f"name: {person['name']}")
                        print(f"age: {person['age']}")
                        print()
                        count += 1
                if count == 1:
                    print(f'{count} person found')
                elif count == 0:
                    print('not found')
                else:
                    print(f'{count} people found')
            else:
                print('digit only')
        elif option == '2':
            for value in content:
                print(value)
    except json.decoder.JSONDecodeError:
        print('no entry in database yet')
            
def delete_entry(json_file):
    try:
        with open(json_file, 'r')as file:
            content = json.load(file)
        option = input('press 1 to delete a person | press 2 to delete everything: ')
        if option == '1':
            new_list = []
            deleted = False
            ask = input('enter id or name: ')
            for person in content:
                if ask != person['id'] and ask != person['name']:
                    new_list.append(person)
                    with open(json_file, 'w')as file:
                        json.dump(new_list, file, indent=4)
                else:
                    deleted = True
            if deleted:
                print('deleted successfully')
            else:
                print('id not existing')
        elif option == '2':
            
            with open(json_file, 'w')as file:
                file.write("")
                print('everything has been deleted')
    except json.decoder.JSONDecodeError:
        print('no entry in database yet')

def edit_entry(json_file):
    try:
        with open(json_file, 'r')as file:
            content = json.load(file)
        found = False
        ask = input('enter id: ')
        for person in content:
            if ask == person['id']:
                name = input('name: ')
                if name.replace(" ", "").isalpha():
                        age = input('age: ')
                        if age.replace(" ", "").isdigit():
                            if name == person['name'] and age == person['age']:
                                print('nothing changed')
                            else:
                                person['name'] = name
                                person['age'] = age
                                found = True
                        else:
                            print('digit only')
                else:
                    print('alpha only')
        if found:
            with open(json_file, 'w')as file:
                json.dump(content, file, indent=4)
                print('entry has been changed')
    except json.decoder.JSONDecodeError:
        print('no entry in database yet')

def main():
    json_file = 'oop.json'

    options = {
        "1": "add",
        "2": "find",
        "3": "delete",
        "4": "edit"
    }
    while True:
        display_list(options)
        ask = input('choose an option: ')
        if ask == '1':
            add_entry(json_file)
        elif ask == '2':
            find_entry(json_file)
        elif ask == '3':
            delete_entry(json_file)
        elif ask == '4':
            edit_entry(json_file)
        elif ask == '':
            print('bye')
            break
        else:
            print('enter the available key')
            
main()