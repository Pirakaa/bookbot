from stats import word_counter, character_counter, sort_dict

def get_book_text(filepath):
    with open(filepath, encoding="utf-8") as f:
        return f.read()
    

def main():
    text = get_book_text("books/frankenstein.txt")
    word_counter(text)
    characters = character_counter(text)
    characters_sorted = sort_dict(characters)
    for item in characters_sorted:
        if item['char'].isalpha():
            print(f"{item['char']}: {item['num']}")
    
main()