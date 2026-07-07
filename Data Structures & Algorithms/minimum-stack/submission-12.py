class MinStack:

    def __init__(self):
        self.stack = []
        self.minimum = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.minimum == [] or val <= self.minimum[-1]:
            self.minimum.append(val)

    def pop(self) -> None:
        v = self.stack.pop()
        if v == self.minimum[-1]:
            self.minimum.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        print(self.minimum)
        return self.minimum[-1]
