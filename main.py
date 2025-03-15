import sys


if len(sys.argv) > 1:
    first_argument = sys.argv[0] 
    file_path = sys.argv[1]
if len(sys.argv) != 2: 
    print("Usage: python3 main.py <path_to_book>") 
    sys.exit(1)



from stats import ( 
    num_words,
    book_bot_dict,
    sort_char_counts,

)


def main():
  
   full_book = get_book_text(sys.argv[1]) 
   text_count = num_words(full_book) 
   chara_count = book_bot_dict(full_book)
   sorted_chara = sort_char_counts(chara_count)
   
   print(print_report(full_book, text_count, sorted_chara))






def get_book_text(file_path): 
    with open(file_path) as f: 
        return f.read()   
    
    





def print_report(book_path,word_count, sorted_chars): 
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------") 

     # Loop through the sorted list of character dictionaries
    for char_dict in sorted_chars:
        char = char_dict["char"]
        count = char_dict["count"]
        
        # Only print alphabetical characters
        if char.isalpha():
            print(f"{char}: {count}")
    
    print("============= END ===============")
    
    
    



   
    


















main()