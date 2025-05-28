def get_words_in_string(string):
    words = string.split()
    # print(f"Words list:\n{words}")
    return len(words)

def get_characters_in_string(string):
    string = string.lower()
    character_dict = {}
    for char in string:
        if char in character_dict:
            character_dict[char] += 1
        else:
            character_dict[char] = 1
    return character_dict

def sort_on(dict):
    return dict["num"]

def get_sorted_char_dict_list(char_dict):
    char_dict_list = []
    for key in char_dict:
        small_dict = {
            "char": key, 
            "num": char_dict[key]
        }
        char_dict_list.append(small_dict)
    char_dict_list.sort(reverse=True, key=sort_on)
    return char_dict_list