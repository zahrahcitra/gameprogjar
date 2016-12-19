import pygame

class Game():

	def __init__(self):
		pygame.init() #memulai pygame
		self.screen = pygame.display.set_mode((500,500)) #buat layar
		self.running = True
		#self.screen.fill((190,190,190))
		self.flag = [[0 for xrange in range(500)]for yrange in range(500)]
		#flag = [[0 for xrange in range(500)]for yrange in range(500)]
		self.nilaih1=0
		self.nilaiv1=0
		self.wida()
		self.inisialisasi()
		self.clientsatu()
		
	def clientsatu(self):
		while self.running:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					exit()
				elif event.type == pygame.MOUSEBUTTONDOWN and event.pos[0]<100 and event.pos[1]<100:
					#print "1"
					horisontal=30
					vertical=20
					if self.flag[horisontal][vertical]==0:
						self.cewek(horisontal,vertical)
						self.flag[horisontal][vertical]=1
						self.check_clientsatu()
						print self.flag[horisontal][vertical]
						print horisontal
						print vertical
					
				elif event.type == pygame.MOUSEBUTTONDOWN and event.pos[0]>100 and event.pos[0]<200 and event.pos[1]<100:
					horisontal=130
					vertical=20 
					if flag[horisontal][vertical]==0:
						self.cewek(horisontal,vertical)
						flag[horisontal][vertical]=1
						self.check_clientsatu()
						
				elif event.type == pygame.MOUSEBUTTONDOWN and event.pos[0]>200 and event.pos[0]<300 and event.pos[1]<100:
					horisontal=230
					vertical=20 
					if flag[horisontal][vertical]==0:
						self.cewek(horisontal,vertical)
						flag[horisontal][vertical]=1
						self.check_clientsatu()
						
				elif event.type == pygame.MOUSEBUTTONDOWN and event.pos[0]>300 and event.pos[0]<400 and event.pos[1]<100:
					horisontal=330
					vertical=20 
					if flag[horisontal][vertical]==0:
						self.cewek(horisontal,vertical)
						flag[horisontal][vertical]=1
						self.check_clientsatu()
						
				elif event.type == pygame.MOUSEBUTTONDOWN and event.pos[0]>400 and event.pos[0]<500 and event.pos[1]<100:
					horisontal=430
					vertical=20
					if flag[horisontal][vertical]==0:
						self.cewek(horisontal,vertical)
						flag[horisontal][vertical]=1
						self.check_clientsatu()
#-------------------------------------------------------------------------------------------------------------------------------------------
				elif event.type == pygame.MOUSEBUTTONDOWN and event.pos[0]<100 and event.pos[1]>100 and event.pos[1]<200:
					horisontal=30
					vertical=120
					if flag[horisontal][vertical]==0:
						self.cewek(horisontal,vertical)
						flag[horisontal][vertical]=1
				elif event.type == pygame.MOUSEBUTTONDOWN and event.pos[0]>100 and event.pos[0]<200 and event.pos[1]>100 and event.pos[1]<200:
					horisontal=130
					vertical=120
					if flag[horisontal][vertical]==0:
						self.cewek(horisontal,vertical)
						flag[horisontal][vertical]=1
				elif event.type == pygame.MOUSEBUTTONDOWN and event.pos[0]>200 and event.pos[0]<300 and event.pos[1]>100 and event.pos[1]<200:
					horisontal=230
					vertical=120
					if flag[horisontal][vertical]==0:
						self.cewek(horisontal,vertical)
						flag[horisontal][vertical]=1
				elif event.type == pygame.MOUSEBUTTONDOWN and event.pos[0]>300 and event.pos[0]<400 and event.pos[1]>100 and event.pos[1]<200:
					horisontal=330
					vertical=120
					if flag[horisontal][vertical]==0:
						self.cewek(horisontal,vertical)
						flag[horisontal][vertical]=1
				elif event.type == pygame.MOUSEBUTTONDOWN and event.pos[0]>400 and event.pos[0]<500 and event.pos[1]>100 and event.pos[1]<200:
					horisontal=430
					vertical=120
					if flag[horisontal][vertical]==0:
						self.cewek(horisontal,vertical)
						flag[horisontal][vertical]=1
