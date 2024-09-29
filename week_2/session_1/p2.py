# Write a function create_dictionary() that takes in a list of keys and a list of values as parameters. 
# The function returns a dictionary where each item in keys is paired with a corresponding item in values.
# keys[i] should be paired with values[i] in the dictionary where 0 <= i <= len(keys). You may assume keys and values are the same length.

def create_dictionary(keys, values):
    for i in range(len(keys)):
        dictionary = dict(zip(keys, values))
        return dictionary

def main():
    keys = ["peanut", "dragon", "star", "pop", "space"]
    values = ["butter", "fly", "fish", "corn", "ship"]
    print(create_dictionary(keys, values))

main()