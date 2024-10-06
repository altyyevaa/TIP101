def reverse_string(my_str):
    #iterate through the string:
    reversed_string = ""
    length = len(my_str)
    for char in range(length-1, -1, -1):
        reversed_string += my_str[char]
    return reversed_string



def main():
    my_str = "live"
    print(reverse_string(my_str))

main()