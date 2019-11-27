def factorial(n):
    # state a base case of if n equals zero
    if n == 0:
        # return 1
        return 1
    # return n multiplied by factorial called with n - 1
    return n * factorial(n - 1)
