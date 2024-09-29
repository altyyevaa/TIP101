#Write a function index_to_value_map() that takes in a list lst and returns a 
# dictionary that maps the index of each element in lst to its value.

def index_to_value_map(lst):
    final_dict = {}
    for i in range(len(lst)):
        final_dict[i] = lst[i]
        # print (f"{i} : {lst[i]}")
    return final_dict


def main():
    lst = ["apple", "banana", "cherry"]
    print(index_to_value_map(lst))

main()