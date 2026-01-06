# Using a stack write a Python code to reverse a string

# Recap: Stack allows insertion and deletion only from the top of the list.
# [start:stop] specifies a section of a list from the start index to the stop index but excluding the stop index
# [::step] tells Python to traverse the string from right to left instead of the usual left to right

word = "Brain"


def main():
    print(f"Word: {word}")
    print(f"Reversed: {solution()}")


def method_1():
    """ This method makes use of the slice operator. Omitting the start and stop indexing tells Python to traverse the string from right to left instead of the usual left to right """

    return word[::-1]


def method_2():
    """ This method simply extracts the items in the string starting from the last item and then joins them to form a new string """

    holder = [-i-1 for i in range(len(word))]

    rev = "".join([word[n] for n in holder])
    print(rev)


# The implementation of the solution is quite different from what I imagined. The stack in this case is used as holder.
# Begin with an empty list -> that's the stack
# Get each character from word and append to the stack
# While the stack is not empty, pop every character and build the reversed string

def solution():
    stack = [] # Represents the stack data structure
    result = []

    for char in word:
        stack.append(char)
    
    # Keep popping until the stack is empty
    while not len(stack) == 0:
        result.append(stack.pop()) # Remove and return the last item then append to result
    
    return "".join(result)


if __name__ == "__main__":
    main()