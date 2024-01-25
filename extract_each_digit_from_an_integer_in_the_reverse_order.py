# Write a Program to extract each digit from an integer in the reverse order

def reverse_digits(n):
    return ' '.join(list(str(n))[::-1])

# Test the function
print(reverse_digits(7536))
