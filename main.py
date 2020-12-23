import pygame
import random
from bubble_sort import bubble_sort
from quick_sort import quick_sort
from merge_sort import merge_sort
from heap_sort import heap_sort

pygame.init()

#loading the font
myFont = pygame.font.SysFont("monospace",35,True)

class Visualiser():

    def __init__(self):
        self.size = (1000,800)
        self.screen = pygame.display.set_mode(self.size)
        self.array = []
        self.red = [] #The indexes of the red elements

    def update_screen(self):

        #Background color
        self.screen.fill('#FFFFFF')

        #Drawing the rectangles
        for i in range(len(self.array)):
            if i in self.red:
                pygame.draw.rect(self.screen, '#FF0000', (250 + i*10, (self.size[1] - 20) - self.array[i]*10, 5, self.array[i]*10))
            else:
                pygame.draw.rect(self.screen, '#000000', (250 + i*10, (self.size[1] - 20) - self.array[i]*10, 5, self.array[i]*10))

        #Drawing the buttons
        bubble_sort_text = myFont.render('Bubble Sort',1,(0,0,0)) 
        self.screen.blit(bubble_sort_text,(5,5))

        quick_sort_text = myFont.render('Quick Sort',1,(0,0,0)) 
        self.screen.blit(quick_sort_text,(5,55))

        merge_sort_text = myFont.render('Merge Sort',1,(0,0,0)) 
        self.screen.blit(merge_sort_text,(5,105))

        heap_sort_text = myFont.render('Heap Sort',1,(0,0,0)) 
        self.screen.blit(heap_sort_text,(5,155))

        shuffle_text = myFont.render('Shuffle',1,(0,0,0)) 
        self.screen.blit(shuffle_text,(5,750))

        pygame.display.update()


    def create_array(self):
        #Creating the initial array
        
        nums = list(range(1,71))
        self.array = []

        for i in range(len(nums)):
            choice = random.choice(nums)
            
            while choice in self.array:
                choice = random.choice(nums)
            
            self.array.append(choice)
    
    def run(self):
        pygame.display.set_caption("Sorting Visualiser")
        
        cont = True

        self.create_array()
        while cont:

            pygame.time.delay(100)

            #Closing the window
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    cont = False

            #Checking mouse clicks for launching the osrting algorithms
            if pygame.mouse.get_pressed()[0]:
                x,y = pygame.mouse.get_pos()

                if  x <= 200 and y <= 50: #Bubble sort button
                    bubble_sort(self.array, self.red, self.update_screen)
                elif x <= 200 and y >= 50 and y <= 100: #Quick sort button
                    quick_sort(self.array, 0, len(self.array)-1, self.red, self.update_screen)
                elif x <= 200 and y >= 100 and y <= 150: #Merge sort button
                    array_copy = self.array[:]
                    merge_sort(array_copy, self.red, self.update_screen, self.array)
                elif x <= 200 and y >= 150 and y <= 200: #Heap sort button
                    heap_sort(self.array, self.red, self.update_screen)
                elif x <= 200 and y >= 750: #Shuffle button
                    self.create_array()

            self.update_screen()

if __name__ == '__main__':
    visu = Visualiser()
    visu.run()
