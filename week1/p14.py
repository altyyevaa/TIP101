#Write a function print_negatives() that takes a 
#list of integers lst and prints all negative numbers in the list.

def print_negatives(lst):
    #for i in range(len(lst)):
    found_negative = False
    for i in lst:
        if i < 0:
            found_negative = True
            print(i)
    if found_negative == False:
        print(None)



    
        


def main():
    lst = [1, 2, -3, -4, 6, -20]
    print_negatives(lst)


if __name__ == '__main__':
    main()
