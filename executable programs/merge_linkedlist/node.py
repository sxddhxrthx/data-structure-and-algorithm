class Node:
    def __init__(self, data=0):
        self.data = data
        self.next = None

    def __repr__(self):
        return self.data

    def __str__(self):
        return str(self.data)
