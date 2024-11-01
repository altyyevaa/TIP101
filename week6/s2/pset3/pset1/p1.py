class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def is_circular(head):
    if not head:
        return False

    current = head
    while current.next:  # Traverse the list until we reach the end or find a cycle
        if current.next == head:  # If next node points back to head, it's circular
            return True
        current = current.next

    return False  # If we reach a node with no next, it's not circular

# Example: Create a circular linked list: num1 -> num2 -> num3 -> num1
num1 = Node(1)
num2 = Node(2)
num3 = Node(3)
num1.next = num2
num2.next = num3
num3.next = num1  # Making the list circular

print(is_circular(num1))  # Should print True