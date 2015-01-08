from stack import Stack

def parenthese_checker(symbol_string):
    s = Stack()
    balanced = True
    index = 0
    while index < len(symbol_string) and balanced:
        symbol = symbol_string[index]
        if symbol in "([{":
            s.push(symbol)
        else:
            if s.isEmpty():
                balanced = False
            else:
                top = s.pop()
                if not matches(top, symbol):
                    balanced = False
        index = index + 1
    if balanced and s.isEmpty():
        return True
    else:
        return False

def matches(open_symbol, close_symbol):
    opens = "([{"
    closers = ")]}"
    return opens.index(open_symbol) == closers.index(close_symbol)

if __name__ == "__main__":
    print parenthese_checker('{{([][])}()}')
    print parenthese_checker('[{()]')
