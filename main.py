import os



def get_list(options):
    for key, value in options.items():
        print(f"({key}) {value}")


def display(items):
    sort = sorted(items)
    for i in sort:
        print(i)



def add_folder(directory):
    
    if not os.path.exists(directory):
        os.mkdir(directory)
    
    ask = input('create a folder: ')
    char = any(char in "()*&^%$#@!~`,.;':?}{[]" for char in ask )
    error = ask[0] == '/' or ask[-1] == '/'
    fullpath = os.path.join(directory, ask)
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
  



def find_folder(directory):
    if not os.path.exists(directory):
        output = "no directory at the moment"
        return output

    
    folders = os.listdir(directory)
    sort = sorted(folders)
    
    for index, folder in enumerate(sort, start=1):
        print(f"{index}. {folder}")
    
    ask = input('enter the folder name: ')
    if not ask:
        return 'try again'
    else:
        fullpath = os.path.join(directory, ask)
        if os.path.exists(fullpath):
            files = os.listdir(fullpath)
            if files:
                for file in files:
                    print(file)
            else:
                return 'no content'
        else:
            return 'file does not exist'
    

    
def create_file_txt(prompt):
    ask = input(prompt).strip()
    formatted_ask = f"{ask}.txt"
    return formatted_ask


def create_file(directory):

    try:
        dir = os.listdir(directory)
        display(dir)
        ask = input('select a folder: ')
        if ask in dir:
            ask2 = input('press 1 new file | press 2 add content | press enter to exit: ')
            if ask2 == '1':
                ask3 = create_file_txt('file name: ')
                fullpath = os.path.join(directory, ask, ask3)
                with open(fullpath, 'w')as file: 
                    file.write('')
                    print('new file has been created')
            elif ask2 == '2':
                full = os.path.join(directory, ask)
                full_path = os.listdir(full)
                display(full_path)
                ask4 = input('select a file: ')
                joinpath = os.path.join(full, ask4)
                if os.path.exists(joinpath):
                    ask5 = input('note: ')
                    print('note list: ')
                    with open(joinpath, 'a')as file:
                        file.write(f"{ask5}\n") 
                    with open(joinpath, 'r')as file:
                        con = file.read()
                    print(con)
                            


    except FileNotFoundError:
        print('file not found error')



    
            

            
       
def main():
    directory = '/Users/michaeljamessoria/Documents/IDLE/folders'

    options = {

        "1": "create a folder",
        "2": "find folder",
        "3": "create a file"
    }
    get_list(options)
    while True:
        ask = input('press 1 new folder | press 2 find folder | press 3 new file: ').lower().strip()
        if ask == '1':
            add_folder(directory)
        elif ask == '2':
            print(find_folder(directory))
        elif ask == '3':
            create_file(directory)
        

main()