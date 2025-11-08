from stats import word_counter, character_counter, sort_dict
import sys

def get_book_text(filepath):
    with open(filepath, encoding="utf-8") as f:
        return f.read()

if len(sys.argv) != 2:
    print('Usage: python3 main.py <path_to_book>')
    sys.exit(1)
    

def main():
    book_path = sys.argv[1]
    text = get_book_text(book_path)
    word_counter(text)
    characters = character_counter(text)
    characters_sorted = sort_dict(characters)
    for item in characters_sorted:
        if item['char'].isalpha():
            print(f"{item['char']}: {item['num']}")
    
main()