#-----------------------------------------------------------------------------------------------------------------------------------
				elif event.type == pygame.MOUSEBUTTONDOWN and event.pos[0]<100 and event.pos[1]>200 and event.pos[1]<300:
					horisontal=30
					vertical=220
					if flag[horisontal][vertical]==0:
						self.cewek(horisontal,vertical)
						flag[horisontal][vertical]=1
				elif event.type == pygame.MOUSEBUTTONDOWN and event.pos[0]>100 and event.pos[0]<200 and event.pos[1]>200 and event.pos[1]<300:
					horisontal=130
					vertical=220
					if flag[horisontal][vertical]==0:
						self.cewek(horisontal,vertical)
						flag[horisontal][vertical]=1
				elif event.type == pygame.MOUSEBUTTONDOWN and event.pos[0]>200 and event.pos[0]<300 and event.pos[1]>200 and event.pos[1]<300:
					horisontal=230
					vertical=220
					if flag[horisontal][vertical]==0:
						self.cewek(horisontal,vertical)
						flag[horisontal][vertical]=1
				elif event.type == pygame.MOUSEBUTTONDOWN and event.pos[0]>300 and event.pos[0]<400 and event.pos[1]>200 and event.pos[1]<300:
					horisontal=330
					vertical=220
					if flag[horisontal][vertical]==0:
						self.cewek(horisontal,vertical)
						flag[horisontal][vertical]=1
				elif event.type  == pygame.MOUSEBUTTONDOWN and event.pos[0]>400 and event.pos[0]<500 and event.pos[1]>200 and event.pos[1]<300:
					horisontal=430
					vertical=220
					if flag[horisontal][vertical]==0:
						self.cewek(horisontal,vertical)
						flag[horisontal][vertical]=1
#--------------------------------------------------------------------------------------------------------------------------------------
				elif event.type == pygame.MOUSEBUTTONDOWN and event.pos[0]<100 and event.pos[1]>300 and event.pos[1]<400:
					horisontal=30
					vertical=320
					if flag[horisontal][vertical]==0:
						self.cewek(horisontal,vertical)
						flag[horisontal][vertical]=1
				elif event.type == pygame.MOUSEBUTTONDOWN and event.pos[0]>100 and event.pos[0]<200 and event.pos[1]>300 and event.pos[1]<400:
					horisontal=130
					vertical=320
					if flag[horisontal][vertical]==0:
						self.cewek(horisontal,vertical)
						flag[horisontal][vertical]=1
				elif event.type == pygame.MOUSEBUTTONDOWN and event.pos[0]>200 and event.pos[0]<300 and event.pos[1]>300 and event.pos[1]<400:
					horisontal=230
					vertical=320
					if flag[horisontal][vertical]==0:
						self.cewek(horisontal,vertical)
						flag[horisontal][vertical]=1
				elif event.type == pygame.MOUSEBUTTONDOWN and event.pos[0]>300 and event.pos[0]<400 and event.pos[1]>300 and event.pos[1]<400:
					horisontal=330
					vertical=320
					if flag[horisontal][vertical]==0:
						self.cewek(horisontal,vertical)
						flag[horisontal][vertical]=1
				elif event.type  == pygame.MOUSEBUTTONDOWN and event.pos[0]>400 and event.pos[0]<500 and event.pos[1]>300 and event.pos[1]<400:
					horisontal=430
					vertical=320
					if flag[horisontal][vertical]==0:
						self.cewek(horisontal,vertical)
						flag[horisontal][vertical]=1
#---------------------------------------------------------------------------------------------------------------------------------------------
				elif event.type == pygame.MOUSEBUTTONDOWN and event.pos[0]<100 and event.pos[1]>400 and event.pos[1]<500:
					horisontal=30
					vertical=420
					if flag[horisontal][vertical]==0:
						self.cewek(horisontal,vertical)
						flag[horisontal][vertical]=1
				elif event.type == pygame.MOUSEBUTTONDOWN and event.pos[0]>100 and event.pos[0]<200 and event.pos[1]>400 and event.pos[1]<500:
					horisontal=130
					vertical=420
					if flag[horisontal][vertical]==0:
						self.cewek(horisontal,vertical)
						flag[horisontal][vertical]=1
				elif event.type == pygame.MOUSEBUTTONDOWN and event.pos[0]>200 and event.pos[0]<300 and event.pos[1]>400 and event.pos[1]<500:
					horisontal=230
					vertical=420
					if flag[horisontal][vertical]==0:
						self.cewek(horisontal,vertical)
						flag[horisontal][vertical]=1
				elif event.type == pygame.MOUSEBUTTONDOWN and event.pos[0]>300 and event.pos[0]<400 and event.pos[1]>400 and event.pos[1]<500:
					horisontal=330
					vertical=420
					if flag[horisontal][vertical]==0:
						self.cewek(horisontal,vertical)
						flag[horisontal][vertical]=1
				elif event.type  == pygame.MOUSEBUTTONDOWN and event.pos[0]>400 and event.pos[0]<500 and event.pos[1]>400 and event.pos[1]<500:
					horisontal=430
					vertical=420
					if flag[horisontal][vertical]==0:
						self.cewek(horisontal,vertical)
						flag[horisontal][vertical]=1
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
					if flag[horisontal][vertical]==0:
						self.cowok(horisontal,vertical)
						flag[horisontal][vertical]=1
				elif event.type == pygame.MOUSEBUTTONDOWN and event.pos[0]>100 and event.pos[0]<200 and event.pos[1]<100:
					horisontal=125
					vertical=22
					if flag[horisontal][vertical]==0:
						self.cowok(horisontal,vertical)
						flag[horisontal][vertical]=1
				elif event.type == pygame.MOUSEBUTTONDOWN and event.pos[0]>200 and event.pos[0]<300 and event.pos[1]<100:
					horisontal=225
					vertical=22 
					if flag[horisontal][vertical]==0:
						self.cowok(horisontal,vertical)
						flag[horisontal][vertical]=1
				elif event.type == pygame.MOUSEBUTTONDOWN and event.pos[0]>300 and event.pos[0]<400 and event.pos[1]<100:
					horisontal=325
					vertical=22 
					if flag[horisontal][vertical]==0:
						self.cowok(horisontal,vertical)
						flag[horisontal][vertical]=1
				elif event.type == pygame.MOUSEBUTTONDOWN and event.pos[0]>400 and event.pos[0]<500 and event.pos[1]<100:
					horisontal=425
					vertical=22
					if flag[horisontal][vertical]==0:
						self.cowok(horisontal,vertical)
						flag[horisontal][vertical]=1
