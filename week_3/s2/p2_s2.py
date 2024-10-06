#Write a function remove_duplicates() that takes in a sorted(***) list of integers nums as a 
# parameter and removes all duplicates in the list. The function returns the modified list(****).

def remove_duplicates(nums):
    #UPI:
    #Use for loop for looping through all elements in the list
            #while i is not only once in the list: (true) -> false
                #keep removing the other numbers that are equal to i
                #update the list -> nums = nums(removed version)
        #return nums
    i = 0
    for j in range(len(nums)):
        if nums[i] != nums[j]:
            nums[i] = nums[j]




        
    #     while (nums[i] == nums[i+1]):
    #       nums = nums.pop()
    # return nums
        

        

 

def main():
    nums = [1,1,1,2,3,4,4,5,6,6]
    #no_dups = [1,2,3,4,5,6]
    print(remove_duplicates(nums))


main()


