from stack import Stack

def parenthese_checker(symbol_string):
    s = Stack()
    balanced = True
    index = 0
    while index < len(symbol_string) and balanced:
        symbol = symbol_string[index]
        if symbol == "(":
            s.push(symbol)
        else:
            if s.isEmpty():
                balanced = False
            else:
                s.pop()

        index = index + 1

    if balanced and s.isEmpty():
        return True
    else:
        return False

if __name__ == "__main__":
    print parenthese_checker('((()))')
    print parenthese_checker('(()')
    print parenthese_checker('')
