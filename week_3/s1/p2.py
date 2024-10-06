
def firstLastWord(word):
    first = word[0]
    last = word[-1]
    inverval = word[1:-1]
    return last + inverval + first

if __name__ == "__main__":
    word = 'boat'
    #word = 'hello'
    print(f'Input: {word}')
    print(f'Output: {firstLastWord(word)}')