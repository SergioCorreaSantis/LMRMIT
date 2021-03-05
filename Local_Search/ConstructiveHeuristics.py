import time
class ConstructiveHeuristics(object):
    """
    :param: Object Graph with all information of node and method for calculation
    """
    def __init__(self,graph):
        self.graph = graph

    def NearestNeighbor(self,start_node):

        """
        :param start_node: integer, node in node list.
        :return: dictionary {'route':list,'time':float]
        """
        start_time = time.time()
        list_node = self.graph.GetNodesList()
        NN=[int(start_node)]
        while len(NN)<len(list_node):
            k=NN[-1]
            nn={(k,j):self.graph.Dist(k,j) for j in list_node if j!=k and j not in NN }
            new = min(nn.items(),key=lambda x:x[1])
            NN.append(int(new[0][1]))
        NN.append(start_node)
        end_time = time.time()
        sol = {'route':NN,'time':end_time-start_time}
        return sol
