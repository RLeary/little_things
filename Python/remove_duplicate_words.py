# Removes duplicate words from a string
# not effiecient - O(n^2), as 'in' goes throuhg the whole list each time
# it is called in the loop

def remove_duplicate_words(s):
    words = s.split()
    words_list = list()
    
    for word in words:
        if word not in words_list:
            words_list.append(word)
            
    return ' '.join(str(x) for x in words_list)