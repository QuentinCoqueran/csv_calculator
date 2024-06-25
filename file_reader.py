import csv


def read_csv(file_name):
    numbers = []
    with open(file_name, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            for item in row:
                try:
                    num = int(item)
                    numbers.append(num)
                except ValueError:
                    print(f"Skipping non-integer value: {item}")
    return numbers
