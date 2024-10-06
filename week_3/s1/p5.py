#Write a function first_unique_char() that given a string my_str as a parameter, 
#it finds the first non-repeating character in it and returns its index. If it does not exist, then return -1.

def first_unique_char(my_str):
    #set an index pointer to 0
    #iterate through the string's chars:
    my_dict = {}
    for char in my_str:
        if char not in my_dict:
            my_dict[char] = 1
        else:
            my_dict[char] += 1

# Find the first unique character
    for i in range(len(my_str)):
        if my_dict[my_str[i]] == 1:
            return i  # Return the index of the first unique character

    return -1  # Return -1 if no unique character is found



def main():

    my_str = "leetcode"
    print(first_unique_char(my_str))

    str2 = "loveleetcode"
    print(first_unique_char(str2))

    str3 = "aabb"
    print(first_unique_char(str3))


main()

