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

    find_folder = input('enter the folder: ')
    if find_folder in content:
        content = os.listdir(find_folder)
        print(content)
        ask = input('press 1 to add file | press 2 to add content: ')
        if ask == '1':
            ask2 = input('file name: ')
            formatted = f"{ask2}.txt"
            file = os.path.join(find_folder, formatted)
            note = input('note: ')
            with open(file, 'a')as file:
                file.write(f"{note}\n")
                print('new file has been created')
        elif ask == '2':
            files = os.listdir(find_folder)
            print(files)
            choose_file = input('enter the file: ').lower().strip()
            formatted_file = f"{choose_file}.txt"
            if formatted_file in files:
                print(formatted_file)
                new_note = input('add note: ')
                filelist = os.path.join(find_folder, formatted_file)
                with open(filelist, 'a')as file:
                    file.write(f"{new_note}\n")
                    print('added new note')
                with open(filelist, 'r')as file:
                    print()
                    print('notes:')
                    file_content = file.read()
                    print(file_content)
                

            
       
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