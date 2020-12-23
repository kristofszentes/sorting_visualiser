import pygame

#This algorithm is definetely the hardest to visualize as it is hard to show how the different lists are merged
#This visualization still gives you a feel of the "divide and conquer" idea that is at the core of this algorithm

def merge_sort(array, red, update, visual_array):
    
    n = len(array)

    if n <= 1:
        return array
    
    left, right = [], []

    for i in range(n):
        if i < (n/2):
            left.append(array[i])
        else:
            right.append(array[i])

    merge_sort(right, red, update, visual_array)
    merge_sort(left, red ,update, visual_array)

    array.clear()
    array.extend(merge(right, left, red, update, visual_array))

def merge(right, left, red, update, visual_array):
    merged = []

    while right != [] and left != []:

        #We color the two compared values in red
        red.append(right[0])
        red.append(left[0])
        update()
        pygame.time.delay(10)


        if right[0] <= left[0]:
            merged.append(right.pop(0))
        else:
            merged.append(left.pop(0))

        red.pop()
        red.pop()
        update()
        pygame.time.delay(10)

    while right != []:
        merged.append(right.pop(0))
    while left != []:
        merged.append(left.pop(0))

    #The visualization of the changes
    first = min(list_of_indexes(visual_array, merged))
    for i in range(len(merged)):
        visual_array[first + i] = merged[i]

    return merged


def list_of_indexes(li, elements):
    return [li.index(x) for x in elements]
