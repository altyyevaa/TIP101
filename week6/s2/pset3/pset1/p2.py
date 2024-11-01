
"""Steps to Solve the Problem
Detect Cycle:

Initialize tortoise and hare to the head of the list.
Move tortoise by one step and hare by two steps in each iteration.
If tortoise and hare meet, a cycle exists; if hare reaches the end (None), there’s no cycle, so return None.
Find Cycle Start:

If a cycle is detected, reset tortoise to head.
Move both tortoise and hare one step at a time until they meet again. This meeting point is the start of the cycle.
Identify Last Node in the Cycle:

After finding the start of the cycle, use one pointer to traverse until it reaches the node that points back to the cycle start.
This node is the last node in the cycle."""

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def find_last_node_in_cycle(head):
    slow = head
    fast = head
    has_cycle = False

    while fast and fast.next: # 1->2 ->3 ->4 ->5
        slow = slow.next          # Move tortoise by 1 step
        fast = fast.next.next             # Move hare by 2 steps
        if slow == fast:              # Cycle detected
            has_cycle = True
            break
  #no cycle detected return none:
    if not has_cycle:
        return None

#Step 3: Find the start of the cycle:
    slow = head                      # Move tortoise back to head
    while slow != fast:
        slow = slow.next         # Move both by 1 step
        fast = fast.next

 # Step 4: Find the last node in the cycle
    last_node = fast
    while last_node.next != fast:
        last_node = last_node.next

    return last_node


def main():
    """Example Input: num1 -> num2 -> num3 -> num4 -> num2

    Example Output: num4"""
    num1 = Node(1)
