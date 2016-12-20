import pygame
from threading import Thread
from PodSixNet.Connection import ConnectionListener, connection
from time import sleep


class Game(ConnectionListener):
    def __init__(self):
        pygame.init()  # memulai pygame
        self.screen = pygame.display.set_mode((500, 500))  # buat layar
        # inialisasi untuk status permainan (koordinasi dengan server)
        self.flag = [[0 for xrange in range(500)] for yrange in range(500)]
        self.inisialisasi()
        self.statuswin = None
        self.num = None
        self.running = False
        self.statusturn = None
        self.movement = [[0 for a in range(100)] for b in range(100)]
        print self.movement[0][0]
        # self.screen.fill((190,190,190))
        host, port = "10.151.62.84", 6969
        print "Connect to: ", host, ":", port
        self.Connect((host, int(port)))
        self.gameid = None
        # Membuat layar menunggu untuk client yang pertama konek ke server
        if not self.running:
            thread = Thread(target=self.tunggu())
            thread.start()

        # untuk mengecek sudahkah ada musuh yang masuk
        while not self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
            connection.Pump()
            self.Pump()
            sleep(0.01)

    # def Network(self, data):
    #     print data

    def Network_startgame(self, data):
        self.running = True
        self.playerke = data["player"]
        self.gameid = data["gameid"]
        self.statusturn = data["torf"]
        print "Startgame jalan"

    # if self.playerke == 0:
    # 	self.statusturn = True
    # else:
    # 	self.statusturn = False

    def Network_win(self,data):
        self.statuswin = data["torf"]
        self.gameid = data["gameid"]
        self.statusturn = data["statusturn"]
        print "Status menang",self.statuswin
        print "Status Turndari win",self.statusturn

    def Network_place(self, data):
        x = data["horisontal"]
        y = data["vertical"]
        playerke = data["playerke"]
        self.gameid = data["gameid"]
        self.statusturn = data["torf"]
        print "Receive From Server"
        if playerke == 1 and self.flag[x][y] == 0:
            self.cowok(x, y, playerke, self.gameid)
        elif playerke == 0 and self.flag[x][y] == 0:
            self.cewek(x, y, playerke, self.gameid)

    # def Network_whoseturn(self, data):
    # 	self.statusturn = data["torf"]
    # 	print "whoseturn jalan"

    # def Network_jalanlawan(self, data):

    def calcScore(self, x, y, client):
        # print (x," ",y)
        temp = client
        for i in range(5):
            temp = temp & self.movement[i][y]
        if (temp == client):
            thread = Thread(target=self.win())
            thread.start()

        temp = client
        for i in range(5):
            temp = temp & self.movement[x][i]
        if (temp == client):
            thread = Thread(target=self.win())
            thread.start()

    def win(self):
        self.gambarwin = pygame.image.load("charizard.png").convert_alpha()
        self.gambarmenang = pygame.image.load("menang.png").convert_alpha()
        myfont = pygame.font.SysFont(None, 40)
        self.screen.fill((255, 204, 153))
        label = myfont.render("You WIN", 1, (255, 255, 255))
        self.screen.blit(self.gambarwin, (245, 250))
        self.screen.blit(label, (10, 225))
        self.screen.blit(self.gambarmenang ,(100,345))
        pygame.display.flip()
        self.Send({"action": "win","statuswin":True,"playerke":self.playerke,"gameid":self.gameid})

    def lose(self):
        self.gambarlose = pygame.image.load("gengar.png").convert_alpha()
        myfont = pygame.font.SysFont(None, 40)
        self.screen.fill((255, 204, 153))
        label = myfont.render("You Lose", 1, (255, 255, 255))
        self.screen.blit(self.gambarlose, (245, 250))
        self.screen.blit(label, (10, 225))
        pygame.display.flip()

    def pickgambar(self):
        # print 5
        if self.playerke == 0:
            self.clientsatu()
        else:
            self.clientdua()

    def tunggu(self):
        self.screen.fill(0)
        myfont = pygame.font.SysFont(None, 40)

        label = myfont.render("Waiting Other Player...", 1, (255, 255, 255))

        self.screen.blit(label, (10, 225))

        pygame.display.flip()

    def clientsatu(self):
        # print 123
        # if self.playerke == 1:
        # 	self.statusturn = True
        # else:
        # 	self.statusturn = False```
        connection.Pump()
        self.Pump()
        for event in pygame.event.get():
            if self.statusturn == True:
                if event.type == pygame.QUIT:
                    exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    posX = event.pos[0]
                    posY = event.pos[1]
                    for i in range(5):
                        for j in range(5):
                            if (posX <= (i + 1) * 100 and posX >= i * 100 and posY >= j * 100 and posY <= (j + 1) * 100):
                                posXdraw = i * 100 + 30
                                posYdraw = j * 100 + 20
                                if self.flag[posXdraw][posYdraw] == 0:
                                    self.cewek(posXdraw, posYdraw,1,self.gameid)
                                    print "Drawing Cewek"
                                self.movement[i][j] = 1
                                self.calcScore(i, j, 1)
                elif pygame.key.get_pressed()[pygame.K_SPACE]:
                    print "spasi nih sob"


                    # while self.running:
                    # 	print "Dia"
                    # 	for event in pygame.event.get():
                    # 		print "Looping"
                    # 		if self.statusturn == True:
                    # 			if event.type == pygame.QUIT:
                    # 				exit()
                    # 			elif event.type == pygame.MOUSEBUTTONDOWN:
                    # 				posX = event.pos[0]
                    # 				posY = event.pos[1]
                    # 				for i in range(5):
                    # 					for j in range(5):
                    # 						if (posX <= (i + 1) * 100 and posX >= i * 100 and posY >= j * 100 and posY <= (
                    # 							j + 1) * 100):
                    # 							posXdraw = i * 100 + 30
                    # 							posYdraw = j * 100 + 20
                    # 							self.cowok(posXdraw, posYdraw,1)
                    # 							self.movement[i][j] = 2
                    # 							self.calcScore(i, j, 2)
                    # 			elif pygame.key.get_pressed()[pygame.K_SPACE]:
                    # 				print "spasi nih sob"
                    # 			else:
                    # 				break
                    # 		else:
                    # 			break

    def clientdua(self):
        # print 123
        # if self.playerke == 1:
        # 	self.statusturn = True
        # else:
        # 	self.statusturn = False```
        connection.Pump()
        self.Pump()
        for event in pygame.event.get():
            if self.statusturn == True:
                if event.type == pygame.QUIT:
                    exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    posX = event.pos[0]
                    posY = event.pos[1]
                    for i in range(5):
                        for j in range(5):
                            if (posX <= (i + 1) * 100 and posX >= i * 100 and posY >= j * 100 and posY <= (j + 1) * 100):
                                posXdraw = i * 100 + 30
                                posYdraw = j * 100 + 20
                                if self.flag[posXdraw][posYdraw] == 0:
                                    self.cowok(posXdraw, posYdraw, 0, self.gameid)
                                    self.flag[posXdraw][posYdraw] = 1
                                    print "Drawing Cowok"
                                self.movement[i][j] = 2
                                self.calcScore(i, j, 2)
                elif pygame.key.get_pressed()[pygame.K_SPACE]:
                    print "spasi nih sob"

    def wida(self):
        self.gambarpink = pygame.image.load("pink.png").convert_alpha()
        self.screen.fill((255, 204, 153))
        j = 5
        x = 0
        y = 0
        while j > 0:
            i = 5
            x = 0
            while i > 0:
                self.screen.blit(self.gambarpink, (x, y))  # load image\
                x = x + 100
                i = i - 1
            y = y + 100
            j = j - 1
        pygame.display.flip()  # reload screen display

    def cewek(self, horisontal, vertical, playerke, gameid):
        if self.statuswin == None:
            print "Status Giliran",self.statusturn
            self.gambargirl = pygame.image.load("girl.png").convert_alpha()
            self.screen.blit(self.gambargirl, (horisontal, vertical))
            self.flag[horisontal][vertical] = 1
            # self.statusturn = False
            if playerke == 1:
                self.Send({"action": "place", "horisontal": horisontal, "vertical": vertical, "gameid": self.gameid,
                           "playerke": self.playerke})
                print "Sending To server"
                self.statusturn = False
            pygame.display.flip()

    def cowok(self, horisontal, vertical, playerke, gameid):
        if self.statuswin == None:
            print self.statusturn
            self.gambarboy = pygame.image.load("boy.png").convert_alpha()
            self.screen.blit(self.gambarboy, (horisontal, vertical))
            self.flag[horisontal][vertical] = 1
            # self.statusturn = False
            if playerke == 0:
                self.Send({"action": "place", "horisontal": horisontal, "vertical": vertical, "gameid": self.gameid,
                           "playerke": self.playerke})
                print "Sending To server"
                self.statusturn = False
            pygame.display.flip()

    def inisialisasi(self):
        flag = [[0 for xrange in range(500)] for yrange in range(500)]
        xrange = 0
        yrange = 0
        while xrange < 425:
            while yrange < 425:
                flag[xrange][yrange] = 0
                yrange = yrange + 1
            xrange = xrange + 1

            #	def opening(self) :
            #		myfont = pygame.font.SysFont("Arial",80)
            #		self.screen.fill((0, 0, 0))
            #		label = myfont.render("",1,(255, 255, 255))#munculin tulisannya
            # self.screen.blit(label,(0,0))
            # pygame.display.flip()


game = Game()
game.wida()
# game.pickgambar()

while True:
    connection.Pump()
    pygame.display.flip()
    if game.statuswin == None:
        game.pickgambar()
    elif game.statuswin == True:
        game.win()
        pygame.display.flip()
    elif game.statuswin == False:
        game.lose()
        pygame.display.flip()
