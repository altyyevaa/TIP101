#Write a function sum_ten() that returns the sum of numbers from 1 to 10.

def sum_ten():
    sum = 0
    for i in range(1, 11):
        sum = sum + i
    return sum
      

def main():
    print(sum_ten())
    

if __name__ == '__main__':
    main()