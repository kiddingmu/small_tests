from stack import Stack

def divide_by2(dec_number):
    reminder_stack = Stack()

    while dec_number > 0:
        reminder = dec_number % 2
        reminder_stack.push(reminder)
        dec_number = dec_number // 2

    bin_string = ""
    while not reminder_stack.isEmpty():
        bin_string = bin_string + str(reminder_stack.pop())

    return bin_string


if __name__ == "__main__":
    print divide_by2(42)
