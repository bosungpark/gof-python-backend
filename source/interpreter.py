class AbstractExpression():
    @staticmethod
    def interpret():
        ...

class Number(AbstractExpression):

    def __init__(self, value):
        self.value = int(value)

    def interpret(self):
        return self.value

    def __repr__(self):
        return str(self.value)


class Add(AbstractExpression):
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def interpret(self):
        return self.left.interpret() + self.right.interpret()

    def __repr__(self):
        return f"{self.left} + {self.right}"


SENTENCE = "5 + 4"
TOKENS = SENTENCE.split(" ")

AST: list[AbstractExpression] = []
AST.append(Add(Number(TOKENS[0]), Number(TOKENS[2])))  # 5 + 4

AST_ROOT = AST.pop()
print(AST_ROOT)  # 5 + 4
AST_ROOT.interpret() == 9