import PodSixNet.Channel
import PodSixNet.Server
from time import sleep


class ClientChannel(PodSixNet.Channel.Channel):

    def Network(self, data):
        print data

    def Network_place(self, data):
        x = data["horisontal"]
        y = data["vertical"]
        self.gameid = data["gameid"]
        playerke = data["playerke"]
        print "Recv From Player ke",playerke
        self._server.placeing(x, y, data, self.gameid, playerke)
        # self._server.gantiTurn(self.gameid,playerke)
        # self._server.gantiTurn(x,y,data,self.gameid,playerke)

    def Network_win(self,data):
        playerke = data["playerke"]
        self.statuswin = data["statuswin"]
        self.gameid = data["gameid"]
        self._server.win(self.statuswin,playerke,self.gameid)


class BoxesServer(PodSixNet.Server.Server):
    channelClass = ClientChannel

    def __init__(self, *args, **kwargs):
        PodSixNet.Server.Server.__init__(self, *args, **kwargs)
        self.games = []
        self.queue = None
        self.currentIndex = 0

    def Connected(self, channel, addr):
        print 'new connection:', channel
        if self.queue == None:
            print "As Player ke", self.currentIndex
            self.currentIndex += 1
            channel.gameid = self.currentIndex
            self.queue = gamenya(channel, self.currentIndex)
        else:
            channel.gameid = self.currentIndex
            self.queue.player1 = channel
            self.queue.player0.Send(
                {"action": "startgame", "player": 0, "gameid": self.queue.gameid,"torf": True})
            self.queue.player1.Send(
                {"action": "startgame", "player": 1, "gameid": self.queue.gameid,"torf": False})
            print "As Player ke", self.currentIndex
            self.games.append(self.queue)
            self.queue = None

    def placeing(self, x, y, data, gameid, playerke):
        game = [a for a in self.games if a.gameid == gameid]
        print len(game)
        if len(game) == 1:
            game[0].placeing(x, y, data, gameid,playerke)



    # def gantiTurn(self,gameid, playerke):
    #     game = [a for a in self.games if a.gameid == gameid]
    #     print len(game)
    #     if len(game) == 1:
    #         print 3
    #         game[0].gantiTurn(playerke)
        # print "as Player ", self.playerke
        # # playerid = self.playerke , channel
        # # self.send({"action":"player", "playerke": self.playerke})
        # self.playerke+=1

    def win(self,statuswin,playerke,gameid):
        game = [a for a in self.games if a.gameid == gameid]
        print "cekcek"
        if len(game) == 1:
            game[0].statuswin(statuswin,playerke)

class gamenya:
    def __init__(self,player0, currentIndex):
        self.player0 = player0
        self.player1 = None
        self.gameid = currentIndex
        self.turn = 0

    # def gantiTurn(self, playerke):
    #     print 98
    #     if playerke == self.turn:
    #         print 7878
    #         self.turn = 0 if self.turn else 1
    #         self.player1.Send({"action": "place","torf": True if self.turn == 1 else False})
    #         self.player0.Send({"action": "place","torf": True if self.turn == 0 else False})
    #         print playerke
            # self.player0.Send(data)
            # self.player1.Send(data)

    def placeing(self, x, y, data, gameid,playerke):
        print "playerke",playerke
        print "giliransapa",self.turn
        # make sure it's their turn
        if playerke == self.turn:
            self.turn = 1 if self.turn else 0
            self.player0.Send({"action": "place","horisontal": x, "vertical": y, "gameid":self.gameid,"playerke":playerke,"torf": True if self.turn == 1 else False})
            print "Send to",self.player0
            self.player1.Send({"action": "place","horisontal": x, "vertical": y, "gameid":self.gameid,"playerke":playerke,"torf": True if self.turn == 0 else False})
            print "send to",self.player1
        else:
            self.turn = 1 if self.turn else 0
            self.player0.Send({"action": "place","horisontal": x, "vertical": y, "gameid":self.gameid,"playerke":playerke,"torf": True if self.turn == 0 else False})
            print "Send to",self.player0
            self.player1.Send({"action": "place","horisontal": x, "vertical": y, "gameid":self.gameid,"playerke":playerke,"torf": True if self.turn == 1 else False})
            print "send to",self.player1
            # self.player0.Send(data)
            # self.player1.Send(data)
    # def sending(self,x,y,player):
    
    def statuswin(self,statuswin,playerke):
        if playerke == self.turn:
            self.turn = 1 if self.turn else 0
            self.player0.Send({"action": "win","gameid": self.gameid, "playerke": playerke,"torf": True if self.turn == 0 else False,"statusturn": False})
            print "Send to", self.player0
            self.player1.Send({"action": "win","gameid": self.gameid, "playerke": playerke, "torf": True if self.turn == 1 else False,"statusturn": False})
            print "send to", self.player1
        else:
            self.turn = 1 if self.turn else 0
            self.player0.Send({"action": "win","gameid": self.gameid, "playerke": playerke,"torf": True if self.turn == 1 else False,"statusturn": False})
            print "Send to", self.player0
            self.player1.Send({"action": "win","gameid": self.gameid, "playerke": playerke, "torf": True if self.turn == 0 else False,"statusturn": False})
            print "send to", self.player1


host, port = "10.151.62.84", 6969
boxesServe = BoxesServer(localaddr=(host, int(port)))
if (boxesServe):
    print "Server on: ", host, ":", port

while True:
    boxesServe.Pump()
    sleep(0.01)
