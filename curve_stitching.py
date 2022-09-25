'''
CURVE STITCHING
Program asks for number of points, then draw them in a circular pattern.

Then, it asks for a function f that will be used to draw lines from each point n to the next one f(n)
'''

import pygame as pg
import numpy as np

n_puntos = int(input("number of points : "))
func = input("f(n) = ")

class Punto(pg.sprite.Sprite):
	
	def __init__(self, n, x, y):
		pg.sprite.Sprite.__init__(self)
		self.image = pg.Surface([5,5], pg.SRCALPHA)
		pg.draw.circle(self.image,(0,0,0),(3,3),2)
		self.rect = self.image.get_rect()
		self.numero=n
		self.rect.topleft=x,y
	
	def update(self):
		pass

def main():
	
	global n_puntos, func
	
	centro_x=400
	centro_y=400
	radio=200
	
	pg.init()
	screen = pg.display.set_mode((800,800),pg.SCALED)
	background = pg.Surface(screen.get_size())
	background = background.convert()
	background.fill((250,250,250))
	screen.blit(background, (0,0))
	pg.display.flip()
	
	puntos=pg.sprite.RenderPlain()
	lista_puntos=[]
	
	for i in range(n_puntos):
		punto1=Punto(i,centro_x+radio*np.cos(2*np.pi*i/n_puntos),centro_y+radio*np.sin(2*np.pi*i/n_puntos))
		lista_puntos+=[punto1]
		punto1.add(puntos)
	
	
	going = True
	while going:
		for event in pg.event.get():
			if event.type == pg.QUIT: going = False
			
		screen.blit(background, (0,0))
		puntos.draw(screen)
		
		for pto in lista_puntos:
			funcion = lambda n: eval(func)
			pg.draw.line(screen,(0,0,0),pto.rect.center,lista_puntos[funcion(pto.numero)%n_puntos].rect.center)
		
		pg.display.flip()
		

if __name__ == '__main__':
    main()