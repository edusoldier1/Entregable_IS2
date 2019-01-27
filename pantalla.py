import pygame
import sys

class Personaje(pygame.sprite.Sprite):
    def __init__(self, imagen):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(imagen)
        self.x = 0
        self.y = 0
        self.ancho = 10
        self.alto = 10
        

class Pantalla:
    def __init__(self, canvas):
        self.sprites = {}
        self._canvas = canvas
        """self.eventos =	{
        "Arriba": False,
        "Abajo": False,
        "Derecha": False,
        "Izquierda": False,
        "Salir":False
        }"""

    def agregar_sprite(self, nombre, sprite):
        self.sprites[nombre] = sprite
   
    def handle_events(self,x,y,imgx,imgy,alto,ancho):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                #self.eventos["Salir"]=True
                pygame.quit(); sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if x>=imgx and x<=(imgx+ancho) and y>=imgy and y<=(imgy+alto):
                    pygame.quit(); sys.exit()
               # print(self.eventos["Salir"])
            """if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.eventos["Izquierda"]=True
                    print(self.eventos["Izquierda"])
                if event.key == pygame.K_RIGHT:
                    self.eventos["Derecha"]=True
                    print(self.eventos["Derecha"])
                if event.key == pygame.K_UP:
                    self.eventos["Arriba"]=True
                    print(self.eventos["Arriba"])
                if event.key == pygame.K_DOWN:
                    self.eventos["Abajo"]=True
                    print(self.eventos["Abajo"])"""

    """def update(self):
        for nombre in self.eventos:
            self.eventos[nombre]=False"""
            #print(self.eventos[nombre])

    def render(self):
        #print("render")
        #self._canvas.fill([0,0,0])
        for nombre, sprite in self.sprites.items():
            surf = pygame.Surface((sprite.ancho, sprite.alto))
            self._canvas.blit(sprite.image, surf.get_rect(topleft=(sprite.x, sprite.y)))
        pygame.display.flip()
    
class EjemploPantalla(Pantalla):
    def __init__(self, canvas):
        Pantalla.__init__(self, canvas)
        #este es el personaje
        #p1 = Personaje("images/personajes/hero/hero1.png")
        #este es el fondo
        fondo = Personaje("images/fondos/login1.png")
        #botones del login
        salir = Personaje("images/botones/salir.png")
        salir.x = 103
        salir.y = 593
        jugar = Personaje("images/botones/jugar.png")
        jugar.x = 469
        jugar.y = 373
        olvide = Personaje("images/botones/olvide.png")
        olvide.x = 836
        olvide.y = 509
        registrar = Personaje("images/botones/registrar.png")
        registrar.x = 836
        registrar.y = 472
        creditos = Personaje("images/botones/creditos.png")
        creditos.x = 836
        creditos.y = 596
        self.agregar_sprite("Background",fondo)
        self.agregar_sprite("Salir",salir)
        self.agregar_sprite("Jugar",jugar)
        self.agregar_sprite("Registrar",registrar)
        self.agregar_sprite("Olvide",olvide)
        self.agregar_sprite("Creditos",creditos)
        #self.agregar_sprite("hero1",p1)
        #self.update()


# Para crear una pantalla extra (o la de login) se crea una clase COMO EjemploPantalla y se instancia 
# desde game.py en la clase ScreenManager
# EJEMPLO:

""" class Login(Pantalla):
    def __init__(self, canvas):
        Pantalla.__init__(self, canvas)
        p1 = Personaje("images/personajes/hero/hero1.png")
        self.agregar_sprite("hero1",p1)
        self.handle_events()
        self.update() """
