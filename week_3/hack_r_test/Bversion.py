def anagram_checker(str1, str2):
# Remove spaces and convert both strings to lowercase
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()

    if len(str1) != len(str2):
        return False

    char_count = {}
    for char in str1:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

 # Check each character in str2 against the dictionary
    for char in str2:
        if char in char_count:
            char_count[char] -= 1
        if char_count[char] < 0:
            return False
        else:
            return False

    for count in char_count.values():
        if count != 0:
            return False

    return True

def main():
    str1 = "aziza"
    str2 = "aizza"
    print(anagram_checker(str1, str2))

main()