def print_pair(dictionary, target):
    for key in dictionary:
        if key == target:
            print(key, dictionary[key])
            return

def main():
    dictionary = {"spongebob": "squarepants", "patrick": "star", "squidward": "tentacles"}
    print_pair(dictionary, "patrick")
    print_pair(dictionary, "plankton")
    print_pair(dictionary, "spongebob")

main()