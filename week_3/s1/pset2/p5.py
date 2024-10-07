import string


def compress_string(my_str):
    pass
    my_dict = {}
    comp_s = ""
    compressed_length = 0
    
    for char in my_str:
        if char not in my_dict:
            my_dict[char] = 1
        else:
            my_dict[char] += 1
        
    for key, value in my_dict.items():
        comp_s += str(key) + str(value)
        compressed_length += len(str(key)) + len(str(value))  # Keep track of length
        
        # Early return if compressed string is longer or equal to original
        if compressed_length >= len(my_str):
            return my_str  # Return original string if compression isn't effective
    return comp_s


def main():
    my_str = "aaaaabbcccd"
    compressed_Str = compress_string(my_str)
    print(compressed_Str)

    my_str2 = "abcde"
    compressed_Str2 = compress_string(my_str2)
    print(compressed_Str2)

main()