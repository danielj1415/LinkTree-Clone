import pygame
from colorsDictionary import color
import webbrowser

pygame.init()

class Icon:
    def __init__(self, image, scale, link, window, value, radius, thickness):
        self.image = image
        self.scale = scale
        self.link = link
        self.window = window
        self.icon = pygame.transform.scale(pygame.image.load(self.image), self.scale)
        self.rectIcon = self.icon.get_rect()
        self.thickness = thickness
        self.value = value
        self.radius = radius
        print(self.link)

    def draw(self):
        self.window.blit(self.icon, self.rectIcon)
        if self.value == True:
            pygame.draw.rect(self.window, color["white"], self.rectIcon, self.thickness, self.radius)

    def rect(self):
        return self.rectIcon

    def drawNew(self):
        pygame.draw.rect(self.window, color["navyBlue"], self.rectIcon, self.thickness, self.radius)

    def determineMouseOver(self, x, y):
        if self.rectIcon.collidepoint(x, y):
            return True
        else:
            return False

    def openLink(self):
        if self.link == None:
            return 1
        else:
            webbrowser.open(self.link)

