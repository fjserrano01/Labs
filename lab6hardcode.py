from lab6 import kruskalls_algorythm
from lab6 import GraphALNode
from lab6 import GraphAL
from lab6 import topological_sort
#   Fernando Serrano, Instructor: Diego Aguirre, T.A.: Anindita Nath, 12/11/2018, CS 2302 DataStructures
#   This program is written to include the use of the Topological Sort for Graphs and Kruskal's Algorithm.
#   These are then tested by running a file with a hardcoded Graph as an input and is then displayed in
#   in the output with both the unserted array in the shape of the graph, and the answer list is displayed
#   by showing the source and the output together, seperated by a blank line from the next vertex in the
#   minimum spanning tree.


#   Manuel input of the graph and its vertices
def main():

    graph = GraphAL(7, True)
    graph.add_edge(0, 1, 1)
    graph.add_edge(1, 0, 4)
    graph.add_edge(1, 2, 2)
    graph.add_edge(0, 3, 2)
    graph.add_edge(3, 2, 1)
    graph.add_edge(4, 2, 5)
    graph.add_edge(5, 4, 1)
    graph.add_edge(3, 5, 4)
    graph.add_edge(0, 6, 5)
    print(graph)
    kruskalls_algorythm(graph)
    # topological_sort(graph)

main()