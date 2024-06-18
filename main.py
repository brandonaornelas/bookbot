
def get_book_text(path):
    with open(path, 'r') as f:
        return f.read()

def book_count(text):
    words = text.split()
    return len(words)

def characters_count(path):
    with open(path, 'r') as f:
        contents = f.read()
        count = {}
        for char in contents.lower():
            if char.isalpha():
                if char in count:
                    count[char] += 1
                else:
                    count[char] = 1
        return count


def main():
    book_path = './books/frankenstein.txt'
    text = get_book_text(book_path)
    word_count = book_count(text)
    character_count = characters_count(book_path)
    print(f'--- Begin report of {book_path} ---')
    print(f"{word_count} words found in document")
    print()
    for key, value in character_count.items():
        print(f'The {key} character was found {value} times')
    
    print('--- End report ---')
    

main()
