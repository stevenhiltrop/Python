def get_factors(value: int) -> list:
    """
    Get factors from given value

    :param
    value: int

    :return:
    factors: list
    """
    return list([divmod(value, number)[0], number] for number in range(1, value + 1) if value % number == 0)


def get_palindromes(products: list) -> list:
    """
    Get palindromes out of a given list of numbers

    :param:
    products: list

    :return:
    list
    """
    return list(number for number in products if str(number) == str(number)[::-1])


def get_products(max_factor: int, min_factor: int) -> list:
    """
    Calculate the products of a given range of numbers

    :params:
    max_factor: int
    min_factor: int

    :return:
    products: list
    """
    return list(set(i * j for i in range(min_factor, max_factor + 1) for j in range(min_factor, max_factor + 1)))


def largest(max_factor: int, min_factor=0) -> tuple:
    """
    Largest palindrome

    :params:
    max_factor: int
    min_factor: int [default=0]

    :return:
    largest_palindrome: tuple
    """
    products = get_products(max_factor, min_factor)
    palindromes = get_palindromes(products)


def smallest(max_factor: int, min_factor=0) -> tuple:
    """
    Largest palindrome

    :params:
    max_factor: int
    min_factor: int [default=0]

    :return:
    largest_palindrome: tuple
    """
    products = get_products(max_factor + 1, min_factor)
    palindromes = get_palindromes(products)
    value = min(palindromes)
    factors = get_factors(value)
    return tuple(value, factors)
