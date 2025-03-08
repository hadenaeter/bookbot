def word_count(text):
    words = text.split()
    return len(words)

def get_character_frequencies(text):
    char_dict = {}
    for char in text:
        char = char.lower()
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1
    return sort_char_dict(char_dict)

def sort_char_dict(char_dict):
    def sort_on(char_dict):
        return char_dict["count"]
    frequencies = []
    for char in char_dict:
        frequencies.append({"character": char, "count": char_dict[char]})
    frequencies.sort(reverse=True, key=sort_on)
    return frequencies
