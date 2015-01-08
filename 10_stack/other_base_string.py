from stack import Stack

def base_converter(dec_number, base):
    digits = '0123456789ABCDEF'
    reminder_stack = Stack()

    while dec_number > 0:
        reminder = dec_number % base
        reminder_stack.push(reminder)
        dec_number = dec_number // base

    base_string = ""
    while not reminder_stack.isEmpty():
        base_string = base_string + digits[reminder_stack.pop()]

    return base_string

if __name__ == "__main__":
    print base_converter(25,2)
    print base_converter(25,16)
