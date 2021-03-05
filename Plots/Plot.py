import matplotlib.pyplot as plt
class Plot(object):
    """
    :param: Object Graph with all information of node and method for calculation
    """
    def __init__(self,graph):
        self.graph = graph

    def PlotSolution(self,route):
        """

        :param route: list - solution route with format [0,1,2,3,...,0]
        :return: Plot object - with node and plot of route.
        """
        plt.figure(figsize=(12,5))
        x = [self.graph.GetX(i) for i in self.graph.GetNodesList()]
        y = [self.graph.GetY(j) for j in self.graph.GetNodesList()]
        plt.scatter(x,y)
        for n in self.graph.GetNodesList():
            plt.annotate(str(n),xy=(self.graph.GetX(n),self.graph.GetY(n)),xytext=(self.graph.GetX(n)-0.5,self.graph.GetY(n)-4),color='#ff0097')

        for n in range(len(route)-1):
            i = route[n]
            j = route[n+1]
            plt.plot([self.graph.GetX(i),self.graph.GetX(j)],[self.graph.GetY(i),self.graph.GetY(j)],color='blue')

        plt.xlabel("Eje X",fontsize =14)
        plt.ylabel("Eje Y",fontsize =14)
        plt.title(" TSP ",fontsize =18)
        return plt.show()