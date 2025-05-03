import os



def get_list(options):
    for key, value in options.items():
        print(f"({key}) {value}")


def add_folder(directory):
    if not os.path.exists(directory):
        os.mkdir(directory)

    add_folder = input('add folder name: ')
    added_folder = os.path.join(directory, add_folder)
    if not os.path.exists(added_folder):
        os.mkdir(add_folder)
        print('added new folder')
    
    else:
        print(f'welcome to {add_folder}')



    ask = input('do you want to add a file: ')
    if ask == 'y':
        ask2 = input('file name: ')
        content = os.path.join(added_folder, ask2 + ".txt")
        ask3 = input('write a note: ')
        with open(content, 'a')as file:
            file.write(f'{ask3} \n')
            print(f"'{ask3}' has been noted")

def find_folder(directory):
    content = os.listdir(directory)
    for index in content:
        print(index)

    ask = input('enter the folder name: ')
    if ask in content:
        add_file = input('add new file: ')
        added = os.path.join(directory, ask, add_file + ".txt")
        with open(added, 'a')as file:
            file.write('')
            print('added new file')
       
def main():
    directory = '/Users/michaeljamessoria/Documents/IDLE'


    options = {

        "1": "create new folder",
        "2": "find folder"
    }
    get_list(options)
    while True:
        ask = input('press 1 to create a folder | press 2 to find a folder: ').lower().strip()
        if ask == '1':
            add_folder(directory)
        elif ask == '2':
            find_folder(directory)
        

main()