class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operatorMap = {
            "+": lambda l,r: l + r,
            "*": lambda l,r: l * r,
            "-": lambda l,r: l - r,
            "/": lambda l,r: int(l / r),
        }
        
        stack = []
        for token in tokens:
            if token in operatorMap:
                right = stack.pop()
                left = stack.pop()
                token = operatorMap[token](left, right)
            
            stack.append(int(token))
        
        return stack.pop()

        
