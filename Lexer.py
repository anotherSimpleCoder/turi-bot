from curses.ascii import isalpha, isspace
from Token import Token


class Lexer:
    def lex(self, input_string):
        tokens = list()
        for c in input_string:
            res = self.char_to_token(c)
            tokens.append(res)

        return tokens


    def char_to_token(self, char):
        if isspace(char):
            return Token.SPACE()

        elif isalpha(char):
            return Token.LT(char)


        