import pygame
from colorsDictionary import color
from Node import Node
from Icon import Icon

pygame.init()

WIDTH, HEIGHT = 600, 800
window = pygame.display.set_mode((WIDTH, HEIGHT))

iphonescreenScale = (800, 800)
iphone = pygame.transform.scale(pygame.image.load("iPhone13.png").convert_alpha(), iphonescreenScale)
screen = pygame.transform.scale(pygame.image.load("screengradient.png").convert_alpha(), iphonescreenScale)
rectPhoneScreen = iphone.get_rect()
rectPhoneScreen.centerx = (WIDTH / 2)
rectPhoneScreen.centery = (HEIGHT / 2)

offset = 0
initialPos = 200
nodeArray = []
nodeContent = ["Google Form", "Discord Server", "Spotify Playlist", "Twitch.tv", "Latest YT Video", "Apple.com"]
nodeLinkArray = ["https://forms.gle/ov2hjs7s2PAM5hHf7", "https://discord.gg/Mva3ZaQXy5", "https://open.spotify.com/playlist/0nw1bMLsKgIljeMxSUh6it?si=a3fd146fe1ad44b1",
                 "https://www.twitch.tv/", "https://www.youtube.com/watch?v=dQw4w9WgXcQ", "https://www.apple.com/"]
for i in range(6):
    sampleString = nodeContent[i]
    sampleStringTwo = nodeLinkArray[i]
    nodeArray.append(Node(window, initialPos + offset, sampleString, sampleStringTwo))
    offset += 80

iconScale = (85, 85)
iconScaleTwo = (70, 70)
yPosOffset = 59
yPosOffsetTwo = 730

icons = []
iconImageArray = ["nintendoSwitch.PNG", "img.png", "youtube.png", "spotify.png"]
iconLink = [None, "instagram.com", "https://www.youtube.com/channel/UCScIOxFOQoNtH8LsPwa9QyQ", "https://open.spotify.com/user/ky1cqrwj8yym3ysdcu5hzvtzj?si=7790c06995214428"]
icons.append(Icon(iconImageArray[0], iconScale, None, window, True, 0, 2))
icons.append(Icon(iconImageArray[1], iconScaleTwo, iconLink[1], window, True, 16, 4))
icons.append(Icon(iconImageArray[2], iconScaleTwo, iconLink[2], window, True, 12, 4))
icons.append(Icon(iconImageArray[3], iconScaleTwo, iconLink[3], window, True, 40, 4))

icons[0].rectIcon.centerx = WIDTH / 2
icons[0].rectIcon.centery = ((nodeArray[0].yPos() - yPosOffset) / 2) + yPosOffset
icons[1].rectIcon.centerx = WIDTH / 2
icons[1].rectIcon.centery = yPosOffsetTwo - 50
icons[2].rectIcon.centerx = (WIDTH / 2) + 100
icons[2].rectIcon.centery = yPosOffsetTwo - 50
icons[3].rectIcon.centerx = (WIDTH / 2) - 100
icons[3].rectIcon.centery = yPosOffsetTwo - 50

def main():
    run = True
    x = 0
    y = 0
    while run:
        window.fill(color["gray"])
        window.blit(iphone, rectPhoneScreen)
        window.blit(screen, rectPhoneScreen)
        for m in range(4):
            icons[m].draw()
        for i in range(6):
            nodeArray[i].draw()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                exit()
            elif event.type == pygame.MOUSEMOTION:
                mousex, mousey = event.pos
                x = mousex
                y = mousey
        for i in range(6):
            mouseOver = nodeArray[i].determineMouseOver(x, y)
            if mouseOver:
                nodeArray[i].drawNew()
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    nodeArray[i].openLink()
                    main()
        for j in range(4):
            mouseOverTwo = icons[j].determineMouseOver(x, y)
            if mouseOverTwo:
                icons[j].drawNew()
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    icons[j].openLink()
                    main()

        pygame.display.update()

if __name__ == "__main__":
    main()