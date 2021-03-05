import numpy as np
class Node(object):
    """
    :param: number of node.
    """
    def __init__(self,node):
        # Atributes:
        self.node = node
        self.x    = round(np.random.random(),4)*100
        self.y    = round(np.random.random(),4)*100
        self.demand = np.random.randint(10,100)
    # Methods:
    def GetNode(self):
        """
        :return: number of node
        """
        return self.node

    def GetX(self):
        """

        :return: Coordenate X of the node
        """
        return self.x

    def GetY(self):
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