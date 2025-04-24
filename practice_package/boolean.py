check_between_numbers = lambda a, b, c: a < b < c or a > b > c  # noqa: E731


check_odd_three = lambda n: 99 < abs(n) < 1000 and abs(n) % 2  # noqa: E731


check_unique_digits = lambda n: 99 < abs(n) < 1000 and len(set(str(n))) >= 3  # noqa: E731


def check_palindrome_number(n):
    return str(abs(n))[::-1] == str(abs(n))


check_ascending_digits = lambda n: (100 <= abs(n) <= 999) and \
    (abs(n) // 100 < abs(n) // 10 % 10 < abs(n) % 10)  # noqa: E731