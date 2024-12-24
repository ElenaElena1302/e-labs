def max_of_two_num(n,m):
    if n > m:
        return n
    else:
        return m
a = int(input("Enter 1 number:"))
b = int(input("Enter 2 number:"))
x = max_of_two_num(a, b)
print("Maximum of", a, "and", b, "is", x)