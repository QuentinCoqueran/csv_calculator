
def check_operation():
    operation = ''
    valid_operation = False
    while not valid_operation:
        operation = input('Enter the operation (+ or *): ')
        if operation in ('+', '*'):
            valid_operation = True
        else:
            print('Operation not supported')
    return operation
