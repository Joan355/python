import operator

#["2","1","+","3","*"]
#((2 + 1) * 3) = 9

class Solution:
    OPERATORS = {"+":operator.add, "-":operator.sub, "*": operator.mul, "/":operator.truediv}
    def evalRPN(self, tokens: list[str]) -> int:
        opcontainer = []
        for i in tokens: 
            if i in self.OPERATORS:
                result = self.binOp(*opcontainer[-2:], i)
                opcontainer[-2:] = []
                opcontainer.append(result)
            else:
                opcontainer.append(i)
        return opcontainer[0]

    def binOp(self,x,y,op):
        return self.OPERATORS[op](int(x),int(y))  

tokens = (["2","1","+","3","*"], ["4","13","5","/","+"], ["10","6","9","3","+","-11","*","/","*","17","+","5","+"])
sol = Solution()
for token in tokens:
    print(sol.evalRPN(token))




