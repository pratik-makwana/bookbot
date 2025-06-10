def get_num_words(text):
    return len(text.split())


def get_chars_count(content):
    char_count = {}

    for char in content:
        char_count[char.lower()] = char_count.get(char.lower(), 0) + 1

    return char_count


def sort_on(dictionary):
    
    for (key, value) in dictionary.items():
        if isinstance(value, (int, float)):
            return value
    return -float('inf')


def char_dict_to_sorted_list(d):

    sorted_list = [{k: v} for k, v in d.items() if k.isalpha()]
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list