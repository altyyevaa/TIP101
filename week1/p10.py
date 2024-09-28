#Write a function get_last() that takes in a list as a parameter and returns the last item in the list. 
# Return None if the list is empty.

def get_last(lst):
        if lst == []:
             return None
        else:
             return lst[len(lst) - 1]


def main():
    my_list = [1,2,3,4,5]
    print(get_last(my_list))

if __name__ == '__main__':
    main()



