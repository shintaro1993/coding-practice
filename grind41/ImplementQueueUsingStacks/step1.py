class MyQueue:
    def __init__(self):
        self.output_stack = []
        self.buffer_stack = []

    def push(self, x: int) -> None:
        self.buffer_stack.append(x)

    def pop(self) -> int:
        if not self.output_stack:
            while self.buffer_stack:
                tmp = self.buffer_stack.pop()
                self.output_stack.append(tmp)
        return self.output_stack.pop()

    def peek(self) -> int:
        if self.output_stack:
            return self.output_stack[-1]
        return self.buffer_stack[0]

    def empty(self) -> bool:
        return not self.output_stack and not self.buffer_stack
