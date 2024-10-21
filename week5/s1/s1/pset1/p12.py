class Node:
	def __init__(self, value, next=None):
		self.value = value
		self.next= next
		
def print_linked_list(head):
    result = []
    current_node = head
    while current_node is not None:
        result.append(current_node.value)  # Add the current node's value to the list
        current_node = current_node.next
    
    # Join the values with " -> " and print the final result
    print(" -> ".join(result))


def main():
    node_e = Node("e", next= None)
    node_d = Node("d", next = node_e )
    node_c = Node("c", next= node_d)
    node_b = Node("b", next = node_c)
    node_a = Node("a", next= node_b)
        
    print_linked_list(node_a)

main()