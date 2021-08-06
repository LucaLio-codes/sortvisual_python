import pygame
import sys
import random
import sorters.sorterFactory as sf
from util.sorttype import SortType

N = 300
W = 5
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
        self.sortType = SortType.MERGE
        self.font = pygame.font.SysFont("Arial", 30)
        self.font.set_bold(True)
        self.data = [i for i in range(N)]
        self.screen = pygame.display.set_mode((N * W, N + 40))
        pygame.display.set_caption("Sorting Visualized")
        self.screen.fill(BLACK)
        self.displayData = self.data.copy()
        self.sorter = sf.getSorter(self.sortType, self.data)
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
            test = (self.displayData[d] / max(self.data)) * 360
            color = pygame.Color(0,0,0)
            color.hsva = (test, 100, 100)
            pygame.draw.rect(self.screen, color if d not in highlight else HIGHLIGHT, r)
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
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.shuffle()
                    self.sorter = sf.getSorter(self.sortType, self.data)
                    self.time = self.sorter.getTimeMs()
                    self.drawLegend((str(self.sorter), self.time, 0, 0))
                elif event.key == pygame.K_RETURN:
                    self.op = self.sorter.getOperations()
                    stack = self.sorter.getStack()
                    self.animate(stack)
                elif event.key == pygame.K_ESCAPE:
                    self.mainloop()
                elif event.key in range(pygame.K_1, pygame.K_5):
                    self.sortType = SortType(event.key - pygame.K_1 + 1)
                    self.sorter = sf.getSorter(self.sortType, self.data)
                    self.screen.fill(BLACK)
                    self.drawLegend((str(self.sorter), 0, 0, 0))
                    self.visualizeData()
                elif event.key in range(pygame.K_KP1, pygame.K_KP5):
                    self.sortType = SortType(event.key - pygame.K_KP1 + 1)
                    self.sorter = sf.getSorter(self.sortType, self.data)
                    self.screen.fill(BLACK)
                    self.drawLegend((str(self.sorter), 0, 0, 0))
                    self.visualizeData()
                elif event.key == pygame.K_c and pygame.key.get_mods() & pygame.KMOD_CTRL:
                    sys.exit()
                else:
                    print(event.key)


    def shuffle(self):
        self.screen.fill(BLACK)
        random.shuffle(self.data)
        self.displayData = self.data.copy()
        self.visualizeData()


if __name__ == "__main__":
    dut = Visualizer()
    dut.mainloop()
