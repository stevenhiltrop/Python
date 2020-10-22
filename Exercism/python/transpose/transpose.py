import itertools


def transpose(s) -> str:
    a = itertools.zip_longest(*s.splitlines(), fillvalue='$')
    return '\n'.join(''.join(w).rstrip('$').replace('$', ' ') for w in a)
