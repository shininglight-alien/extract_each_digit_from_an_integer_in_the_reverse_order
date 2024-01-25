# Write a Program to extract each digit from an integer in the reverse order

def reverse_digits(n):
    return ' '.join(list(str(n))[::-1])

# get user input
n = int(input("Integer Entry:"))

# test the function
print(reverse_digits(n))
