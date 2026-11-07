def check_prime(num):
    if num < 2:
        return False

    sqrt_num = num**0.5
    i = 2
    while i <= sqrt_num:
        if num % i == 0:
            return False
        i += 1
    return True

num1 = 600_851_475_143
factor = 2

while num1 != 1:
    if check_prime(factor):
        while num1 % factor == 0:
            print(num1, factor)
            num1 = num1 // factor
            continue

    factor += 1