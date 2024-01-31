import operator
from ast import literal_eval
class Solution:
    
    OPERATORS = {"+":operator.add, "-":operator.sub, "*":operator.mul, "/":operator.truediv}

    def evalRPN(self, tokens: list[str]) -> int:

        operands = []
        currentResult = None
        for i in tokens:
            if i not in self.OPERATORS:
                operands.append(i)
                
            else: 
                
                if currentResult != None: 
                    operands.append(currentResult)
                    
                currentResult = self.binOp(*operands,i)
                operands.clear()

        return currentResult
        
    def binOp(self, x, y, op):
        return self.OPERATORS[op](int(x),int(y))


        
calc = Solution()
tokens1 = ["2","1","+","3","*"]
tokens2 = ["4","13","5","/","+"]
tokens3 = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
print(f"La solucion para los tokens {tokens1} es {calc.evalRPN(tokens1)}")

#print(type(operator.add(3,2)))


