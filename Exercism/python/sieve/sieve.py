def primes(limit: int) -> list:
    """
    Get a list of prime numbers for the given limit using Sieve of Eratosthenes

    :param:
    limit: int

    :return:
    primes: list
    """
    if limit >= 2:
        a = [True] * limit
        a[0] = a[1] = False
        prime_numbers = list()

        for (i, is_prime) in enumerate(a):
            if is_prime:
                prime_numbers.append(i)
                for n in range(i * i, limit, i):  # Mark factors non-prime
                    a[n] = False

        return prime_numbers
    else:
        return list()
