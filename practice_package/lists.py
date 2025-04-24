def square_odds(numbers):
    return [x ** 2 for x in numbers if x % 2 != 0]


def normalize_names(names):
    return [name.capitalize() for name in names]


def remove_invalid_emails(emails):
    return [
        email for email in emails
        if email.count('@') == 1 and len(email) >= 5
        and not email.startswith('@') and not email.endswith('@')
    ]


def filter_palindromes(words):
    return [word for word in words if word.lower() == word[::-1].lower()]


def calculate_factorial(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


def find_common_prefix(strings):
    if not strings:
        return ""
    prefix = strings[0]
    for s in strings[1:]:
        i = 0
        while i < len(prefix) and i < len(s) and prefix[i] == s[i]:
            i += 1
        prefix = prefix[:i]
        if not prefix:
            break
    return prefix
