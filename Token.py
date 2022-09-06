class Token:
    def __init__(self, type, value):
        self.type = type
        self.value = value

    def LT(x):
        res = Token("LT", x)

        return res

    def SPACE():
        res = Token("SPACE", None)

        return res

    def print_token(self):
        print(self.type + '(' + self.value + ')')