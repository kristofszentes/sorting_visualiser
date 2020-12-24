import pygame

def insertion_sort(array, red, update):
    for i in range(1,len(array)):
        j = i
        while j > 0 and array[j-1] > array[j]:
            
            red.extend([j-1, j])
            update()
            pygame.time.delay(10)

            array[j], array[j-1] = array[j-1], array[j]

            update()
            pygame.time.delay(10)
            red.pop()
            red.pop()
            j -= 1
        