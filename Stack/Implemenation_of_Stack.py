class Stack:
    def __init__(self):
        self.data = []

    def push(self,item):
        self.data.append(item)

    def isEmpty(self):
        return self.data == []

    def poping(self):
        if self.isEmpty():
            return "Stack is empty"
        return self.data.pop()
    
    def length(self):
        return len(self.data)
    

S = Stack()
S.push(5)
S.push(10)
S.push(15)
S.push(20)
while not S.isEmpty():
    print(S.poping())

    
