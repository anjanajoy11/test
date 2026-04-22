term = input("Enter a string: ")
if term == term[::-1]:
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")


n = int(input("Enter a number: "))
a = 0
b = 1

print("The Fibonacci sequence up to", n, "is:")
for i in range(n):
    print(a, end=' ')
    c = a + b
    a = b
    b = c