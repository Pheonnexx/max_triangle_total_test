import sys

def calculate_triangle_total(filename):
    triangle_file_lines = open(filename).readlines()
    position = 1
    triangle_numbers = []

    for triangle_line in triangle_file_lines:

        numbers_in_range = []
        index_range = list(range(position - 1, position + 2, 1))
        line = list(map(int, triangle_line.split(' ')))

        for index, number in list(enumerate(line, start=1)):

            if index in index_range:
                numbers_in_range.append(number)

            # If it is not in the range it doesnt append anything, if numbers in range is empty
            # max raises an error which i am not interested in.
            try:
                if max(numbers_in_range) == number:
                    max_number = number
                    current_position = index
            except ValueError:
                pass

        triangle_numbers.append(max_number)
        position = current_position

    total = sum(triangle_numbers)
    print("TOTAL")
    print(total)

calculate_triangle_total(sys.argv[1])
