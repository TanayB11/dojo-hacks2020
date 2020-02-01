import pygame
# import pandas as pd

# df = pd.read_excel('decks/temp.xlsx').to_dict() # print(df['Pinyin'][0])

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

import pygame

white = (255,255,255)
black = (0,0,0)
orange = (255,165,0)


pygame.init()
display = pygame.display.set_mode((1280,1024))
pygame.display.set_caption('ReflectOS')

exit = False

while not exit:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit = True
        print(event)

    display.fill(white)
    pygame.draw.rect(display, RED, [55,200,100,70],0)
    pygame.display.update()

pygame.quit()
quit()
# convert to postscript file
cv = turtle.getcanvas()
cv.postscript(file= "file_name.ps")
turtle.done()
# postscript to png? list
import os, glob
#convert p
list = glob.glob('*.ps')

for file in list:

    root = file[:-2]
    pdffile = root + 'pdf'
    pngfile = root + 'png'
    os.system('convert ' + file + ' ' + pdffile)
    os.system('convert ' + file + ' ' + pngfile)
