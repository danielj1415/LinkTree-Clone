import pygame
from colorsDictionary import color
import webbrowser

pygame.init()

class Node:
    def __init__(self, window, yPosOffset, text, link):
        self.window = window
        self.yPosoffset = yPosOffset
        self.node = pygame.Rect(0, 0, 300, 60)
        self.node.centerx = self.window.get_width() / 2
        self.node.centery = self.yPosoffset
        self.thickness = 2
        self.text = text
        self.link = link

        self.font = pygame.font.SysFont("Karla-Regular.ttf", 30)
        self.textImg = self.font.render(text, True, color["white"])
        self.textRect = self.textImg.get_rect()
        self.textRect.centerx = self.window.get_width() / 2
        self.textRect.centery = self.node.centery
        self.numGroup = (self.textRect.x, self.textRect.y)

    def draw(self):
        self.window.blit(self.textImg, self.numGroup)  # for self.numGroup, it sets it at a position
        pygame.draw.rect(self.window, color["white"], self.node, self.thickness)

    def returnRect(self):
        return self.node

    def determineMouseOver(self, x, y):
        if self.node.collidepoint(x, y):
            return True
        else:
            return False

    def drawNew(self):
        pygame.draw.rect(self.window, color["navyBlue"], self.node)
        pygame.draw.rect(self.window, color["navyBlue"], self.node, 2)
        self.window.blit(self.textImg, self.numGroup)  # for self.numGroup, it sets it at a position

    def openLink(self):
        webbrowser.open(self.link)

    def yPos(self):
        return self.node.y

