def perfect(n):
    sum_divisor = 0
    for x in range(1, n):
        if n % x == 0:
            sum_divisor += x
    if sum_divisor == n:
        return True
    else:
        return False


print(perfect(6))
print(perfect(1000))
print(perfect(10000))
