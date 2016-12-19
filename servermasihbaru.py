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
        self._server.gantiTurn(x,y,data,self.gameid,playerke)


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
            self.games.append(self.queue)
            self.queue = None

    def gantiTurn(self, x,y ,data,gameid, playerke):
        game = [a for a in self.games if a.gameid == gameid]
        print len(game)
        if len(game) == 1:
            print 3
            game[0].gantiTurn(x,y,data,gameid,playerke)
        # print "as Player ", self.playerke
        # # playerid = self.playerke , channel
        # # self.send({"action":"player", "playerke": self.playerke})
        # self.playerke+=1


class gamenya:
    def __init__(self,player0, currentIndex):
        self.player0 = player0
        self.player1 = None
        self.gameid = currentIndex
        self.turn = 0

    def gantiTurn(self,x,y,data,gameid, playerke):
        print 98
        if playerke == self.turn:
            print 7878
            self.turn = 0 if self.turn else 1
            self.player1.Send({"action": "place", "horisontal":x,"vertical":y,"gameid":gameid,"torf": True if self.turn == 1 else False})
            self.player0.Send({"action": "place", "horisontal":x,"vertical":y,"gameid":gameid,"torf": True if self.turn == 0 else False})
            # self.player0.Send(data)
            # self.player1.Send(data)
    # def sending(self,x,y,player):



host, port = "localhost", 6969
boxesServe = BoxesServer(localaddr=(host, int(port)))
if (boxesServe):
    print "Server on: ", host, ":", port

while True:
    boxesServe.Pump()
    sleep(0.01)
