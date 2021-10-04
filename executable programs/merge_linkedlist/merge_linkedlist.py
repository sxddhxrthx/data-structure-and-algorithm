from node import Node
from linkedlist import LinkedList

list_a = LinkedList()
node_a1 = Node(2)
node_a2 = Node(5)
node_a3 = Node(7)
list_a.head = node_a1
list_a.append(node_a2)
list_a.append(node_a3)
list_a

list_b = LinkedList()
node_b1 = Node(3)
node_b2 = Node(11)
list_b.head = node_b1
list_b.append(node_b2)
list_b

print("List A: ", list_a)
print("List B: ", list_b)


def merge_lists(head_a: Node, head_b: Node) -> Node:

    dummy_node = tail = Node()

    while True:

        if head_a is None:
            tail.next = head_b
            break
        if head_b is None:
            tail.next = head_a
            break

        if head_a.data <= head_b.data:
            tail.next = head_a
            head_a = head_a.next
        else:
            tail.next = head_b
            head_b = head_b.next
        tail = tail.next

    return dummy_node.next


list_a.head = merge_lists(node_a1, node_b1)
print("Merged List: ",list_a)