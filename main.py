import os



def get_list(options):
    for key, value in options.items():
        print(f"({key}) {value}")



def add_folder(directory):
    dir = os.getcwd()
    print(dir)

    ask = input('create a folder: ')
    char = any(char in "()*&^%$#@!~`,.;':?}{[]" for char in ask )
    error = ask[0] == '/' or ask[-1] == '/'
    fullpath = os.path.join(dir, ask)
    if not os.path.exists(fullpath):
        if not error and not char:
            os.makedirs(fullpath)
            print('new folder has been created')
        else:
            print('try again')
    else:
        print('already existing')
        
    
            
        



# def find_folder(directory):
#     content = os.listdir(directory)
#     for index in content:
#         print(index)

#     find_folder = input('enter the folder: ')
#     if find_folder in content:
#         content = os.listdir(find_folder)
#         print(content)

#         ask = input('press 1 to add file | press 2 to add content: ')
#         if ask == '1':
#             ask2 = input('file name: ')
#             formatted = f"{ask2}.txt"
#             file = os.path.join(find_folder, formatted)
#             note = input('note: ')
#             with open(file, 'a')as file:
#                 file.write(f"{note}\n")
#                 print('new file has been created')

#         elif ask == '2':
#             files = os.listdir(find_folder)
#             for i in files:
#                 print(i.replace('.txt', ''))
#             choose_file = input('enter the file: ').lower().strip()
#             formatted_file = f"{choose_file}.txt"

#             if formatted_file in files:
#                 new_note = input('add note: ')
#                 filelist = os.path.join(find_folder, formatted_file)
#                 with open(filelist, 'a')as file:
#                     file.write(f"{new_note}\n")
#                     print('added new note')
#                 with open(filelist, 'r')as file:
#                     print()
#                     print('notes:')
#                     file_content = file.read()
#                     print(file_content)
                

            
       
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
        # elif ask == '2':
        #     find_folder(directory)
        

main()