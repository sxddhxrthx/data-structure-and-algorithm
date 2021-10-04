class Stack:

    maxx = []

    def __init__(self):
        self.item = []

    def is_empty(self):
        return self.item == []

    def push(self, value):
        self.item.append(value)

    def pop(self):
        removed_element = self.item.pop()
        return removed_element

    def peak(self):
        return self.item[-1]

    def __len__(self):
        return len(self.item)

    def __repr__(self):
        return str(self.item)


def evaluate(exp_list: list) -> int:
    stack = Stack()
    operators = ['+', '-', '*', '/']
    for char in exp_list:
        if char in operators:
            op_b = stack.pop()
            op_a = stack.pop()
            result = eval(f"{op_a}{char}{op_b}")
            stack.push(result)
        else:
            stack.push(char)
    return stack.peak()


if __name__ == "__main__":
    exp = "3,4,+,2,*,1,+"
    exp = "-641,6,/,28,/"
    exp = "1,1,+,-2,*"
    exp_list = exp.split(",")
    output = evaluate(exp_list)
    print(output)
