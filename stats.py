def word_counter(txt):
    word_count = txt.split()
    print(f'Found {len(word_count)} total words')
    
def character_counter(txt):
    txt = txt.lower()
    char_dict = {}
    for char in txt:
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1
    return char_dict