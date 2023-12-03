print("{:>60}".format("* " * 25))
print("{:>11}{:^58}*".format("*", "\033[1;95mFind the smallest factor\033[0m"))
print("{:>60}".format("* " * 25), "\n")
factors = []

while True:
    num = int(input("Enter an integer: "))
    if num >= 2:
        for i in range(2, num + 1):
            if num % i == 0:
                factors.append(i)
    else:
        print("\033[91mInvalid input. Enter a number greater than 2\033[0m\n")
        continue

    smallest_factor = min(factors)
    print(f"The smallest factor other than 1 for {num} is \033[93m{smallest_factor}\033[0m\n")
    factors.clear()
