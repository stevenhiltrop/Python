def bubble_sort(our_list):  # I create my function bubble_sort with the argument called our_list
    b = len(our_list) - 1  # for every list, I will have a minus 1 iteration
    for x in range(b):  # for each element in the range of b, I check if they are ordered or not
        for y in range(b - x):
            if our_list[y] > our_list[y + 1]:  # if one element is greater than the nearest element in the list
                our_list[y], our_list[y + 1] = our_list[y + 1], our_list[y]  # I have to swap the elemnts, in other words
                # I exchange the position of the two elements
        return our_list


our_list = [15, 1, 9, 3]
print(bubble_sort(our_list))
