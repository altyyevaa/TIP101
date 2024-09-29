
def is_subsequence(lst, sequence):
    result = []
    for i in range(len(sequence)):
        for j in range(len(lst)):
            if sequence[i] == lst[j]:
                result.append(lst[j]) 
        return True
    else:
        return False

def is_subsequence(lst, sequence):
    j = 0
    for i in range(len(lst)):
        if lst[i] == sequence[j]:
            j += 1
        if j == len(sequence):
            return True
    return False
        
        

lst = [5, 1, 22, 25, 6, -1, 8, 10]
sequence = [1, 6, -1, 10]
print(is_subsequence(lst, sequence))
    
           
def main():
  lst = [5, 22, 25, 6, -1, 8, 10, 1]
  sequence = [6, -1]
  print(is_subsequence(lst, sequence))

if __name__ == "__main__":
    main()
