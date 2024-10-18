class Node:
	def __init__(self, value, next=None):
		self.value = value
		self.next = next
		
		
def add_first(head, new_node):
	pass
    #It should insert new_node as the new head of the linked_list. The function returns new_node.
	new_node.next = head
	

def main():
	# Using the Linked List from Problem 2
    my_list = ["Jigglypuff", "Wigglytuff"]
    node_1 = Node(my_list[0])
    print(node_1.value, "->", node_1.next.value)

    new_node = Node("Ditto")
    node_1 = add_first(node_1, new_node)

    print(node_1.value, "->", node_1.next.value)
    #Jigglypuff -> Wigglytuff 
    #Ditto -> Jigglypuff

main()