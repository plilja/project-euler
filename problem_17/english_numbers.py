known_numbers = {
    1: 'one',
    2: 'two',
    3: 'three',
    4: 'four',
    5: 'five',
    6: 'six',
    7: 'seven',
    8: 'eight',
    9: 'nine',
    10: 'ten',
    11: 'eleven',
    12: 'twelve',
    13: 'thirteen',
    14: 'fourteen',
    15: 'fifteen',
    16: 'sixteen',
    17: 'seventeen',
    18: 'eighteen',
    19: 'nineteen',
    20: 'twenty',
    30: 'thirty',
    40: 'forty',
    50: 'fifty',
    60: 'sixty',
    70: 'seventy',
    80: 'eighty',
    90: 'ninety',
}


def english_number(number):
    if number == 0:
        return 'zero'

    parts = []
    rest = number % 100
    if number != rest:
        parts += [_english_number_100_to_9999(number - rest)]
    if rest != 0:
        parts += [_english_number_0_to_99(rest)]
    return ' and '.join(parts)


def _english_number_100_to_9999(number):
    result = ''
    if number >= 1000:
        result += _thousands(int(number / 1000)) + ' '
    if number % 1000 != 0:
        result += _hundreds(int(number % 1000) / 100)
    return result.strip()


def _english_number_0_to_99(number):
    if number in known_numbers:
        return known_numbers[number]
    b = number % 10
    a = number - b
    return known_numbers[a] + '-' + known_numbers[b]


def _thousands(num_thousands):
    return known_numbers[num_thousands] + ' thousand'


def _hundreds(num_hundreds):
    return known_numbers[num_hundreds] + ' hundred'


def len_numbers(numbers):
    numbers_as_english = [english_number(n) for n in numbers]
    num_letters_for_each_number = [len(n.replace(' ', '').replace('-', '')) for n in numbers_as_english]
    return sum(num_letters_for_each_number)
