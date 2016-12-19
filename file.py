import pygame


class Game():
	def __init__(self):
		pygame.init() #memulai pygame
		self.screen = pygame.display.set_mode((500,500)) #buat layar
		self.running = True
		#self.screen.fill((190,190,190))
		self.wida()
		self.clientdua()
	
	def clientsatu(self):
		while self.running:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					exit()
				elif event.type == pygame.MOUSEBUTTONDOWN and event.pos[0]<100 and event.pos[1]<100:
					#print "1"
					horisontal=30
					vertical=20
					self.cewek(horisontal,vertical)
				elif event.type == pygame.MOUSEBUTTONDOWN and event.pos[0]>100 and event.pos[0]<200 and event.pos[1]<100:
					horisontal=130
					vertical=20 
					self.cewek(horisontal,vertical)
				elif event.type == pygame.MOUSEBUTTONDOWN and event.pos[0]>200 and event.pos[0]<300 and event.pos[1]<100:
					horisontal=230
					vertical=20 
					self.cewek(horisontal,vertical)
				elif event.type == pygame.MOUSEBUTTONDOWN and event.pos[0]>300 and event.pos[0]<400 and event.pos[1]<100:
					horisontal=330
					vertical=20 
					self.cewek(horisontal,vertical)
				elif event.type == pygame.MOUSEBUTTONDOWN and event.pos[0]>400 and event.pos[0]<500 and event.pos[1]<100:
					horisontal=430
					vertical=20
					self.cewek(horisontal,vertical)
#-------------------------------------------------------------------------------------------------------------------------------------------
				elif event.type == pygame.MOUSEBUTTONDOWN and event.pos[0]<100 and event.pos[1]>100 and event.pos[1]<200:
					horisontal=30
					vertical=120
					self.cewek(horisontal,vertical)
				elif event.type == pygame.MOUSEBUTTONDOWN and event.pos[0]>100 and event.pos[0]<200 and event.pos[1]>100 and event.pos[1]<200:
					horisontal=130
					vertical=120
					self.cewek(horisontal,vertical)
				elif event.type == pygame.MOUSEBUTTONDOWN and event.pos[0]>200 and event.pos[0]<300 and event.pos[1]>100 and event.pos[1]<200:
					horisontal=230
					vertical=120
					self.cewek(horisontal,vertical)
				elif event.type == pygame.MOUSEBUTTONDOWN and event.pos[0]>300 and event.pos[0]<400 and event.pos[1]>100 and event.pos[1]<200:
					horisontal=330
					vertical=120
					self.cewek(horisontal,vertical)
				elif event.type == pygame.MOUSEBUTTONDOWN and event.pos[0]>400 and event.pos[0]<500 and event.pos[1]>100 and event.pos[1]<200:
					horisontal=430
					vertical=120
					self.cewek(horisontal,vertical)
#-----------------------------------------------------------------------------------------------------------------------------------
				elif event.type == pygame.MOUSEBUTTONDOWN and event.pos[0]<100 and event.pos[1]>200 and event.pos[1]<300:
					horisontal=30
					vertical=220
					self.cewek(horisontal,vertical)
				elif event.type == pygame.MOUSEBUTTONDOWN and event.pos[0]>100 and event.pos[0]<200 and event.pos[1]>200 and event.pos[1]<300:
					horisontal=130
					vertical=220
					self.cewek(horisontal,vertical)
				elif event.type == pygame.MOUSEBUTTONDOWN and event.pos[0]>200 and event.pos[0]<300 and event.pos[1]>200 and event.pos[1]<300:
					horisontal=230
					vertical=220
					self.cewek(horisontal,vertical)
				elif event.type == pygame.MOUSEBUTTONDOWN and event.pos[0]>300 and event.pos[0]<400 and event.pos[1]>200 and event.pos[1]<300:
					horisontal=330
					vertical=220
					self.cewek(horisontal,vertical)
				elif event.type  == pygame.MOUSEBUTTONDOWN and event.pos[0]>400 and event.pos[0]<500 and event.pos[1]>200 and event.pos[1]<300:
					horisontal=430
					vertical=220
					self.cewek(horisontal,vertical)
