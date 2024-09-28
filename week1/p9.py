#Write a function get_first() that takes in a list as a parameter and returns 
# the first item in the list. Return None if the list is empty

def get_first(lst):
    return lst[0]

def main():
    lst =[1,2.3,4]
    print(get_first(lst))

if __name__ == '__main__':
    main()
