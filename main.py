import os



def get_list(options):
    for key, value in options.items():
        print(f"({key}) {value}")


def display(items):
    sort = sorted(items)
    for i in sort:
        if i.endswith('.txt'):
            print(f'{i.replace('.txt', '')}')
        else:
            print(i)
        


def add_folder(dir_folder):
    
    if not os.path.exists(dir_folder):
        os.mkdir(dir_folder)
    try:
        ask = input('create a folder: ')
        char = any(char in "()*&^%$#@!~`,.;':?}{[]" for char in ask )
        error = ask[0] == '/' or ask[-1] == '/'
        fullpath = os.path.join(dir_folder, ask)
        if not os.path.exists(fullpath):
            try:
                if not error and not char:
                    os.mkdir(fullpath)
                    print('folder has been created')
                else:
                    print('try again')
            except FileNotFoundError:
                print('cannot make a subfolder')
            
        else:
            print('already existing')
    except IndexError:
        print("index error")



def find_folder(dir_folder):
    if not os.path.exists(dir_folder):
        output = "no dir_folder at the moment"
        return print(output)

    
    folders = os.listdir(dir_folder)
    sort = sorted(folders)
    
    for index, folder in enumerate(sort, start=1):
        print(f"{index}. {folder}")
    
    ask = input('enter the folder name: ').strip()
    if not ask:
        print('try again')
    else:
        fullpath = os.path.join(dir_folder, ask)
        if os.path.exists(fullpath):
            files = os.listdir(fullpath)
            if files:
                display(files)
            else:
                print('no content')
        else:
            print('file does not exist')
        
    
def create_file_txt(prompt):
    ask = input(prompt).strip()
    formatted_ask = f"{ask}.txt"
    return formatted_ask


def create_file(dir_folder):

    try:
        dir = os.listdir(dir_folder)
        display(dir)
        ask = input('select a folder: ')
        if ask in dir:
            while True:
                ask2 = input('press 1 new file | press 2 add content | press enter to exit: ')
                if ask2 == '1':
                    ask3 = create_file_txt('file name: ')
                    fullpath = os.path.join(dir_folder, ask, ask3)
                    with open(fullpath, 'w')as file: 
                        file.write('')
                        print('new file has been created')
                elif ask2 == '2':
                    full = os.path.join(dir_folder, ask)
                    full_path = os.listdir(full)
                    

                    display(full_path)
                    ask4 = input('select a file: ')
                    joinpath = os.path.join(full, ask4 + ".txt")
                    if os.path.exists(joinpath):
                        while True:
                            ask5 = input('add note: ')
                            if ask5 == "":
                                return False
                            else:
                                print('note list: ')
                                with open(joinpath, 'a')as file:
                                    file.write(f"{ask5}\n") 
                                with open(joinpath, 'r')as file:
                                    con = file.read()
                                print(con)
                elif ask2 == '':
                    return False
                
                else:
                    print('wrong key')

    except FileNotFoundError:
        print('file not found error')



def delete_folder(dir_folder):
    print(dir_folder)

    dir_list = os.listdir(dir_folder)
    display(dir_list)
    ask  = input('foldername: ')
    if ask in dir_list:
        print(ask)
        merge = os.path.join(dir_folder, ask)
        print(merge)
        merge_list = os.listdir(merge)
        if not merge_list:
           os.rmdir(merge)
           print('deleted successfully')
        else:
            print('there is a content inside')



       
def main():

    # directory = '/Users/michaeljamessoria/Documents/IDLE/folders'
    directory = os.getcwd()
    print(directory)
    main_folder = 'folders'
    dir_folder = os.path.join(directory, main_folder)
    print(dir_folder)

    options = {

        "1": "create folder",
        "2": "find folder",
        "3": "create file",
        "4": "delete folder"
    }
    get_list(options)
    while True:
        ask = input('press (1) new folder | press (2) find folder | press (3) new file | press (4) delete folder: ').lower().strip()
        if ask == '1':
            add_folder(dir_folder)
        elif ask == '2':
            find_folder(dir_folder)
        elif ask == '3':
            create_file(dir_folder)
        elif ask == '4':
            delete_folder(dir_folder)
        
main()