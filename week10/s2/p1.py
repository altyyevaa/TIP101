"""Given an integer array nums, return True if any value appears at least twice in the array, 
and return False if every element is distinct."""

def contains_duplicate(nums):
    listCopy = set()

    listCopy.update(nums)
    print("List has:", nums)
    print("Set has:", listCopy)
    # Instance where there are duplicate numbers
    if len(nums) > len(listCopy):
        return True
    
    else:
        return False
    

list1 = [1, 2, 3, 4, 4]
list2 = []
list3 = [1,2,3]
print("Contains duplicate: List 1 - ", contains_duplicate(list1)) 
print("Contains duplicate: List 2 - ", contains_duplicate(list2))
print("Contains duplicate: List 3 - ", contains_duplicate(list3))


#UMPIRE:
#U: we have an array that contains integers, and we have to check if some number in the array appears more than one.
# if it does, we return true, if it doesn't we return false. 
#M: dictionary -> {"1" : 2, "2" : 1} - key-value pairs
#P: initiate an empty dictionary
 #  Loop through the array: 
 #      keep track of each number's frequency in an array by updating the dict
 #      return dict
 # Loop through the dict:
 #     if any key has a value greater than 1
 #        return false
 #      else return