# write a function that returns the number of prime numbers that exist up to
# and including a given number
def count_primes(num):
    if num < 2:
        return 0

    primes = [2]
    x = 3

    while x <= num:
        for y in primes:
            if x % y == 0:
                x += 2
                break
        else:
            primes.append(x)
            x += 2

    print(primes)
    return primes

count_primes(50)
