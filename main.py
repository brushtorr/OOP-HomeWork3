import os
file_names = ['1.txt', '2.txt', '3.txt']

def get_line_count(file_name):
    with open(file_name, 'r', encoding='utf-8') as file:
        return len(file.readlines())

file_names.sort(key=get_line_count)

output_file_name = 'result.txt'
with open(output_file_name, 'w', encoding='utf-8') as output_file:
    for file_name in file_names:
        line_count = get_line_count(file_name)

        output_file.write(f'{file_name}\n{line_count}\n')

        with open(file_name, 'r', encoding='utf-8') as input_file:
            for line in input_file:
                output_file.write(line)
            output_file.write('\n')



