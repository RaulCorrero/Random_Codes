'''
Draws n dots moving in straight lines so that
the dots look like they are moving in a circular motion.
'''

import pygame as pg
import numpy as np

def main():
	pg.init()
	screen = pg.display.set_mode((800,800))
	
	background = pg.Surface(screen.get_size()).convert()
	background.fill((0,0,0))
	
	pg.draw.circle(background,(200,200,200),(400,400),400)
	
	screen.blit(background,(0,0))
	pg.display.flip()
	
	clock = pg.time.Clock()
	circulos = True
	k=-1
	n = input("Number of circles:")
	try:
		n=int(n)
	except:
		print("Error in number of circles, running with n=10")
		n=10
	xs = np.linspace(0.,2*np.pi,n+1)[:-1]
	lineas = True
	while circulos:
		k+=1
		clock.tick(40)
		
		for event in pg.event.get():
			if event.type == pg.QUIT: circulos = False
			if event.type == pg.KEYDOWN:
				if event.key == pg.K_SPACE:
					n+=1
					xs = np.linspace(0.,2*np.pi,n+1)[:-1]
				if event.key == pg.K_a:
					lineas = not lineas
				
		
		screen.blit(background,(0,0))
		
		x0 = (400-175*np.cos(np.pi/2.0 + 0.1*k/np.pi),400-175*np.sin(np.pi/2.0 + 0.1*k/np.pi))
		
		for i in xs:
			if lineas:
				color = (127+127*np.cos(i),0,127+127*np.sin(i))
				x1 = (400-175*np.cos(np.pi/2.0+3)+175*np.cos(-i+3),400-175*np.sin(np.pi/2.0+3)-175*np.sin(-i+3))
				x2 = (400-175*np.cos(np.pi+np.pi/2.0+3)+175*np.cos(np.pi-i+3),400-175*np.sin(np.pi+np.pi/2.0+3)-175*np.sin(np.pi-i+3))
				y0 = x2[0]-x1[0]
				y1 = x2[1]-x1[1]
				pg.draw.line(screen,color,(x1[0]-200*y0,x1[1]-200*y1),(x2[0]+200*y0,x2[1]+200*y1))
		
		for i in xs:
			color = (127+127*np.cos(i),0,127+127*np.sin(i))
			pg.draw.circle(screen,color,(x0[0]+175*np.cos(0.1*k/np.pi-i),x0[1]-175*np.sin(0.1*k/np.pi-i)),15)
		
		
		pg.display.flip()
	pg.quit()

if __name__=="__main__": main()