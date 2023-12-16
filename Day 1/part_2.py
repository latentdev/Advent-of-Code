import re

word_to_digit = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9',
    'zero': '0'
}

def get_all_digits(line):
    return re.findall(r'(?:\d+?|one|two|three|four|five|six|seven|eight|nine)', line)

numbers = []
with open('input.txt') as file:
    lines = file.readlines()
    for line in lines:
        digits = get_all_digits(line)
        first = word_to_digit.get(digits[0],digits[0])
        last = word_to_digit.get(digits[-1],digits[-1])
        number = first+last
        numbers.append(int(number))
        print(f'{number}|{digits}|{line}')
print(f'Calibrarion Code: {sum(numbers)}')