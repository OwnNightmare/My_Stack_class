

class Stack:
    def __init__(self):
        self.stack = []
        self.open_braces = ['(', '[', '{']
        self.close_braces = [')', ']', '}']

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if not self.is_empty():
            popped = self.stack.pop()
            return popped
        return None

    def is_empty(self):
        if len(self.stack) == 0:
            return True
        return False

    def peek(self):
        if not self.is_empty():
            return self.stack[-1]

    def size(self):
        return len(self.stack)

    def is_balanced(self, sequence: str):
        if len(sequence) == 0:
            return 'empty'
        if len(sequence) % 2 == 0:
            for i in sequence:
                if i in self.open_braces:
                    self.push(i)
                elif i in self.close_braces and len(sequence) != 0:
                    pos = self.close_braces.index(i)
                    if self.open_braces[pos] == self.peek():
                        self.pop()
                    else:
                        return 'unbalanced'
                else:
                    return 'unbalanced'
            return 'balanced'
        return 'unbalanced'


if __name__ == '__main__':
    s = Stack()
    print(s.is_balanced('({[([])]})'))





