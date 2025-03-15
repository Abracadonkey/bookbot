def num_words(book_text): 
     
    count = len(book_text.split()) 
    return count  



def book_bot_dict(book_text): 
    character_count = {} 
    low_case = book_text.lower() 
    for character in low_case: 
        if character in character_count:
            character_count[character] += 1 
        else: 
            character_count[character] = 1
   
    return character_count
    

def sort_char_counts(char_counts):
    char_list = [] 
    for char, count in char_counts.items(): 
        char_list.append({"char": char, "count": count}) 

    def sort_on(dict): 
            return dict["count"] 
        
    char_list.sort(reverse=True,key=sort_on) 

    return char_list






    

 