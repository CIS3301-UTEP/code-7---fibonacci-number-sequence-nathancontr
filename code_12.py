def get_fibonacci_number(position):
    #used recursion example from in-class, changed variables to fit this function
    if position == 0:
        return 0
    if position == 1:
        return 1
    
    return get_fibonacci_number(position - 2) + get_fibonacci_number (position - 1)

def get_fibonacci_number_sequence(number):
    #if input is 0, there is no sequence to create
    #so it returns an empty list
    if number == 0:
        return [0]
    #the first number in the sequence is 0, so the sequence
    #doesnt need to create a list, it only returns one number
    elif number == 1:
        return [get_fibonacci_number(0), get_fibonacci_number(1)]
    #returns the first two numbers in the sequence,
    #which is 0, and 1, dont need to create a special list code
    # elif number == 2:
        # return [get_fibonacci_number(0), get_fibonacci_number(1)]
    #calls back itself, i use number-1 because the first position isnt 1,
    #it is 0
    else:
        sequence = get_fibonacci_number_sequence(number - 1)
        #the append adds the higher and higher sequence numbers
        #to the list
        #didnt use number-1 here because in testing it would give me
        #the sequence excluding the number I asked for
        sequence.append(get_fibonacci_number(number))
        return sequence

if __name__ == "__main__":
#testers
    # print(get_fibonacci_number(10))
    # print(get_fibonacci_number_sequence(10))

    print("\nHello! Welcome to the Fibonacci Number Sequence Finder!")
    user_input = int(input("\n Please enter the position of the number in the Fibonacci Sequence you are asking to find: "))
#inserts user input into both functions
    answer = get_fibonacci_number(user_input)
    sequence = get_fibonacci_number_sequence(user_input)
#outputs
    print(f"The Fibonacci number at position {user_input} is: \n{answer}")
    print(f"The Fibonacci sequence up to position {user_input} is: \n{sequence}")


    