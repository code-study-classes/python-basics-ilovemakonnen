# loops.py

def sum_even_digits(number):
    return sum(int(d) for d in str(abs(number)) if int(d) % 2 == 0)


def count_vowel_triplets(text):
    vowels = set("aeiouy")
    text = text.lower()
    count = 0
    for i in range(len(text) - 2):
        if (text[i] in vowels and 
            text[i + 1] in vowels and 
            text[i + 2] in vowels):
            count += 1
    return count


def find_fibonacci_index(number):
    if number == 1:
        return 1  # По условию задачи 1 считается только один раз на позиции 1
    a, b = 1, 1
    index = 2
    while b < number:
        a, b = b, a + b
        index += 1
    return index if b == number else -1


def remove_duplicates(string):
    if not string:
        return ""
    result = [string[0]]
    for ch in string[1:]:
        if ch != result[-1]:
            result.append(ch)
    return ''.join(result)
