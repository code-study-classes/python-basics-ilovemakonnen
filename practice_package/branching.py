def is_weekend(day):
    return day < 8 and day in range(6, 8)


def get_discount(amount):
    return amount / 10 if amount >= 5000 else \
        amount / 20 if amount >= 1000 else 0


def describe_number(n):
    even = 'четное' if n % 2 == 0 else 'нечетное'
    digits = 'однозначное' if len(str(n)) == 1 else \
        'двузначное' if len(str(n)) == 2 else \
        'трехзначное'
    return f"{even} {digits} число"


def convert_to_meters(unitNumber, lengthInUnits):
    match unitNumber:
        case 1:
            return lengthInUnits / 10
        case 2:
            return lengthInUnits * 1000
        case 3:
            return lengthInUnits
        case 4:
            return lengthInUnits / 1000
        case 5:
            return lengthInUnits / 100
        case _:
            return 0


def describe_age(age):
    units = {
        1: 'один', 2: 'два', 3: 'три', 4: 'четыре',
        5: 'пять', 6: 'шесть', 7: 'семь', 8: 'восемь', 9: 'девять'
    }
    tens = {
        2: 'двадцать', 3: 'тридцать', 4: 'сорок', 5: 'пятьдесят',
        6: 'шестьдесят', 7: 'семьдесят', 8: 'восемьдесят', 9: 'девяносто'
    }

    if age == 100:
        age_str = 'сто'
    else:
        ten = age // 10
        unit = age % 10
        age_str = tens[ten]
        if unit != 0:
            age_str += ' ' + units[unit]

    last_digit = age % 10
    if last_digit == 1:
        age_word = 'год'
    elif 2 <= last_digit <= 4:
        age_word = 'года'
    else:
        age_word = 'лет'

    return f"{age_str} {age_word}"
