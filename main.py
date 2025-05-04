import os



def get_list(options):
    for key, value in options.items():
        print(f"({key}) {value}")



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
    

    


            
       
def main():
    directory = '/Users/michaeljamessoria/Documents/IDLE/folders'

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
            print(find_folder(directory))
        

main()