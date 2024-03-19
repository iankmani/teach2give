# Write a program that takes an integer as input and returns an integer with reversed digit
# ordering.
def reverse_integer(n):
    # Convert the integer to a string to make it echo
    num_str = str(n)
    
    
    if num_str[0] == '-':
        reversed_str = '-' + num_str[:0:-1]  # Reverse the string excluding the negative sign
    else:
        reversed_str = num_str[::-1]  # Reverse the string
    
    
    reversed_int = int(reversed_str)
    
    return reversed_int


