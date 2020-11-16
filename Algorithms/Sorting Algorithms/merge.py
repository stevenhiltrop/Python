def merge_sort(our_list, left, right):  # left and right corresponds to starting and ending element of ourlist
    if right - left > 1:  # check if the length of our_list is greater than 1
        middle = (left + right) // 2  # we divide the length in two parts
        merge_sort(our_list, left, middle)  # recursively I call the merge_sort function from left to middle
        merge_sort(our_list, middle, right)  # then from middle to right
        merge_list(our_list, left, middle, right)  # finally I create our_list in complete form(left, middle and right)


def merge_list(our_list, left, middle, right):  # I create the function merged_list
    left_list = our_list[left:middle]  # I define the left_list
    right_list = our_list[middle:right]  # I define the right list
    k = left  # it is the the temporary variable
    i = 0  # this variable that correspond to the index of the first group help me to iterate from left to right
    j = 0  # this variable that correspond to the index of the second group help me to iterate from left to right
    while left + i < middle and middle + j < right:  # the condition that I want to archive before to stop my iteration
        if (left_list[i] <= right_list[j]):  # if the element in the left_list is less or equal to the element in the right_list
            our_list[k] = left_list[i]  # In this case I fill the value of the left_list in our_list with index k
            i = i + 1  # now I have to increment the value by 1
        else:  # if the above condition is not match
            our_list[k] = right_list[j]  # I fill the right_list element in our_list with index k
            j = j + 1  # I increment index j by 1
        k = k + 1  # now I increment the value of k by 1
    if left + i < middle:  # check if left + i is less than middle
        our_list[k] = left_list[i]  # I place all elements of my left_list in our_list
        i = i + 1
        k = k + 1
    else:  # otherwise if my left_list is empty
        while k < right:  # until k is less then right
            our_list[k] = right_list[j]  # I place all elements of right_list in ourlist
            j = j + 1
            k = k + 1


our_list = input('input - unordered elements: ').split()  # insert the input and split
our_list = [int(x) for x in our_list]
merge_sort(our_list, 0, len(our_list))
print('output - ordered elements: ')
print(our_list)
