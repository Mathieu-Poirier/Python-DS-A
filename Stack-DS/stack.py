class StackDS:
    
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        self.items.pop()

    
    def is_empty(self):
        return len(self.items) == 0

    def peek(self):
        if(len(self.items) == 0):
            print("Stack is empty...")
        else:
            return self.items[-1]
    
    def __repr__(self):
        return "".join(str(self.items))

def stackBuilder(num):
    memStack = StackDS()
    memStack.push(num)
    return memStack

def testCase():
    testStack = stackBuilder(4)
    assert testStack.peek() == 5

testCase()