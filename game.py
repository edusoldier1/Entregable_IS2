import pygame
from pantalla import *

class ScreenManager:
    def __init__(self):
        pygame.init()
        img_background = "login1"
        canvas = pygame.display.set_mode((1120, 700))
		
		#Reemplazar esta línea con self._pantalla_actual = Login(canvas)#
        self._pantalla_actual = EjemploPantalla(canvas)
		
        self.clock = pygame.time.Clock()
        backdrop = pygame.image.load("images/fondos/" + img_background + ".png").convert()
        backdropbox = canvas.get_rect()

    def run(self):
        while True:
            x,y = pygame.mouse.get_pos()
            #self._pantalla_actual.update()
            self._pantalla_actual.render()
            width,height = self._pantalla_actual.sprites["Salir"].image.get_size()
            locx = self._pantalla_actual.sprites["Salir"].x
            locy = self._pantalla_actual.sprites["Salir"].y
            self._pantalla_actual.handle_events(x,y,locx,locy,height,width)
            self.clock.tick(60)

def main():

    manager = ScreenManager()
    manager.run()

if __name__ == "__main__":

    main()
