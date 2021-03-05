from Basic.Graph import Graph
from Local_Search.ConstructiveHeuristics import ConstructiveHeuristics
from Local_Search.ImprovementHeuristics import ImprovementHeuristics
from Plots.Plot import Plot

#Numbers of customers
customers = 20

#Creating objects: Graph, ConstructiveHeuristics, ImprovementHeuristics:
graph = Graph(customers)
con    = ConstructiveHeuristics(graph)
opt   = ImprovementHeuristics(graph)

#Select starting node
start_node = 2
initial_solution = con.NearestNeighbor(start_node)
print('Initial Route '+str(initial_solution['route']) + ' Time '+str(initial_solution['time']))
print('Distance of initial route ' + str(graph.TotalDist(initial_solution['route'])))

best_solution = opt.TwoOpt(initial_solution)
print('Final Route '+str(best_solution['route']) + ' Time '+str(best_solution['time']))
print('Distance of final route ' + str(graph.TotalDist(best_solution['route'])))

# Plotting solution:
plot = Plot(graph)
plot.PlotSolution(best_solution['route'])

#test
