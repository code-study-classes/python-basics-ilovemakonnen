import collections

def count_char_occurrences(text):
    # Оставляем только буквы, преобразуем их в нижний регистр
    filtered_text = [char.lower() for char in text if char.isalpha()]
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
            column_widths[col] = max(column_widths.get(col, 0), len(str(row.get(col, "N/A"))))
    
    # Формируем заголовки
    table = "| " + " | ".join(col.upper().ljust(column_widths[col]) for col in columns) + " |"
    table += "\n|" + "|".join("-" * (column_widths[col] + 2) for col in columns) + "|"
    
    # Формируем строки таблицы
    for row in data_dict.values():
        table += "\n| " + " | ".join(str(row.get(col, "N/A")).ljust(column_widths[col]) for col in columns) + " |"
    
    return table

def deep_update(base_dict, update_dict):
    if not base_dict:
        return update_dict

    updated_dict = base_dict.copy()
    
    for key, value in update_dict.items():
        if isinstance(value, dict) and key in updated_dict and isinstance(updated_dict[key], dict):
            updated_dict[key] = deep_update(updated_dict[key], value)
        elif key not in updated_dict:
            updated_dict[key] = value
        else:
            updated_dict[key] = value
    
    # Удаление ключей, которых нет в update_dict
    for key in list(updated_dict.keys()):
        if key not in update_dict:
            del updated_dict[key]
    
    return updated_dict

