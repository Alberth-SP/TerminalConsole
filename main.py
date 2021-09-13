import pygame, sys

from consola import *
from letra import *



VERDE = (0, 255, 0)
BLANCO = (255, 255, 255)


INI_X = 90
INI_Y = 240
SIZE = 50
INC_LET = 14
PAS_X = 60
PAS_Y = 60
AUM_X = 10


pygame.init()
def create_leters(ini_x, ini_y, text):
	i = 0
	hight = 20
	texts = []
	for j in range(len(text)):
		if j %70 == 0 and j > 0:
			texts.append(Letra(ini_x, ini_y, text[i:j+1], VERDE, 30))
			i = j+1
			ini_y += hight
	if text[i:]:
		texts.append(Letra(ini_x, ini_y, text[i:], VERDE, 30))
	return texts


letras_imgs = {

	'Q': [ 
			Consola(INI_X + (PAS_X * 0) + (AUM_X * 0) , INI_Y + (PAS_Y * 0) , SIZE, SIZE, 2, 3), 
			Letra( (INI_X + (PAS_X * 0) + (AUM_X * 0))+ INC_LET , INI_Y + (PAS_Y * 0) + INC_LET , "Q") 
		],
	'W': [ 
			Consola(INI_X + (PAS_X * 1) + (AUM_X * 0) , INI_Y + (PAS_Y * 0) , SIZE, SIZE, 2, 3), 
			Letra( (INI_X + (PAS_X * 1) + (AUM_X * 0))+ INC_LET , INI_Y + (PAS_Y * 0) + INC_LET , "W") 
		],
	'E': [ 
			Consola(INI_X + (PAS_X * 2) + (AUM_X * 0) , INI_Y + (PAS_Y * 0) , SIZE, SIZE, 2, 3), 
			Letra( (INI_X + (PAS_X * 2) + (AUM_X * 0))+ INC_LET , INI_Y + (PAS_Y * 0) + INC_LET , "E") 
		],
	'R': [ 
			Consola(INI_X + (PAS_X * 3) + (AUM_X * 0) , INI_Y + (PAS_Y * 0) , SIZE, SIZE, 2, 3),
			Letra( (INI_X + (PAS_X * 3) + (AUM_X * 0))+ INC_LET , INI_Y + (PAS_Y * 0) + INC_LET , "R") 
		],
	'T': [ 
			Consola(INI_X + (PAS_X * 4) + (AUM_X * 0) , INI_Y + (PAS_Y * 0) , SIZE, SIZE, 2, 3), 
			Letra( (INI_X + (PAS_X * 4) + (AUM_X * 0))+ INC_LET , INI_Y + (PAS_Y * 0) + INC_LET , "T") 
		],
	'Y': [ 
			Consola(INI_X + (PAS_X * 5) + (AUM_X * 0) , INI_Y + (PAS_Y * 0) , SIZE, SIZE, 2, 3), 
			Letra( (INI_X + (PAS_X * 5) + (AUM_X * 0))+ INC_LET , INI_Y + (PAS_Y * 0) + INC_LET , "Y")
		],
	'U': [ 
			Consola(INI_X + (PAS_X * 6) + (AUM_X * 0) , INI_Y + (PAS_Y * 0) , SIZE, SIZE, 2, 3), 
			Letra( (INI_X + (PAS_X * 6) + (AUM_X * 0))+ INC_LET , INI_Y + (PAS_Y * 0) + INC_LET  , "U") 
		],
	'I': [ 
			Consola(INI_X + (PAS_X * 7) + (AUM_X * 0) , INI_Y + (PAS_Y * 0) , SIZE, SIZE, 2, 3), 
			Letra( (INI_X + (PAS_X * 7) + (AUM_X * 0))+ INC_LET , INI_Y + (PAS_Y * 0) + INC_LET  , "I")
		],
	'O': [ 
			Consola(INI_X + (PAS_X * 8) + (AUM_X * 0) , INI_Y + (PAS_Y * 0) , SIZE, SIZE, 2, 3), 
			Letra( (INI_X + (PAS_X * 8) + (AUM_X * 0))+ INC_LET , INI_Y + (PAS_Y * 0) + INC_LET  , "O") 
		],
	'P': [ 
			Consola(INI_X + (PAS_X * 9) + (AUM_X * 0) , INI_Y + (PAS_Y * 0) , SIZE, SIZE, 2, 3), 
			Letra( (INI_X + (PAS_X * 9) + (AUM_X * 0))+ INC_LET , INI_Y + (PAS_Y * 0) + INC_LET  , "P") 
		],

	

	'A': [ Consola(INI_X + (PAS_X * 0) + (AUM_X * 1) , INI_Y + (PAS_Y * 1) , SIZE, SIZE, 2, 3), 
			Letra( (INI_X + (PAS_X * 0) + (AUM_X * 1))+ INC_LET , INI_Y + (PAS_Y * 1) + INC_LET  , "A") 
		 ],
	'S': [ Consola(INI_X + (PAS_X * 1) + (AUM_X * 1) , INI_Y + (PAS_Y * 1) , SIZE, SIZE, 2, 3), 
			Letra( (INI_X + (PAS_X * 1) + (AUM_X * 1))+ INC_LET , INI_Y + (PAS_Y * 1) + INC_LET  , "S") 
		 ],
	'D': [ Consola(INI_X + (PAS_X * 2) + (AUM_X * 1) , INI_Y + (PAS_Y * 1) , SIZE, SIZE, 2, 3), 
			Letra( (INI_X + (PAS_X * 2) + (AUM_X * 1))+ INC_LET , INI_Y + (PAS_Y * 1) + INC_LET  , "D") 
		 ], 
	'F': [ Consola(INI_X + (PAS_X * 3) + (AUM_X * 1) , INI_Y + (PAS_Y * 1) , SIZE, SIZE, 2, 3), 
			Letra( (INI_X + (PAS_X * 3) + (AUM_X * 1))+ INC_LET , INI_Y + (PAS_Y * 1) + INC_LET  , "F") 
		 ],
	'G': [ Consola(INI_X + (PAS_X * 4) + (AUM_X * 1) , INI_Y + (PAS_Y * 1) , SIZE, SIZE, 2, 3), 
			Letra( (INI_X + (PAS_X * 4) + (AUM_X * 1))+ INC_LET , INI_Y + (PAS_Y * 1) + INC_LET  , "G") 
		 ],
	'H': [ Consola(INI_X + (PAS_X * 5) + (AUM_X * 1) , INI_Y + (PAS_Y * 1) , SIZE, SIZE, 2, 3), 
			Letra( (INI_X + (PAS_X * 5) + (AUM_X * 1))+ INC_LET , INI_Y + (PAS_Y * 1) + INC_LET  , "H") 
		 ],
	'J': [ Consola(INI_X + (PAS_X * 6) + (AUM_X * 1) , INI_Y + (PAS_Y * 1) , SIZE, SIZE, 2, 3), 
			Letra( (INI_X + (PAS_X * 6) + (AUM_X * 1))+ INC_LET , INI_Y + (PAS_Y * 1) + INC_LET  , "J") 
		 ],
	'K': [ Consola(INI_X + (PAS_X * 7) + (AUM_X * 1) , INI_Y + (PAS_Y * 1) , SIZE, SIZE, 2, 3), 
			Letra( (INI_X + (PAS_X * 7) + (AUM_X * 1))+ INC_LET , INI_Y + (PAS_Y * 1) + INC_LET  , "K") 
		 ],
	'L': [ Consola(INI_X + (PAS_X * 8) + (AUM_X * 1) , INI_Y + (PAS_Y * 1) , SIZE, SIZE, 2, 3), 
			Letra( (INI_X + (PAS_X * 8) + (AUM_X * 1))+ INC_LET , INI_Y + (PAS_Y * 1) + INC_LET  , "L") 
		 ],


	'Z': [ Consola(INI_X + (PAS_X * 0) + (AUM_X * 4) , INI_Y + (PAS_Y * 2) , SIZE, SIZE, 2, 3), 
			Letra( (INI_X + (PAS_X * 0) + (AUM_X * 4))+ INC_LET , INI_Y + (PAS_Y * 2) + INC_LET  , "Z") 
		 ],
	'X': [ Consola(INI_X + (PAS_X * 1) + (AUM_X * 4) , INI_Y + (PAS_Y * 2) , SIZE, SIZE, 2, 3), 
			Letra( (INI_X + (PAS_X * 1) + (AUM_X * 4))+ INC_LET , INI_Y + (PAS_Y * 2) + INC_LET  , "X") 
		 ],
	'C': [ Consola(INI_X + (PAS_X * 2) + (AUM_X * 4) , INI_Y + (PAS_Y * 2) , SIZE, SIZE, 2, 3), 
			Letra( (INI_X + (PAS_X * 2) + (AUM_X * 4))+ INC_LET , INI_Y + (PAS_Y * 2) + INC_LET  , "C") 
		 ], 
	'V': [ Consola(INI_X + (PAS_X * 3) + (AUM_X * 4) , INI_Y + (PAS_Y * 2) , SIZE, SIZE, 2, 3), 
			Letra( (INI_X + (PAS_X * 3) + (AUM_X * 4))+ INC_LET , INI_Y + (PAS_Y * 2) + INC_LET  , "V") 
		 ],
	'B': [ Consola(INI_X + (PAS_X * 4) + (AUM_X * 4) , INI_Y + (PAS_Y * 2) , SIZE, SIZE, 2, 3), 
			Letra( (INI_X + (PAS_X * 4) + (AUM_X * 4))+ INC_LET , INI_Y + (PAS_Y * 2) + INC_LET  , "B") 
		 ],
	'N': [ Consola(INI_X + (PAS_X * 5) + (AUM_X * 4) , INI_Y + (PAS_Y * 2) , SIZE, SIZE, 2, 3), 
			Letra( (INI_X + (PAS_X * 5) + (AUM_X * 4))+ INC_LET , INI_Y + (PAS_Y * 2) + INC_LET  , "N") 
		 ],
	'M': [ Consola(INI_X + (PAS_X * 6) + (AUM_X * 4) , INI_Y + (PAS_Y * 2) , SIZE, SIZE, 2, 3), 
			Letra( (INI_X + (PAS_X * 6) + (AUM_X * 4))+ INC_LET , INI_Y + (PAS_Y * 2) + INC_LET  , "M") 
		 ],


}






