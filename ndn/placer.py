from mininet.examples.cluster import Placer

nodePlace = []

class PopulatePlacement():
    def __init__( self, placeList ):
        global nodePlace
        nodePlace = placeList


class GuidedPlacer( Placer ):
    "Guided placement"
    def __init__( self, *args, **kwargs ):
        Placer.__init__( self, *args, **kwargs )
        self.count = 0

    def place( self, nodename ):
        assert nodename  #please pylint
        while(1):
            global nodePlace
            if(nodePlace[self.count] != 0):
                global nodePlace
                nodePlace[self.count] -= 1
                # args[self.count] is not zero, hence return the server at that position
                # so that if args[0] is 7 and servers[0] is Europa then place 7 nodes on Europa
                return self.servers[self.count]
            else:
                # while makes sure we go back to the if after this
                self.count += 1
