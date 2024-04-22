import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from data_structures.stack import Stack

# Write a function that can reverse a string using stack
def reverseString(string):
    stack = Stack()

    for char in string:
        stack.push(char)
    for i in range(len(string)):
        print(stack.pop(), end = "")  
    print("\n")    

# Write a function that checks if parantheses are balanced
def balancedParantheses(string):
    stack = Stack()

    for char in string:
        if char in ["(", "{", "["]:
            stack.push(char)

        if char in [")", "}", "]"]:
            if stack.isEmpty(): # ending paranthesis should not be the first character
                return False
            if (char == ")" and stack.peek() == "(") or (char == "}" and stack.peek() == "{") or (char == "]" and stack.peek() == "["):
                stack.pop()
            else:
                return False
    return stack.isEmpty()


if __name__ == "__main__":
    reverseString("Hello World! This will be reversed using stack.")
    reverseString("I wish they would fix Counter Strike 2")

    bool1 = balancedParantheses("({a+b})")
    bool2 = balancedParantheses("))((a+b}{")
    bool3 = balancedParantheses("((a+b))")
    bool4 = balancedParantheses("]]abc[[")
    print(bool1, bool2, bool3, bool4)