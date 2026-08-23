class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        myStack = []
        # Plus (+): 43 Hyphen/Minus (-): 45 Slash (/): 47 Asterisk (*): 42

        for token in tokens:
            if token == "+":
                varA = myStack.pop()
                varB = myStack.pop()
                myStack.append(varB + varA)
            elif token == "-":
                varA = myStack.pop()
                varB = myStack.pop()
                myStack.append(varB - varA)
            elif token == "/":
                varA = myStack.pop()
                varB = myStack.pop()
                myStack.append(int(varB / varA))
            elif token == "*":
                varA = myStack.pop()
                varB = myStack.pop()
                myStack.append(varB*varA)
            else:
                myStack.append(int(token))
        return myStack[-1]
    
        
