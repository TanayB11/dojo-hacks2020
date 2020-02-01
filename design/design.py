import pygame
background_colour = (18, 18, 18)

(width, height) = (500, 500)
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Design')
screen.fill(background_colour)
pygame.display.flip()
running = True
while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False

class Drawing(RelativeLayout):

    # On mouse press how Paint_brush behave
    def on_touch_down(self, touch):
        pb = Paint_brush()
        pb.center = touch.pos
        self.add_widget(pb)

    # On mouse movement how Paint_brush behave
    def on_touch_move(self, touch):
        pb = Paint_brush()
        pb.center = touch.pos
        self.add_widget(pb)
