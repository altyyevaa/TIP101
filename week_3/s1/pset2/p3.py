vowels = 'aeiyu'
def vowel_count(s):
    count_v = 0
    for i in s.lower():
        if i in vowels:
            count_v += 1
    return count_v


def main():
    my_str = "hello world"
    my_str2 = "aAaAaAaAAA"
    my_str3 = "ths strng s mssng vwls"

    count1 = vowel_count(my_str)
    print(count1)
    count2 = vowel_count(my_str2)
    print(count2)
    count3 = vowel_count(my_str3)
    print(count3)

main()