#--------------------------------------------------------------------------------------------------------------------------------------
				elif event.type == pygame.MOUSEBUTTONDOWN and event.pos[0]<100 and event.pos[1]>300 and event.pos[1]<400:
					horisontal=30
					vertical=320
					self.cewek(horisontal,vertical)
				elif event.type == pygame.MOUSEBUTTONDOWN and event.pos[0]>100 and event.pos[0]<200 and event.pos[1]>300 and event.pos[1]<400:
					horisontal=130
					vertical=320
					self.cewek(horisontal,vertical)
				elif event.type == pygame.MOUSEBUTTONDOWN and event.pos[0]>200 and event.pos[0]<300 and event.pos[1]>300 and event.pos[1]<400:
					horisontal=230
					vertical=320
					self.cewek(horisontal,vertical)
				elif event.type == pygame.MOUSEBUTTONDOWN and event.pos[0]>300 and event.pos[0]<400 and event.pos[1]>300 and event.pos[1]<400:
					horisontal=330
					vertical=320
					self.cewek(horisontal,vertical)
				elif event.type  == pygame.MOUSEBUTTONDOWN and event.pos[0]>400 and event.pos[0]<500 and event.pos[1]>300 and event.pos[1]<400:
					horisontal=430
					vertical=320
					self.cewek(horisontal,vertical)
#---------------------------------------------------------------------------------------------------------------------------------------------
				elif event.type == pygame.MOUSEBUTTONDOWN and event.pos[0]<100 and event.pos[1]>400 and event.pos[1]<500:
					horisontal=30
					vertical=420
					self.cewek(horisontal,vertical)
				elif event.type == pygame.MOUSEBUTTONDOWN and event.pos[0]>100 and event.pos[0]<200 and event.pos[1]>400 and event.pos[1]<500:
					horisontal=130
					vertical=420
					self.cewek(horisontal,vertical)
				elif event.type == pygame.MOUSEBUTTONDOWN and event.pos[0]>200 and event.pos[0]<300 and event.pos[1]>400 and event.pos[1]<500:
					horisontal=230
					vertical=420
					self.cewek(horisontal,vertical)
				elif event.type == pygame.MOUSEBUTTONDOWN and event.pos[0]>300 and event.pos[0]<400 and event.pos[1]>400 and event.pos[1]<500:
					horisontal=330
					vertical=420
					self.cewek(horisontal,vertical)
				elif event.type  == pygame.MOUSEBUTTONDOWN and event.pos[0]>400 and event.pos[0]<500 and event.pos[1]>400 and event.pos[1]<500:
					horisontal=430
					vertical=420
					self.cewek(horisontal,vertical)
#---------------------------------------------------------------------------------------------------------------------------------------------
				elif pygame.key.get_pressed()[pygame.K_SPACE]:
					print "spasi nih sob"
					
	
	def clientdua(self):
		while self.running:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					exit()
				elif event.type == pygame.MOUSEBUTTONDOWN and event.pos[0]<100 and event.pos[1]<100:
					#print "1"
					horisontal=25
					vertical=22
					self.cowok(horisontal,vertical)
				elif event.type == pygame.MOUSEBUTTONDOWN and event.pos[0]>100 and event.pos[0]<200 and event.pos[1]<100:
					horisontal=125
					vertical=22
					self.cowok(horisontal,vertical)
				elif event.type == pygame.MOUSEBUTTONDOWN and event.pos[0]>200 and event.pos[0]<300 and event.pos[1]<100:
					horisontal=225
					vertical=22 
					self.cowok(horisontal,vertical)
				elif event.type == pygame.MOUSEBUTTONDOWN and event.pos[0]>300 and event.pos[0]<400 and event.pos[1]<100:
					horisontal=325
					vertical=22 
					self.cowok(horisontal,vertical)
				elif event.type == pygame.MOUSEBUTTONDOWN and event.pos[0]>400 and event.pos[0]<500 and event.pos[1]<100:
					horisontal=425
					vertical=22
					self.cowok(horisontal,vertical)
#-------------------------------------------------------------------------------------------------------------------------------------------
				elif event.type == pygame.MOUSEBUTTONDOWN and event.pos[0]<100 and event.pos[1]>100 and event.pos[1]<200:
					horisontal=25
					vertical=122
					self.cowok(horisontal,vertical)
				elif event.type == pygame.MOUSEBUTTONDOWN and event.pos[0]>100 and event.pos[0]<200 and event.pos[1]>100 and event.pos[1]<200:
					horisontal=125
					vertical=122
					self.cowok(horisontal,vertical)
				elif event.type == pygame.MOUSEBUTTONDOWN and event.pos[0]>200 and event.pos[0]<300 and event.pos[1]>100 and event.pos[1]<200:
					horisontal=225
					vertical=122
					self.cowok(horisontal,vertical)
				elif event.type == pygame.MOUSEBUTTONDOWN and event.pos[0]>300 and event.pos[0]<400 and event.pos[1]>100 and event.pos[1]<200:
					horisontal=325
					vertical=122
					self.cowok(horisontal,vertical)
				elif event.type == pygame.MOUSEBUTTONDOWN and event.pos[0]>400 and event.pos[0]<500 and event.pos[1]>100 and event.pos[1]<200:
					horisontal=425
					vertical=122
					self.cowok(horisontal,vertical)
