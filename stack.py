class s21_stack:

    def __init__(self):
        self.stack = []

    def append(self, value):
        self.stack.append(value)

    def pop(self):
        return self.stack.pop()

    def back(self):
        elem = self.stack.pop()
        self.stack.append(elem)
        return elem

    def front(self):
        return self.stack[0]

    def copy(self, l: list):
        self.stack = l

    def clear(self):
        self.stack = []

    def get_list(self):
        return self.stack.copy()


