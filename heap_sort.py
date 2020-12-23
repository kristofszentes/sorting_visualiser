import pygame

'''
The heap sort is easier to understand when we visualize it with a binary tree but
this is still a pretty satisfying visualization
'''
def heap_sort(array, red, update):

    end = len(array) - 1
    build_max_heap(array, red, update)

    while end > 0:

        red.extend([0,end])
        update()
        pygame.time.delay(20)

        array[end], array[0] = array[0], array[end]
        end -= 1

        red.pop()
        red.pop()
        update()
        pygame.time.delay(20)
        max_heapify(array, 0, red ,update, end)

def build_max_heap(array, red ,update):
    n = len(array)
    for i in range(n//2 , -1, -1):
        max_heapify(array, i, red, update, n - 1)

def max_heapify(array, i,  red, update, size):
    left = 2*i +1
    right = 2*i +2
    largest = i

    if left <= size and array[left] > array[largest]:
        largest = left

    if right <= size and array[right] > array[largest]:
        largest = right

    if largest != i:

        red.extend([i, largest])
        update()
        pygame.time.delay(20)

        array[i], array[largest] = array[largest], array[i]

        update()
        red.pop()
        red.pop()
        pygame.time.delay(20)

        max_heapify(array, largest, red, update, size)
