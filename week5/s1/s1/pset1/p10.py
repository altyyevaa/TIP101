class Node:
	def __init__(self, value, next=None):
		self.value = value
		self.next = next
		
def main():
    node_one = Node("a", next=None)
    node_two = Node("b", next=None)
    node_one.next = node_two
    
    # print(node_one.value) 
    # print(node_one.next) 
    # print(node_two.value)
    # print(node_two.next) 
    print(node_one.value)
    print(node_one.next.value)
    print(node_two.value)

main()