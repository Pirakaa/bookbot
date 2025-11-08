def word_counter(txt):
    word_count = txt.split()
    print(f'Found {len(word_count)} total words')
    
    
def character_counter(txt):
    char_dict = {}
    txt = txt.lower()
    for char in txt:
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1
    return char_dict

def helper_sort(items):
    return items['num']

def sort_dict(dictionary):
    new_list = []
    for key in dictionary:
        add = {'char' : key, 'num' : dictionary[key]}
        new_list.append(add)
    new_list.sort(reverse=True, key=helper_sort)
    return new_list

