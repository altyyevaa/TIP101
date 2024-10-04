
def firstLastWord(word):
    first = word[0]
    last = word[-1]
    inverval = word[1:-1]
    return last + inverval + first

if __name__ == "__main__":
    word = 'boat'
    word = 'hello'
    print(f'Input: {word}')
    print(f'Output: {firstLastWord(word)}')

def paragram(string):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
   
    
    string = list(set(string))
    #print(string)
    count = 0
    for i in range(0, len(string)):
        for j in range(0, len(alphabet)):
            if string[i] == alphabet[j]:
                #print(string[i])
                count += 1
    if count == 26:
        return True
    else:
        return False 
    return

if '__main__' == __name__:
    string = "The quick brown fox jumps over the lazy dog"
    print(f'Input: {string}')
    print(f'It is paragram: {paragram(string)}')

    string = "The dog jumped"
    print(f'Input: {string}')
    print(f'It is paragram: {paragram(string)}')