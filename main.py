
from calculator import calculate
from file_reader import read_csv
from result_displayer import display_result
from verify_file import check_filename
from verify_operand import check_operation


def main():
    print("Début du programme")
    file_name = check_filename()
    operation = check_operation()
    numbers = read_csv(file_name)
    if numbers:
        result = calculate(numbers, operation)
        display_result(numbers, operation, result)
    else:
        print("No valid numbers found in the CSV file.")


if __name__ == "__main__":
    main()
