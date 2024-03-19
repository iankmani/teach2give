def reverse_integer(n):
    # Convert the integer to a string to make it iterable
    num_str = str(n)
    
    # Handle negative numbers
    if num_str[0] == '-':
        reversed_str = '-' + num_str[:0:-1]  # Reverse the string excluding the negative sign
    else:
        reversed_str = num_str[::-1]  # Reverse the string
    
    
    reversed_int = int(reversed_str)
    
    return reversed_int

#examples given are:
print(reverse_integer(500))  # Output: 5
print(reverse_integer(-56))  # Output: -65
print(reverse_integer(-90))  # Output: -9
print(reverse_integer(91))   # Output: 19
