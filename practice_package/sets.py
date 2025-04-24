# sets.py

def find_common_elements(set1, set2):
    return set([x for x in set1 if x in set2])


def is_superset(set_a, set_b):
    for item in set_b:
        if item not in set_a:
            return False
    return True


def remove_duplicates(items):
    seen = set()
    result = []
    for item in items:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result


def count_unique_words(text):
    words = text.lower().split()
    return len(set(words))


def find_shared_items(*sets):
    if not sets:
        return set()
    shared = sets[0].copy()
    for s in sets[1:]:
        shared = {item for item in shared if item in s}
        if not shared:
            break
    return shared
