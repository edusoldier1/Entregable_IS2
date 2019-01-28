import pygame
import sys

pygame.font.init()

font = pygame.font.SysFont("Verdana", 22)
font_color = (255,255,255)
font_background = (0,0,0)
input_box = pygame.Rect(446,338,226,26)

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
        self.active = False
        self.text = ""
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
                if input_box.collidepoint(event.pos):
                    self.active = True
                elif x>=imgx and x<=(imgx+ancho) and y>=imgy and y<=(imgy+alto):
                    pygame.quit(); sys.exit()
                else:
                    self.active = False
            elif event.type == pygame.KEYDOWN:
                if self.active:
                    if event.key == pygame.K_RETURN:
                        print(self.text)
                        self.text = ""
                    elif event.key == pygame.K_BACKSPACE:
                        self.text = self.text[:-1]
                    else:
                        self.text += event.unicode
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
        
        pygame.draw.rect(self._canvas,font_background,input_box,0)
        txt_surface = font.render(self.text, True, font_color)
        self._canvas.blit(txt_surface, (input_box.x+3, input_box.y+3))
        pygame.display.flip()
    
class Login(Pantalla):
    def __init__(self, canvas):
        Pantalla.__init__(self, canvas)
        coordenadas = {"background":(0,0),
        "salir": (103,593),
        "jugar": (469,373),
        "olvide": (836,509),
        "registrar": (836,472),
        "creditos": (836,596)}
        sprites_img = {}
        
        #este es el personaje
        #p1 = Personaje("images/personajes/hero/hero1.png")
        #este es el fondo
        sprites_img["background"] = Personaje("images/fondos/background.png")

        #botones del login
        sprites_img["salir"] = Personaje("images/botones/salir.png")

        sprites_img["jugar"] = Personaje("images/botones/jugar.png")

        sprites_img["olvide"] = Personaje("images/botones/olvide.png")

        sprites_img["registrar"] = Personaje("images/botones/registrar.png")

        sprites_img["creditos"] = Personaje("images/botones/creditos.png")
        
        for nombre,sprite in sprites_img.items():
            sprite.x,sprite.y = coordenadas[nombre]
            self.agregar_sprite(nombre,sprite)

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
