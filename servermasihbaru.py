import PodSixNet.Channel
import PodSixNet.Server
from time import sleep

class ClientChannel(PodSixNet.Channel.Channel):

    def Network(self, data):
        print data


class BoxesServer(PodSixNet.Server.Server):
    channelClass = ClientChannel

    def __init__(self, *args, **kwargs):
        PodSixNet.Server.Server.__init__(self, *args, **kwargs)
        self.games = []
        self.queue = None
        self.currentIndex = 0

    def Connected(self, channel, addr):
        print 'new connection:', channel


host, port = "localhost", 6969
boxesServe = BoxesServer(localaddr=(host, int(port)))
if (boxesServe):
    print "Server on: ", host, ":", port

while True:
    boxesServe.Pump()
    sleep(0.01)