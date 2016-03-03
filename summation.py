n_str = raw_input("Enter a natural number: ")
n = int(n_str)

factorial  = 1
i = 1
while i <= n:
    print i, factorial
    factorial *= i
    i += 1

print factorial
