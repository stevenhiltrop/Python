def ss(number_list, n):
    found = False
    for i in number_list:
        if i == n:
            found = True
            break
    return found


numbers = range(0, 100)
print(f"size of numbers: {len(numbers)}")
s1 = ss(numbers, 2)
print(f"2 in numbers? {s1}")
s2 = ss(numbers, 202)
print(f"202 in numbers? {s2}")
