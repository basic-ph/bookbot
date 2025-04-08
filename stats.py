def count_words(text: str):
    return len(text.split())


def count_chars(text: str):
    result = {}
    for char in text:
        lower_char = char.lower()
        if lower_char not in result:
            result[lower_char] = 1
        else:
            result[lower_char] += 1

    return result


def sort_on(dict):
    return dict["count"]


def get_sorted_chars(chars_dict: dict):
    result = []

    for char, count in chars_dict.items():
        result.append({
            'char': char,
            'count': count,
        })

    result.sort(key=sort_on, reverse=True)

    return result
