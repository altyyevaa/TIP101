"""A circular linked list is a linked list where the tail node points at the head node. Write a function that returns the length of the list.

Evaluate the time and space complexity of your solution. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity."""

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def circular_list_length(head):
     # find the size of the circular linked list
     # traverse through the given linked list:
     #count the values
     #if we reach none, exit the loop 
     #and return the count of the linked list 
     counter = 0
     current = head
     while current:
         counter += 1
         current = current.next
         if current == head:
             break
     return counter

def main():
    head = Node(1)
    current = head
    

# Create the next nodes in a loop
    for i in range(2, 4):  # Adjust the range to the desired size
        current.next = Node(i)
        current = current.next

    current.next = head
    length = circular_list_length(head)
    print("Length of the circular linked list:", length)

main()

