


class LinkedList:
    def __init__(self):
        self.head = None

    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(str(node))
            node = node.next
        #         nodes.append("None")
        #         return str(nodes)
        return " -> ".join(nodes)

    # traversing the LinkedList
    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next

    def insert_after(self, node, new_node):  # O(1)
        new_node.next = node.next
        node.next = new_node

    def insert_before(self, node, new_node):  # O(n)
        for _ in self:
            if _.next == node:
                _.next = new_node
                new_node.next = node

    def append(self, new_node):  # O(n)
        for _ in self:
            pass
        _.next = new_node

    def prepend(self, new_node):  # O(1)
        new_node.next = self.head
        self.head = new_node

    def delete(self, node):  # O(n)
        for _ in self:
            if _.next == node:
                _.next = node.next

    def head_(self):
        return self.head

    def tail(self):
        for _ in self:
            pass
        return _

