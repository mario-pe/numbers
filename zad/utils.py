import textwrap

billions = ['bilion', 'biliony', 'bilionów']

millions = ['milion', 'miliony', 'milionów']

thousands = ['tysiąc', 'tysiące', 'tysięcy']

amounts = [thousands, millions, billions]

houndreds = ['', 'sto', 'dwiescie', 'trzysta', 'czterysta', 'piecset', 'szescset', 'siedemset', 'osiemset',
             'dziewiecset']

tens = ['dzieśięć', 'dwadzieścia', 'trzydzieści', 'czterdzieści', 'pięćdziesiąt', 'sześćdziesiąt', 'siedemdziesiąt',
        'osiemdziesiąt', 'dziewiecdziesiąt']

after_ten = ['jedenaście', 'dwanaście', 'trzynaście', 'czternaście', 'piętnaście', 'szesnaście',
             'siedemnaście', 'osiemnaście', 'dziewiętnaście']

ones = ['', 'jeden', 'dwa', 'trzy', 'cztery', 'pięc', 'sześć', 'siedem', 'osiem', 'dziewięć']


def number_text_converter(number, index):
    if len(number) > 3:
        return 'Błąd'
    number = number.zfill(3)
    result = ''
    number_of_hundreds = int(number[0])
    number_of_tens = int(number[1])
    number_of_ones = int(number[2])

    if number_of_hundreds > 0:
        result += houndreds[number_of_hundreds] + ' '

    if number_of_tens == 0:
        result += ones[number_of_ones] + ' '
    elif number_of_tens == 1:
        if not number_of_ones == 0:
            result += after_ten[number_of_ones -1] + ' '
        else:
            result += tens[0] + ' '
    else:
        result += tens[number_of_tens-1] + ' '
        result += ones[number_of_ones] + ' '

    if index > 1:
        amount = amounts[index - 2]
        if number_of_ones == 1 and number_of_tens != 1:
            result += amount[0] + ' '
        elif number_of_ones < 5 and number_of_tens == 0 and number_of_tens != 1:
            result += amount[1] + ' '
        elif number_of_ones < 5 and number_of_ones > 0 and number_of_tens != 1:
            result += amount[1] + ' '
        else:
            result += amount[2] + ' '
    return result


def word_generator(number):
    label = ''
    if len(number) == 1 and number == '0':
        return 'zero'

    if number[0] == '-':
        label += 'minus '
        number = number[1:]

    print('number: ' + str(number))
    number = number.lstrip("0")
    print('number: ' + str(number))
    lenght = len(number)
    if lenght > 12:
        return "zbyt duza liczba, max 12 cyfr "

    if lenght == 0:
        return 'zera nie maja wartosci, wpisz poprawną liczbe'

    ilosc_trojek = int(len(number) / 3)
    modulo = len(number)%3

    counter = 0
    if modulo != 0:
        counter += 1
    counter += ilosc_trojek

    converted_numbers = prepare_numbers(number)

    print(converted_numbers)
    for i in converted_numbers:
        label += number_text_converter(i, counter)
        counter -= 1
    return label


def prepare_numbers(number):
    split_number = textwrap.wrap(number[::-1], 3)
    correct_order_tabs = split_number[::-1]
    result = []
    for c in correct_order_tabs:
        result.append(c[::-1])
    return result