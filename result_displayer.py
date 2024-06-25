def display_result(numbers, operation, result):
    if isinstance(numbers, list) and len(numbers) > 0:
        expression = str(numbers[0])
        for number in numbers[1:]:
            expression += f" {operation} {number}"
        expression += f" = {result}"

        print(expression)
        print('-------')
        print(f'total = {result} ({operation})')
    else:
        print(f"Invalid numbers type: {type(numbers)}")