#-------------------------------------------------------------------------------------------------------------------------------------------
				elif event.type == pygame.MOUSEBUTTONDOWN and event.pos[0]<100 and event.pos[1]>100 and event.pos[1]<200:
					horisontal=25
					vertical=122
					if flag[horisontal][vertical]==0:
						self.cowok(horisontal,vertical)
						flag[horisontal][vertical]=1
				elif event.type == pygame.MOUSEBUTTONDOWN and event.pos[0]>100 and event.pos[0]<200 and event.pos[1]>100 and event.pos[1]<200:
					horisontal=125
					vertical=122
					if flag[horisontal][vertical]==0:
						self.cowok(horisontal,vertical)
						flag[horisontal][vertical]=1
				elif event.type == pygame.MOUSEBUTTONDOWN and event.pos[0]>200 and event.pos[0]<300 and event.pos[1]>100 and event.pos[1]<200:
					horisontal=225
					vertical=122
					if flag[horisontal][vertical]==0:
						self.cowok(horisontal,vertical)
						flag[horisontal][vertical]=1
				elif event.type == pygame.MOUSEBUTTONDOWN and event.pos[0]>300 and event.pos[0]<400 and event.pos[1]>100 and event.pos[1]<200:
					horisontal=325
					vertical=122
					if flag[horisontal][vertical]==0:
						self.cowok(horisontal,vertical)
						flag[horisontal][vertical]=1
				elif event.type == pygame.MOUSEBUTTONDOWN and event.pos[0]>400 and event.pos[0]<500 and event.pos[1]>100 and event.pos[1]<200:
					horisontal=425
					vertical=122
					if flag[horisontal][vertical]==0:
						self.cowok(horisontal,vertical)
						flag[horisontal][vertical]=1
#-----------------------------------------------------------------------------------------------------------------------------------
				elif event.type == pygame.MOUSEBUTTONDOWN and event.pos[0]<100 and event.pos[1]>200 and event.pos[1]<300:
					horisontal=25
					vertical=222
					if flag[horisontal][vertical]==0:
						self.cowok(horisontal,vertical)
						flag[horisontal][vertical]=1
				elif event.type == pygame.MOUSEBUTTONDOWN and event.pos[0]>100 and event.pos[0]<200 and event.pos[1]>200 and event.pos[1]<300:
					horisontal=125
					vertical=222
					self.cowok(horisontal,vertical)
					flag[horisontal][vertical]=1
				elif event.type == pygame.MOUSEBUTTONDOWN and event.pos[0]>200 and event.pos[0]<300 and event.pos[1]>200 and event.pos[1]<300:
					horisontal=225
					vertical=222
					self.cowok(horisontal,vertical)
					flag[horisontal][vertical]=1
				elif event.type == pygame.MOUSEBUTTONDOWN and event.pos[0]>300 and event.pos[0]<400 and event.pos[1]>200 and event.pos[1]<300:
					horisontal=325
					vertical=222
					self.cowok(horisontal,vertical)
					flag[horisontal][vertical]=1
				elif event.type  == pygame.MOUSEBUTTONDOWN and event.pos[0]>400 and event.pos[0]<500 and event.pos[1]>200 and event.pos[1]<300:
					horisontal=425
					vertical=222
					self.cowok(horisontal,vertical)
					flag[horisontal][vertical]=1
