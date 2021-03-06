import numpy as np
from Basic.Node import Node
class Graph(object):

    def __init__(self,customers):
        """

        :param customers: Nº of customers to create
        """
        #Create node dictionary:
        self.node_dict=dict()
        for n in range(len(customers)):
            node= Node(n,customers.iloc[n])
            aux={'node':node,'x':node.GetX(),'y':node.GetY(),'demand':node.GetDemand()}
            self.node_dict[n]=aux

        self.node_list = list(self.node_dict.keys()) #list with node [0,1,2,3] | intergers
        self.arch  = [(i,j) for i in self.node_list for j in self.node_list if i!=j] # list of Archs.

        #Matrix of distance:
        self.distance = {(i,j): np.hypot(self.node_dict[i]['x']-self.node_dict[j]['x'],
                                         self.node_dict[i]['y']-self.node_dict[j]['y']) for i,j in self.arch}

    # ******** Get Nodes Basic Information ********
    def GetX(self,i):
        """

        :param i: int - node
        :return: float - coordenate X of node i
        """
        return self.node_dict[i]['x']

    def GetY(self,i):
        """

        :param i: int - node
        :return: float - coordenate Y of node i
        """
        return self.node_dict[i]['y']

    def GetDemand(self,i):
        """

        :param i: int - node
        :return: int - Demand of node i
        """
        return self.node_dict[i]['demand']

    def GetNodesList(self):
        """

        :return: list of node as int [0,1,2,3,...]
        """
        return self.node_list

    # ******** Grpah Functions ********
    def Dist(self,i,j):
        """

        :param i: int - Node i
        :param j: int - Node j
        :return: float - Distance from node i and j
        """
        return self.distance[i,j]

    def TotalDist(self,node_list):
        """

        :param node_list: list - route created
        :return:Total Distance of a given route
        """
        total_distance=0
        for n in range(len(node_list)-1):
            i=node_list[n]
            j=node_list[n+1]
            total_distance+=self.distance[(i,j)]
        return total_distance