def get_fibonacci_number(position):
    if position == 0:
        return 0
    if position == 1:
        return 1
    
    return get_fibonacci_number(position - 2) + get_fibonacci_number (position - 1)

def get_fibonacci_number_sequence(number):
    pass #Remove this line and insert your code here. Do not forget to use get_fibonacci_number to create your list of numbers.

if __name__ == "__main__":
    print("\nHello! Welcome to the Fibonacci Number Sequence Finder!")
    user_input = print(int(input("\n Please enter the position of the number in the Fibonacci Sequence you are asking to find: ")))

    pass