#--------------------------------------------------------------------------------------------------------------------------------------
				elif event.type == pygame.MOUSEBUTTONDOWN and event.pos[0]<100 and event.pos[1]>300 and event.pos[1]<400:
					horisontal=25
					vertical=322
					self.cowok(horisontal,vertical)
					flag[horisontal][vertical]=1
				elif event.type == pygame.MOUSEBUTTONDOWN and event.pos[0]>100 and event.pos[0]<200 and event.pos[1]>300 and event.pos[1]<400:
					horisontal=125
					vertical=322
					self.cowok(horisontal,vertical)
					flag[horisontal][vertical]=1
				elif event.type == pygame.MOUSEBUTTONDOWN and event.pos[0]>200 and event.pos[0]<300 and event.pos[1]>300 and event.pos[1]<400:
					horisontal=225
					vertical=322
					self.cowok(horisontal,vertical)
					flag[horisontal][vertical]=1
				elif event.type == pygame.MOUSEBUTTONDOWN and event.pos[0]>300 and event.pos[0]<400 and event.pos[1]>300 and event.pos[1]<400:
					horisontal=325
					vertical=322
					self.cowok(horisontal,vertical)
					flag[horisontal][vertical]=1
				elif event.type  == pygame.MOUSEBUTTONDOWN and event.pos[0]>400 and event.pos[0]<500 and event.pos[1]>300 and event.pos[1]<400:
					horisontal=425
					vertical=322
					self.cowok(horisontal,vertical)
					flag[horisontal][vertical]=1
#---------------------------------------------------------------------------------------------------------------------------------------------
				elif event.type == pygame.MOUSEBUTTONDOWN and event.pos[0]<100 and event.pos[1]>400 and event.pos[1]<500:
					horisontal=25
					vertical=422
					self.cowok(horisontal,vertical)
					flag[horisontal][vertical]=1
				elif event.type == pygame.MOUSEBUTTONDOWN and event.pos[0]>100 and event.pos[0]<200 and event.pos[1]>400 and event.pos[1]<500:
					horisontal=125
					vertical=422
					self.cowok(horisontal,vertical)
					flag[horisontal][vertical]=1
				elif event.type == pygame.MOUSEBUTTONDOWN and event.pos[0]>200 and event.pos[0]<300 and event.pos[1]>400 and event.pos[1]<500:
					horisontal=225
					vertical=422
					self.cowok(horisontal,vertical)
					flag[horisontal][vertical]=1
				elif event.type == pygame.MOUSEBUTTONDOWN and event.pos[0]>300 and event.pos[0]<400 and event.pos[1]>400 and event.pos[1]<500:
					horisontal=325
					vertical=422
					self.cowok(horisontal,vertical)
					flag[horisontal][vertical]=1
				elif event.type  == pygame.MOUSEBUTTONDOWN and event.pos[0]>400 and event.pos[0]<500 and event.pos[1]>400 and event.pos[1]<500:
					horisontal=425
					vertical=422
					self.cowok(horisontal,vertical)
					flag[horisontal][vertical]=1
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
		#self.check_clientdua()
		
	def inisialisasi(self):
		flag = [[0 for xrange in range(500)]for yrange in range(500)]
		xrange=0
		yrange=0
		while xrange<425:
			while yrange<425:
				flag[xrange][yrange]=0
				yrange=yrange+1
			xrange=xrange+1
		
	def check_clientsatu(self):
		h1=30
		v1=20
		n1=0
		m1=0
		print "masuk"
		while(m1<5):
			print "hai"
			print self.flag[30][20]
			if(self.flag[h1][v1]==1):
				print "go"
				h1=h1+100
				self.nilaih1=self.nilaih1+1
				print "oi"
				print self.nilaih1
			if(self.nilaih1==4):
				self.win()
				print "wida"
			m1=m1+1
		while(n1<5):
			if(self.flag[h1][v1]==1):
				v1=v1+100
				nilaiv1=nilaiv1+1
			if(self.nilaiv1==4):
				self.win()
				print "wida"
			n1=n1+1
				
	def check_clientdua(self):
		flag = [[0 for xrange in range(500)]for yrange in range(500)]
		h2=30
		v2=20
		m2=0
		n2=0
		nilaih2=0
		nilaiv2=0
		while(m2<5):
			if(flag[v2][h2+100]==1):
				nilaih2=nilaih2+1
			if(nilaih2==4):
				self.win()
				print "wida"
			m2=m2+1
		while(n2<5):
			if(flag[v2+100][h2]==1):
				nilaiv2=nilaiv2+1
			if(nilaiv2==4):
				self.win()
				print "wida"
			n2=n2+1
	def win(self):
		self.gambarwin = pygame.image.load("win.png").convert_alpha()
		self.screen.blit(self.gambarwin,(250,250))
		pygame.display.flip()
		
 #	def opening(self) :
#		myfont = pygame.font.SysFont("Arial",80)
#		self.screen.fill((0, 0, 0))
#		label = myfont.render("",1,(255, 255, 255))#munculin tulisannya
		#self.screen.blit(label,(0,0))
		#pygame.display.flip()

game = Game()
