import time
import numpy as np
class ImprovementHeuristics(object):
    """
    :param: Object Graph with all information of node and method for calculation
    """
    def __init__(self,graph):
        self.graph = graph

    def TwoOpt(self,sol):
        """

        :param sol: solution dictionary {'route':list,'time':float}
        :return: dictionary with 2-opt solution {'route':list,'time':float}
        """
        initial_solution = sol['route'].copy()
        new_solution = initial_solution.copy()
        start_time = time.time()
        change = 1
        while change !=0:

            initial_dist = self.graph.TotalDist(new_solution)
            min_gain = 0

            # 2-Opt Algorithm:
            for i in range(len(new_solution)-2):
                for j in range(i+2,len(new_solution)-1):
                    actual_cost = self.graph.Dist(new_solution[i],new_solution[i+1]) + self.graph.Dist(new_solution[j],new_solution[j+1])
                    new_cost    = self.graph.Dist(new_solution[i],new_solution[j]) + self.graph.Dist(new_solution[i+1],new_solution[j+1])
                    gain = new_cost - actual_cost

                    if gain <min_gain:
                        min_gain = gain
                        min_i, min_j=i, j

            if min_gain < 0:
                new_solution [min_i+1:min_j+1]=new_solution[min_i+1:min_j+1][::-1].copy()
            final_dist = self.graph.TotalDist(new_solution)
            change = np.abs(initial_dist-final_dist)
        end_time=time.time()
        total_time = sol['time']+end_time-start_time
        sol={'route':new_solution.copy(),'time':total_time}
        return sol
