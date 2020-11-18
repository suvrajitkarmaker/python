class Stack:
    def __init__(self):
        self.stack = []
        self.top = 0
        self.stackSize = 1000000
    
    def push(self, value):
        if(self.stackSize == self.top):
            print("Stack is full")
        else:
            self.stack.append(value)
            self.top = self.top + 1
    
    def pop(self):
        value = None
        if(self.top == 0):
            print("Stack is empty")
        else:
            self.top = self.top - 1
            value = self.stack.pop()
        
        return value
    
    def display(self):
        if(self.top == 0):
            print("Stack is empty")
        else:
            i=self.top -1
            while(i>=0):
                print(self.stack[i], end=' ')
                i-=1    
            print()
st = Stack()
st.push(50)
st.push(78)
st.push(15)
st.push(89)
st.display()
print(st.pop())
st.display()
st.push(59)
st.push(73)
st.display()
print(st.pop())
st.display()