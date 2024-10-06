# def pangram(string):
#     alphabet = 'abcdefghijklmnopqrstuvwxyz'
   
    
#     string = list(set(string))
#     #print(string)
#     count = 0
#     for i in range(0, len(string)):
#         for j in range(0, len(alphabet)):
#             if string[i] == alphabet[j]:
#                 #print(string[i])
#                 count += 1
#     if count == 26:
#         return True
#     else:
#         return False 

def pangram(string):
    alphabet = set('abcdefghijklmnopqrstuvwxyz')  # Step 1
    return alphabet.issubset(set(string.lower()))  # Step 2

    

if '__main__' == __name__:
    string = "The quick brown fox jumps over the lazy dog"
    print(f'Input: {string}')
    print(f'It is pangram: {pangram(string)}')

    string = "The dog jumped"
    print(f'Input: {string}')
    print(f'It is pangram: {pangram(string)}')