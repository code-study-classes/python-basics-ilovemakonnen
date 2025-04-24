from pathlib import Path

extract_file_name = lambda full_file_name: Path(Path(full_file_name).stem).stem  # noqa: E731


def encrypt_sentence(sentence):
    first_half = []
    last_half = []
    for i in range(0, len(sentence)):
        if i % 2 == 0:
            last_half.insert(0, sentence[i])
        else:
            first_half.append(sentence[i])
    return ''.join(first_half) + ''.join(last_half)


def check_brackets(expression):
    openCount = 0
    closeCount = 0
    pos = 0
    for i in range(0, len(expression)):
        if expression[i] != ' ':
            pos += 1
        if expression[i] == '(':
            openCount += 1
        elif expression[i] == ')':
            closeCount += 1
        if closeCount > openCount:
            return pos
    if openCount > closeCount:
        return -1
    return 0


def reverse_domain(domain):
    return '.'.join(domain.split('.')[::-1])


VOWELS = ['a', 'e', 'i', 'o', 'u', 'y']


def count_vowel_groups(word):
    count = 0
    isVowelGroup = False
    for letter in word:
        if letter.lower() in VOWELS and not isVowelGroup:
            count += 1
            isVowelGroup = True
        elif letter.lower() not in VOWELS:
            isVowelGroup = False
    return count