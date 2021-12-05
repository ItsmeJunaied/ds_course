''' Task1'''
class Nodestack:
    stack = []
    pointer = -1

    def push(self, element):
        self.stack = self.stack + [element]
        self.pointer += 1

    def peek(self):
        return self.stack[-1]

    def pop(self):
        val = self.stack[-1]
        self.stack = self.stack[:-1]
        self.pointer -= 1
        return val


print("----------------------------------------------")

def brackets(str):
    new_stack = Nodestack()
    old_stk = Nodestack()
    left_brkt = ["(", "{", "["]
    right_brkt = [")", "}", "]"]
    count = 1
    for i in str:
        if i in left_brkt:
            new_stack.push(i)
            old_stk.push(count)
        if i in right_brkt:
            if new_stack.pointer == -1:
                print("This expression is NOT correct.")
                print(f"Error at character #{count}. '{i}'-not opened.")
                return
            else:
                pred = False
                j = new_stack.pop()
                k = old_stk.pop()
                if j == "(" and i == ")":
                    pred = True
                elif j == "{" and i == "}":
                    pred = True
                elif j == "[" and i == "]":
                    pred = True
                else:
                    pred = False

                if pred!= True:
                    print("This expression is not correct")
                    print(f"Error at character #{j}. '{k}'-closed.")
                    return
        count += 1

    if new_stack.pointer == -1:
        print("This expression is correct")
        return
    else:
        print("This expression is not correct")
        while new_stack.pointer != -1:
            m = new_stack.pop()
            print(f"Error at #char. '{m}'- not closed.")
            print(count)
            new_stack.pointer -= 1
        return


brackets('1+2]*[3*3+{4–5(6(7/8/9)+10)–11+(12*8)]+14')


''' Task2'''

class Node:
    def __init__(self, data, next):
        self.data = data
        self.next = next


class Stack:
    head = None
    pointer = -1

    def push(self, data):
        if self.head == None:
            self.head = Node(data, None)
            self.pointer += 1
        else:
            n = Node(data, None)
            n.next = self.head
            self.head = n
            self.pointer += 1

    def peek(self):
        return (self.head.data)

    def pop(self):
        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.pointer -= 1
        return temp.data


print("----------------------------------------------")

def brackets(str):
    new_stack = Nodestack()
    old_stk = Nodestack()
    left_brkt = ["(", "{", "["]
    right_brkt = [")", "}", "]"]
    count = 1
    for i in str:
        if i in left_brkt:
            new_stack.push(i)
            old_stk.push(count)
        if i in right_brkt:
            if new_stack.pointer == -1:
                print("This expression is NOT correct.")
                print(f"Error at character #{count}. '{i}'-not opened.")
                return
            else:
                pred = False
                j = new_stack.pop()
                k = old_stk.pop()
                if j == "(" and i == ")":
                    pred = True
                elif j == "{" and i == "}":
                    pred = True
                elif j == "[" and i == "]":
                    pred = True
                else:
                    pred = False

                if pred != True:
                    print("This expression is NOT correct.")
                    print(f"Error at character #{j}. '{k}'-closed.")
                    return
        count += 1

    if new_stack.pointer == -1:
        print("This expression is correct.")
        return
    else:
        print("This expression is NOT correct.")
        while new_stack.pointer != -1:
            m = new_stack.pop()
            print(f"Error at #char. '{m}'- not closed.")
            print(count)
            new_stack.pointer -= 1
        return


brackets("1+2*[3*3+{4–5(6(7/8/9)+10)–11+(12*8)]+14")