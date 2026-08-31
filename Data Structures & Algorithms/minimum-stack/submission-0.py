class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        #determine the new minimum value
        if not self.stack:
            current_min = val #if stack is empty, new element = new min
        else:
            current_min = min(val, self.stack[-1][1])
        self.stack.append((val, current_min))

    def pop(self) -> None:
       self.stack.pop() 

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]
