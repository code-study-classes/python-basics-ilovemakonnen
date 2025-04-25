import collections
import re


def count_char_occurrences(text):
    # Разбиваем текст на "слова", игнорируя дефисы и другие небуквенные символы
    words = re.findall(r'[a-zA-Z]+', text)
    filtered_text = [char.lower() for word in words for char in word]
    return dict(collections.Counter(filtered_text))


def merge_dicts(dict1, dict2, conflict_resolver):
    result = dict1.copy()
    for key, value in dict2.items():
        if key in result:
            result[key] = conflict_resolver(key, result[key], value)
        else:
            result[key] = value
    return result


def invert_dictionary(original_dict):
    inverted_dict = {}
    for key, value in original_dict.items():
        if value not in inverted_dict:
            inverted_dict[value] = [key]
        else:
            inverted_dict[value].append(key)
    return inverted_dict


def dict_to_table(data_dict, columns):
    # Определим ширину столбцов для выравнивания
    column_widths = {col: len(col.upper()) for col in columns}
    for row in data_dict.values():
        for col in columns:
            value = str(row.get(col, "N/A"))
            column_widths[col] = max(column_widths.get(col, 0), len(value))
    
    # Формируем заголовки
    headers = [col.upper().ljust(column_widths[col]) for col in columns]
    table = "| " + " | ".join(headers) + " |"
    
    separators = ["-" * (column_widths[col] + 2) for col in columns]
    table += "\n|" + "|".join(separators) + "|"
    
    # Формируем строки таблицы
    for row in data_dict.values():
        row_cells = [
        str(row.get(col, "N/A")).ljust(column_widths[col]) for col in columns
        ]
        table += "\n| " + " | ".join(row_cells) + " |"
    
    return table


def deep_update(base_dict, update_dict):
    result = {}

    for key in base_dict:
        if key in update_dict:
            if (
                isinstance(base_dict[key], dict)
                and isinstance(update_dict[key], dict)
            ):
                result[key] = deep_update(base_dict[key], update_dict[key])
            else:
                result[key] = update_dict[key]
        else:
            result[key] = base_dict[key]

    return result
