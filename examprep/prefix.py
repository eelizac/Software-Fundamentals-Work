def prefix_search(dictionary, key_prefix):
    '''
    Given a dictionary (with strings for keys) and a string, returns a new dictionary containing only the keys (and their corresponding values) for which the string is a prefix.
    If the string is not a prefix for any key, a KeyError is raised.
    You can assume that you will not be given any empty strings in dictionary or as key_prefix

    For example,
    >>> prefix_search({"ac": 1, "ba": 2, "ab": 3}, "a")
    {'ac': 1, 'ab': 3}
    '''
    new_dict = {} 
    for x in dictionary:
        index = len(key_prefix) - 1
        i = 0 
        while i < index:
            if x[i] != key_prefix[i]: 
                break 
            i += 1
         
        if i == index: 
            if x[0] == key_prefix: 
                new_dict[x] = dictionary[x]

    return new_dict 

# prefix_search()

def main(): 
    prefix_search({"ac": 1, "ba": 2, "ab": 3}, "a")


if __name__ == "__main__": 
    main()