def print_inverted_triangle(n):
    for i in range(n):
        print(' ' * i + '*' * (n - i))

n = int(input("Enter the number of rows for the triangle: "))
print_inverted_triangle(n)