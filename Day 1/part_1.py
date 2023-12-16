def get_first_digit(line)->str:
    for char in line:
        if char.isdigit():
            return char
    print(f'Did not find digit in string. String: {line}')

numbers = []
with open('input.txt') as file:
    lines = file.readlines()
    for line in lines:
        first = get_first_digit(line)
        last = get_first_digit(line[::-1])
        numbers.append(int(first+last))
print(f'Calibrarion Code: {sum(numbers)}')