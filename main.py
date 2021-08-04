import pygame
import sys
import random
import time
from arrayvisualizer import ArrayVisualize
from Sorters.sorter import QuickSort

N = 600
W = 2
BLACK = 0, 0, 0


def mainloop():
    pygame.init()
    data = [i for i in range(N)]
    screen = pygame.display.set_mode((N * W, N))
    screen.fill(BLACK)
    visualizer = ArrayVisualize(data, screen, W)
    sorter = QuickSort(data)
    start = False

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN and event.key == 32:
                random.shuffle(data)
                sorter.reset()
                visualizer.visualize_data()
            if event.type == pygame.KEYDOWN and event.key == 13:
                start = True

        while start:
            sorter.step()
            visualizer.visualize_data()
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN and event.key == 27:
                    start = False
            if sorter.isFinished():
                start = False
        pygame.display.flip()


if __name__ == "__main__":
    mainloop()
