from tokenize import Token


from Token import Token

class Parser:
    def __init__(self, tokens_list):
        self.tokens_list = tokens_list

    def parse(self):
        lt_buf = str()
        words = list()
        was_lt = False

        for t in self.tokens_list:
            if type(t) == Token:
                match t.type:
                    case "LT":
                        if not was_lt:
                            lt_buf = ''

                        lt_buf = lt_buf + t.value

                        was_lt = True

                    case "SPACE":
                        was_lt = False
                        words.append(lt_buf)
                        lt_buf = ''

        if was_lt:
            was_lt = False
            words.append(lt_buf)                
            lt_buf = ''

        return words