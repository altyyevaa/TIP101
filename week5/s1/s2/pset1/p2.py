class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next
    def assign(self, next_node):
        self.next = next_node
		

def main():
    my_list = ["Jigglypuff", "Wigglytuff"]
    node_1 = Node(my_list[0])
    node_2 = Node(my_list[1])

    node_1.assign(node_2)
    print(node_1.value, "->", node_1.next.value)
    print(node_2.value, "->", node_2.next)

main()