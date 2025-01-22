def count_words(book):
    words = book.split()
    number_of_words = len(words)
    return number_of_words

def count_characters(book):
    lowered_book = book.lower()
    character_dict = {}
    for char in lowered_book:
        if char not in character_dict:
            character_dict[char] = 1
        else:
            character_dict[char] += 1
    return character_dict

def sort_on(dict):
    return dict["num"]

def report(book):
    words = count_words(book)
    char_dict = count_characters(book)
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{words} words found in the document")
    print(" ")
    new_char_list = []
    for char in char_dict:
        if char.isalpha():
            new_char_list.append({"name":char,"num":char_dict[char]})
    new_char_list.sort(reverse=True, key=sort_on)
    for item in new_char_list:
        print(f"The '{item["name"]}' character was found {item['num']} times")

    print("--- End Report ---")

    



def main():

    with open("books/frankenstein.txt") as f:
        book_contents = f.read()
    
    report(book_contents)
    
main()