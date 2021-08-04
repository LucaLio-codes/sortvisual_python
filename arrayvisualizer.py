
import pygame


class ArrayVisualize:

    def __init__(self, data, screen, width):
        self.data = data
        self.n = len(data)
        self.screen = screen
        self.color = 245, 161, 66
        self.width = width
        self.black = 0, 0, 0



    def print_data(self):
        print(self.data)

    def visualize_data(self):
        self.screen.fill(self.black)
        for d in range(self.n):
            pos = (d*self.width, self.n - self.data[d])
            form = (self.width,  self.n)
            r = pygame.Rect(pos,form)
            pygame.draw.rect(self.screen, self.color, r)



if __name__ == "__main__":
    print("happens")
