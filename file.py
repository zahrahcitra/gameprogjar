import pygame


class Game():
	def __init__(self):
		pygame.init() #memulai pygame
		self.screen = pygame.display.set_mode((500,500)) #buat layar
		self.running = True
		
		self.movement = [[0 for a in range(5)] for b in range(5)]
		#self.screen.fill((190,190,190))
		self.wida()
		self.clientsatu()
		print self.movement[0][0]
	
	def calcScore(self,x,y,client):
		#print (x," ",y)
		temp=client
		for i in range(5):
			temp=temp&self.movement[i][y]
		
		if (temp==client):
			print ("WIN")
		
		temp=client
		for i in range(5):
			temp=temp&self.movement[x][i]
		
		if (temp==client):
			print ("WIN")
			#self.running=0
		
	def clientsatu(self):
		while self.running:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					exit()
				elif event.type == pygame.MOUSEBUTTONDOWN :
					posX=event.pos[0]
					posY=event.pos[1]
					for  i in range(5):
						for j in range(5):
							if (posX<=(i+1)*100 and posX>=i*100 and posY>=j*100 and posY<=(j+1)*100):
								posXdraw=i*100+30
								posYdraw=j*100+20
								self.cewek(posXdraw,posYdraw)
								self.movement[i][j]=1
								self.calcScore(i,j,1)					
				elif pygame.key.get_pressed()[pygame.K_SPACE]:
					print "spasi nih sob"
					
					
	def clientdua(self):
		while self.running:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					exit()
				elif event.type == pygame.MOUSEBUTTONDOWN :
					posX=event.pos[0]
					posY=event.pos[1]
					for  i in range(5):
						for j in range(5):
							if (posX<=(i+1)*100 and posX>=i*100 and posY>=j*100 and posY<=(j+1)*100):
								posXdraw=i*100+30
								posYdraw=j*100+20
								self.cowok(posXdraw,posYdraw)
								self.movement[i][j]=2
								self.calcScore(i,j,2)
				elif pygame.key.get_pressed()[pygame.K_SPACE]:
					print "spasi nih sob"
				
				
	def wida(self):
		self.gambarpink = pygame.image.load("pink.png").convert_alpha()		
		self.screen.fill((255, 204, 153))
		j = 5
		x = 0
		y = 0
		while j>0:
			i = 5
			x = 0
			while i>0:
				self.screen.blit(self.gambarpink,(x,y)) #load image\
				x=x+100
				i=i-1
			y=y+100
			j=j-1
		pygame.display.flip() #reload screen display
	
	def cewek(self,horisontal,vertical): 
		self.gambargirl = pygame.image.load("girl.png").convert_alpha()
		self.screen.blit(self.gambargirl,(horisontal,vertical))
		pygame.display.flip()

	def cowok(self,horisontal,vertical): 
		self.gambarboy = pygame.image.load("boy.png").convert_alpha()
		self.screen.blit(self.gambarboy,(horisontal,vertical))
		pygame.display.flip()

                
		
 #	def opening(self) :
#		myfont = pygame.font.SysFont("Arial",80)
#		self.screen.fill((0, 0, 0))
#		label = myfont.render("",1,(255, 255, 255))#munculin tulisannya
		#self.screen.blit(label,(0,0))
		#pygame.display.flip()

game = Game()
