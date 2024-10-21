class Node:
	def __init__(self, value, next=None):
		self.value = value
		self.next = next
		
def main():
	
    node_4 = Node("Toad", next=None)
    node_3 = Node("Wario", next=node_4)
    node_2 = Node("Luigi", next=node_3)
    node_1 = Node("Mario", next=node_2)
    
	 
    print(node_1.value, "->", node_1.next.value)
    print(node_2.value, "->", node_2.next.value)
    print(node_3.value, "->", node_3.next.value)
    print(node_4.value, "->", node_4.next)
	
main()