import pygame

def quick_sort(array, lo , hi, red , update):
    if lo < hi:
        part = partition(array, lo, hi, red, update)
        quick_sort(array, lo , part-1, red, update)
        quick_sort(array, part+1, hi, red, update)

def partition(array, lo , hi, red, update):
    pivot = array[hi]
    i = lo
    for j in range(lo, hi+1):

        red += [i, j]
        update()
        pygame.time.delay(10)

        if array[j] < pivot:
            
            array[i],array[j] = array[j], array[i]
            i += 1

            update()
            pygame.time.delay(10)

        red.pop()
        red.pop()

    red += [i,hi]
    array[i], array[hi] = array[hi], array[i]
    
    update()
    pygame.time.delay(10)
    red.pop()
    red.pop()

    return i