def run():
	#pygame.init()
	screen = pygame.display.set_mode((800, 600))
	screen.fill((180, 180, 180))


	console = Consola(20, 20, 760, 200)

	console2 = Consola(20, 230, 35, 35, 2, 3)
	console2.setColor((255,255,255))


	clock = pygame.time.Clock()
	
	end = False
	count = 1
	letras = []


	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				end = True
				break
			if event.type == pygame.KEYDOWN:
				if event.key >= 97 and event.key <= 122:
					letra = chr(event.key).upper()
					letras.append( chr(event.key))
					letras_imgs[letra][1].setColor(VERDE)
					letras_imgs[letra][1].updateText()
					letras_imgs[letra][0].setColor(VERDE)
				elif event.key == 8:
					if letras:
						letras.pop()
				elif event.key == pygame.K_SPACE:
					letras.append(" ")

			elif event.type == pygame.KEYUP:
				if event.key >= 97 and event.key <= 122:
					letra = chr(event.key).upper()
					letras_imgs[letra][1].setColor(BLANCO)
					letras_imgs[letra][1].updateText()
					letras_imgs[letra][0].setColor(BLANCO)
		if end:
			break

		screen.fill((0, 0, 0))	

		texts = create_leters(25, 25, "".join(letras) )
		rect = texts[-1].getPosFinal() if texts else (25,25)

		for text in texts:
			screen.blit(text.getText(), text.getPos())
		

		if count < 20:
			barra = Letra(rect[0], rect[1], "|", VERDE, 30)
			screen.blit(barra.getText(), barra.getPos())
		elif count > 20 and count < 40:
			pass
		elif count > 40:
			count = 1

		count += 1
		console.draw(screen)
		
		for k in letras_imgs:
			letras_imgs[k][0].draw(screen)
			screen.blit(letras_imgs[k][1].getText(), letras_imgs[k][1].getPos())
		


		pygame.display.flip()
		clock.tick(60)

run()



