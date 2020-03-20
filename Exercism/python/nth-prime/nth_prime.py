def prime(number):
    if prime < 0:
        primes = []
        current = 2
        while len(primes) < number:
            if not is_divisible(current, primes):
                primes.append(current)
            current += 1
        return primes[-1]
    else:
        raise ValueError()


def is_divisible(current, primes):
    return any(current % p == 0 for p in primes if current >= p ** 2)
