#Write a function reverse_sentence() that takes in a string sentence as a parameter and 
# returns the string with the sentence but with the order of the words reversed. 
# The sentence will only contain alphabetic characters and spaces to separate the words. 
# If there is only one word in the sentence, the function returns the original string.

def reverse_sentence(sentence):
    split = sentence.split()
    index = len(split) - 1
    for word in range(index, -1, -1):
        print(split[word], end=" ")
        

def main():
    sentence = "I solemnly swear I am up to no good"
    reverse_sentence(sentence)

main()
