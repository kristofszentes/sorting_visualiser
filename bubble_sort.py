import pygame

def bubble_sort(array, red, update):

    swapped = True
    
    while swapped:
        
        swapped = False
        
        for i in range(len(array)-1):
            red += [i, i+1]
            update()
            pygame.time.delay(10)

            if array[i] > array[i+1]:

                array[i], array[i+1] = array[i+1], array[i]

                swapped = True

                update()

            pygame.time.delay(10)
            red.pop()
            red.pop()
    return None