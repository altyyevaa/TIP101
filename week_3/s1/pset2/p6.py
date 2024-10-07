def find_the_needle(haystack, needle):
    index = haystack.find(needle)
    return index

    #my_draft application which doesn't work for all cases!
    #for char in range(len(haystack)): 
        # if needle[0] == haystack[char] and needle[1] == haystack[char + 1]:
        #     return char
        # elif needle not in haystack:
        #     return -1
    
    


def main():
    haystack = "tobeornottobe"
    needle = "be"
    print(find_the_needle(haystack, needle)) #output: 2

    haystack2 = "leetcode"
    needle2 = "leeto"
    print(find_the_needle(haystack2, needle2)) #output: -1

main()
