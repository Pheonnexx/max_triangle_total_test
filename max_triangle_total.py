import sys


def calculate_triangle_total(filename):
    triangle_file_lines = open(filename).readlines()
    position = 0
    triangle_numbers = []
    no_of_lines = (len(triangle_file_lines))
    count = 0

    while count < no_of_lines:
        numbers_in_range = []
        secondary_number_list = []
        index_range = list(range(position, position + 2))
        line1 = list(map(int, triangle_file_lines[count].split(' ')))
        try:
            line2 = list(map(int, triangle_file_lines[count + 1].split(' ')))
        except IndexError:
            line2 = []
            pass

        for index in index_range:

            try:
                number = line1[index]
                numbers_in_range.append(number)

                if line2:
                    second_index_range = list(range(index, index + 2))

                    for index_2 in second_index_range:
                        secondary_number = number + line2[index_2]
                        secondary_number_list.append(secondary_number)

                        if max(secondary_number_list) == secondary_number:
                            max_number = number
                            current_position = index

                else:
                    if max(numbers_in_range) == number:
                        max_number = number
                        current_position = index

            except IndexError:
                pass

        triangle_numbers.append(max_number)
        position = current_position
        count += 1
    total = sum(triangle_numbers)
    print("TOTAL")
    print(total)


calculate_triangle_total(sys.argv[1])
