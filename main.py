
class Input():
    def __init__(self):
        self.nums = ""

    def user_input(self):
        user_input = input("Enter a number ")
        self.nums += user_input

    def print_nums(self):
        print(f"The list of numbers: {self.nums}")

    def cont(self):
        continue_prompt = input("Would you like to add another number? Y/N ")
        if continue_prompt == "Y":
            continue_bool = True
        else:
            continue_bool = False
        return continue_bool




