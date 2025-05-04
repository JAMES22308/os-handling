import os

def create_dir():
    filename = input('filename: ')
    os.makedirs(filename)
    print('creted successfully')

def remove_dir():

    path = os.getcwd()
    ask = input('folder: ')

    full_path = os.path.join(path, ask)

    if os.path.exists(full_path):
        try:
            os.rmdir(full_path)
            print('deleted successfully')
        except OSError:
            print('not empty')
    else:
        print('not existing folder')
    
    

def main():

    options = {
        "c": "create",
        "r": "remove",
        "e": "exit"
    }

    for key, value in options.items():
        print(f"({key}) {value}")

    
    while True:
        ask = input("enter option: ")
        if ask == "c":
            create_dir()
        elif ask == "r":
            remove_dir()
        elif ask == 'e':
            print('Bye')
            break
        else:
            print('wrong key')

main()