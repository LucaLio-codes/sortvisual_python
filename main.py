import pygame
import sys
import random
from sorters.bubble import BubbleSort
from sorters.insertion import InsertionSort
from sorters.quick import QuickSort

N = 600
W = 3
BLACK = 0, 0, 0
COLOR = 245, 161, 66
HIGHLIGHT = 214, 11, 11
LEGEND = "Sorter: %s | " \
         "Time Elapsed: %f ms |" \
         "Total Operations: %d | " \
         "Current Operation: %d "


class Visualizer:

    def __init__(self):
        pygame.init()
        pygame.font.init()
        self.font = pygame.font.SysFont("Arial", 30)
        self.font.set_bold(True)
        self.data = [i for i in range(N)]
        self.screen = pygame.display.set_mode((N * W, N + 40))
        self.screen.fill(BLACK)
        self.displayData = self.data.copy()
        self.sorter = QuickSort(self.data)
        self.visualizeData()
        self.drawLegend((str(self.sorter), 0, 0, 0))
        self.op = 0
        self.time = 0

    def mainloop(self):
        while True:
            self.checkLoop()
            pygame.display.flip()

    def visualizeData(self, highlight=list()):
        for d in range(N):
            self.checkLoop()
            pos = (d*W, N - self.displayData[d] + 40)
            form = (W,  N)
            r = pygame.Rect(pos, form)
            pygame.draw.rect(self.screen, COLOR if d not in highlight else HIGHLIGHT, r)
        pygame.display.flip()

    def drawLegend(self, data):
        text = self.font.render(LEGEND % data, False, COLOR)
        self.screen.blit(text, (0, 0))

    def animate(self, stack):
        curop = 1
        while not stack.isEmpty():
            self.screen.fill(BLACK)
            i = stack.pop()
            j = stack.pop()
            self.displayData[i], self.displayData[j] = self.displayData[j], self.displayData[i]
            self.drawLegend((str(self.sorter), self.time, self.op, curop))
            self.visualizeData([i, j])
            curop += 1

    def checkLoop(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN and event.key == 32:
                self.shuffle()
                self.sorter = QuickSort(self.data)
                self.time = self.sorter.getTimeMs()
                self.drawLegend((str(self.sorter), self.time, 0, 0))
            if event.type == pygame.KEYDOWN and event.key == 13:
                self.op = self.sorter.getOperations()
                stack = self.sorter.getStack()
                self.animate(stack)
            if event.type == pygame.KEYDOWN and event.key == 27:
                self.mainloop()

    def shuffle(self):
        self.screen.fill(BLACK)
        random.shuffle(self.data)
        self.displayData = self.data.copy()
        self.visualizeData()


if __name__ == "__main__":
    dut = Visualizer()
    dut.mainloop()
