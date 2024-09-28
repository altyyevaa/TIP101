#Write a function counter() 
#that uses the range function to print numbers between 1 and a given stop value (inclusive).

def counter(stop):
    # i = stop[1]
    for i in range(1, stop+1):
        print (i)

def main():
    stop = 10
    (counter(stop))

if __name__ == '__main__':
    main()
