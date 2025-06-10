def get_num_words(text):
    return len(text.split())


def get_chars_count(content):
    char_count = {}

    for char in content:
        char_count[char.lower()] = char_count.get(char.lower(), 0) + 1

    return char_count