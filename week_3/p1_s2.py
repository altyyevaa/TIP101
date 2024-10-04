#Write a function sum_of_number_strings() that takes in a list of strings nums. Each string is a representations of integers. 
# The function should return the sum of these strings as an integer.
def sum_of_number_strings(nums):
    pass
    #initialize a 'sum' variable that can take the sum of all ints
    #loop through the list:
        #convert the string at i into integer
        #increment sum
    #return sum
    sum = 0
    for i in range(len(nums)): #returns values at index i 
        # i = int(i)
        # sum += i
        sum += int(nums[i]) 
    return sum


def main():
    nums = ["10", "20", "30"]
    sum = sum_of_number_strings(nums)
    print(sum)

main()