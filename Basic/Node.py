import numpy as np
class Node(object):
    """
    :param: number of node.
    """
    def __init__(self,node,clients):
        # Atributes:
        self.node = node
        self.x    = clients[0]
        self.y    = clients[1]
        self.demand = clients[2]
    # Methods:
    def GetNode(self):
        """
        :return: number of node
        """
        return self.node

    def GetLat(self):
        """

        :return: Coordenate X of the node
        """
        return self.x

    def GetLon(self):
        """

        :return: Coordenate Y of the node
        """
        return self.y
    def GetDemand(self):
        """

        :return: Demanan of the node
        """
        return self.demand
    def __str__(self):
        """

        :return: Print node information
        """
        return 'Node {self.node} at position {self.x},{self.y} '.format(self=self)