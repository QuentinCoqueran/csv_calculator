def check_filename():
    file_name = ''
    valid_file_name = False
    while not valid_file_name:
        file_name = input('Enter the file name: ')
        if not file_name:
            print('File name not provided')
            continue
        try:
            with open(file_name, 'r') as file:
                valid_file_name = True
        except FileNotFoundError:
            print('File not found')
    return file_name
