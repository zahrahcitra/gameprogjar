import PodSixNet.Channel
import PodSixNet.Server
from time import sleep


class ClientChannel(PodSixNet.Channel.Channel):
    def Network(self, data):
        print data

    def Network_place(self, data):
        self.x = data["horisontal"]
        self.y = data["vertical"]
        num = data["num"]
        self.gameid = data["gameid"]
        print data
        gamenya(x,y)



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
                {"action": "startgame", "player": 0, "gameid": self.queue.gameid})
            self.queue.player1.Send(
                {"action": "startgame", "player": 1, "gameid": self.queue.gameid})
            self.games.append(self.queue)
            self.queue = None
        # print "as Player ", self.playerke
        # # playerid = self.playerke , channel
        # # self.send({"action":"player", "playerke": self.playerke})
        # self.playerke+=1

class gamenya:
    def __init__(self,player0, currentIndex):
        self.player0 = player0
        self.player1 = None
        self.gameid = currentIndex



    # def sending(self,x,y,player):



host, port = "localhost", 6969
boxesServe = BoxesServer(localaddr=(host, int(port)))
if (boxesServe):
    print "Server on: ", host, ":", port

while True:
    boxesServe.Pump()
    sleep(0.01)
