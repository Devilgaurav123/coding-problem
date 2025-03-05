def second_largest(arr):
    unique_elements=set(arr)

    sorted_elements=sorted(unique_elements,reverse=True)

    if len(sorted_elements)<2:

        return -1

    else:
        return sorted_elements[1]


