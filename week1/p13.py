#Write a function sum_positive_range() that returns the sum of numbers 
# from 1 to a given stop value (inclusive).

def sum_positive_range(stop):
    sum = 0
    for i in range(1, stop+1):
        sum = sum + i
    return sum
    
def main():
    s = sum_positive_range(6)
    print(s)
    
    

if __name__ == '__main__':
    main()