#-----------------------------------------------------------------------------------------------------------------------------------
				elif event.type == pygame.MOUSEBUTTONDOWN and event.pos[0]<100 and event.pos[1]>200 and event.pos[1]<300:
					horisontal=25
					vertical=222
					self.cowok(horisontal,vertical)
				elif event.type == pygame.MOUSEBUTTONDOWN and event.pos[0]>100 and event.pos[0]<200 and event.pos[1]>200 and event.pos[1]<300:
					horisontal=125
					vertical=222
					self.cowok(horisontal,vertical)
				elif event.type == pygame.MOUSEBUTTONDOWN and event.pos[0]>200 and event.pos[0]<300 and event.pos[1]>200 and event.pos[1]<300:
					horisontal=225
					vertical=222
					self.cowok(horisontal,vertical)
				elif event.type == pygame.MOUSEBUTTONDOWN and event.pos[0]>300 and event.pos[0]<400 and event.pos[1]>200 and event.pos[1]<300:
					horisontal=325
					vertical=222
					self.cowok(horisontal,vertical)
				elif event.type  == pygame.MOUSEBUTTONDOWN and event.pos[0]>400 and event.pos[0]<500 and event.pos[1]>200 and event.pos[1]<300:
					horisontal=425
					vertical=222
					self.cowok(horisontal,vertical)
#--------------------------------------------------------------------------------------------------------------------------------------
				elif event.type == pygame.MOUSEBUTTONDOWN and event.pos[0]<100 and event.pos[1]>300 and event.pos[1]<400:
					horisontal=25
					vertical=322
					self.cowok(horisontal,vertical)
				elif event.type == pygame.MOUSEBUTTONDOWN and event.pos[0]>100 and event.pos[0]<200 and event.pos[1]>300 and event.pos[1]<400:
					horisontal=125
					vertical=322
					self.cowok(horisontal,vertical)
				elif event.type == pygame.MOUSEBUTTONDOWN and event.pos[0]>200 and event.pos[0]<300 and event.pos[1]>300 and event.pos[1]<400:
					horisontal=225
					vertical=322
					self.cowok(horisontal,vertical)
				elif event.type == pygame.MOUSEBUTTONDOWN and event.pos[0]>300 and event.pos[0]<400 and event.pos[1]>300 and event.pos[1]<400:
					horisontal=325
					vertical=322
					self.cowok(horisontal,vertical)
				elif event.type  == pygame.MOUSEBUTTONDOWN and event.pos[0]>400 and event.pos[0]<500 and event.pos[1]>300 and event.pos[1]<400:
					horisontal=425
					vertical=322
					self.cowok(horisontal,vertical)
#---------------------------------------------------------------------------------------------------------------------------------------------
				elif event.type == pygame.MOUSEBUTTONDOWN and event.pos[0]<100 and event.pos[1]>400 and event.pos[1]<500:
					horisontal=25
					vertical=422
					self.cowok(horisontal,vertical)
				elif event.type == pygame.MOUSEBUTTONDOWN and event.pos[0]>100 and event.pos[0]<200 and event.pos[1]>400 and event.pos[1]<500:
					horisontal=125
					vertical=422
					self.cowok(horisontal,vertical)
				elif event.type == pygame.MOUSEBUTTONDOWN and event.pos[0]>200 and event.pos[0]<300 and event.pos[1]>400 and event.pos[1]<500:
					horisontal=225
					vertical=422
					self.cowok(horisontal,vertical)
				elif event.type == pygame.MOUSEBUTTONDOWN and event.pos[0]>300 and event.pos[0]<400 and event.pos[1]>400 and event.pos[1]<500:
					horisontal=325
					vertical=422
					self.cowok(horisontal,vertical)
				elif event.type  == pygame.MOUSEBUTTONDOWN and event.pos[0]>400 and event.pos[0]<500 and event.pos[1]>400 and event.pos[1]<500:
					horisontal=425
					vertical=422
					self.cowok(horisontal,vertical)
#---------------------------------------------------------------------------------------------------------------------------------------------
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
