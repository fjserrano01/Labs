#   Fernando Serrano, Instructor: Diego Aguirre, T.A.: Anindita Nath, 12/11/2018, CS 2302 DataStructures
#   This program is written to include the use of the Topological Sort for Graphs and Kruskal's Algorithm.
#   These are then tested by running a file with a hardcoded Graph as an input and is then displayed in
#   in the output with both the unserted array in the shape of the graph, and the answer list is displayed
#   by showing the source and the output together, seperated by a blank line from the next vertex in the
#   minimum spanning tree.
import os

class Vertex:
    def __init__(self, label):
        self.label = label

class Graph:
    def __init__(self):
        self.adjacency_list = {}
        self.edge_weights = {}

    def add_vertex(self, new_vertex):
        self.adjacency_list[new_vertex] = []

    def add_directed_edge(self, from_vertex, to_vertex, weight=1):
        self.edge_weights[(from_vertex, to_vertex)] = weight
        self.adjacency_list[from_vertex].append(to_vertex)

    def add_undirected_edge(self, vertex_a, vertex_b, weight=1):
        self.add_directed_edge(vertex_a, vertex_b, weight)
        self.add_directed_edge(vertex_b, vertex_a, weight)


class DisjointSetForest:
    def __init__(self, n):
        self.dsf = [-1] * n

    def is_index_valid(self, index):
        return 0 <= index <= len(self.dsf)

    def find(self, a):
        if not self.is_index_valid(a):
            return -1

        if self.dsf[a] < 0:
            return a

        self.dsf[a] = self.find(self.dsf[a])

        return self.dsf[a]

    def union(self, a, b):
        ra = self.find(a)
        rb = self.find(b)

        if ra != rb:
            self.dsf[rb] = ra

    def get_num_of_sets(self):
        count = 0

        for num in self.dsf:
            if num < 0:
                count += 1

        return count


class GraphALNode:
    #.item can be used to keep track of destination
    #.source used to keep track of source of node when
    # moved to different arrays
    def __init__(self, item, source, weight, next):
        self.item = item
        self.source = source
        self.weight = weight
        self.next = next


class GraphAL:

    def __init__(self, initial_num_vertices, is_directed):
        self.adj_list = [None] * initial_num_vertices
        self.is_directed = is_directed

    def is_valid_vertex(self, u):
        return 0 <= u < len(self.adj_list)

    def add_vertex(self):
        self.adj_list.append(None)

        return len(self.adj_list) - 1  # Return new vertex id

    def add_edge(self, src, dest, weight = 1.0):
        if not self.is_valid_vertex(src) or not self.is_valid_vertex(dest):
            return

        #  TODO: What if src already points to dest?
        self.adj_list[src] = GraphALNode(dest, src,  weight, self.adj_list[src])

        if not self.is_directed:
            self.adj_list[dest] = GraphALNode(src, src, weight, self.adj_list[dest])

    def remove_edge(self, src, dest):
        self.__remove_directed_edge(src, dest)

        if not self.is_directed:
            self.__remove_directed_edge(dest, src)

    def __remove_directed_edge(self, src, dest):
        if not self.is_valid_vertex(src) or not self.is_valid_vertex(dest):
            return

        if self.adj_list[src] is None:
            return

        if self.adj_list[src].item == dest:
            self.adj_list[src] = self.adj_list[src].next
        else:
            prev = self.adj_list[src]
            cur = self.adj_list[src].next

            while cur is not None:
                if cur.item == dest:
                    prev.next = cur.next
                    return

                prev = prev.next
                cur = cur.next

        return len(self.adj_list)

    def get_num_vertices(self):
        return len(self.adj_list)

    def get_vertices_reachable_from(self, src):
        reachable_vertices = set()

        temp = self.adj_list[src]

        while temp is not None:
            reachable_vertices.add(temp.item)
            temp = temp.next

        return reachable_vertices

    def get_vertices_that_point_to(self, dest):
        vertices = set()

        for i in range(len(self.adj_list)):
            temp = self.adj_list[i]

            while temp is not None:
                if temp.item == dest:
                    vertices.add(i)
                    break

                temp = temp.next

        return vertices

    def __str__(self):
        s = ""

        for i in range(len(self.adj_list)):

            s += str(i) + ": "

            temp = self.adj_list[i]

            while temp is not None:

                s += "(dest = " + str(temp.item) + " , weight = " + str(temp.weight) + ") -> "
                temp = temp.next

            s += " None\n"

        return s





def get_incoming_edge_count(edge_list, vertex):
    count = 0
    for (from_vertex, to_vertex) in edge_list:
        if to_vertex is vertex:
            count = count + 1
    return count


def topological_sort(graph):
    result_list = []

    # make list of vertices with no incoming edges.
    no_incoming = []
    for vertex in graph.adjacency_list.keys():
        if get_incoming_edge_count(graph.edge_weights.keys(), vertex) == 0:
            no_incoming.append(vertex)

    # remaining_edges starts with all edges in the graph.
    # A set is used for its efficient remove() method.
    remaining_edges = set(graph.edge_weights.keys())
    while len(no_incoming) != 0:
        # select the next vertex for the final result.
        current_vertex = no_incoming.pop()
        result_list.append(current_vertex)
        outgoing_edges = []

        # remove current_vertex's outgoing edges from remaining_edges.
        for to_vertex in graph.adjacency_list[current_vertex]:
            outgoing_edge = (current_vertex, to_vertex)
            if outgoing_edge in remaining_edges:
                outgoing_edges.append(outgoing_edge)
                remaining_edges.remove(outgoing_edge)

        # see if removing the outgoing edges creates any new vertices
        # with no incoming edges.
        for (from_vertex, to_vertex) in outgoing_edges:
            in_count = get_incoming_edge_count(remaining_edges, to_vertex)
            if in_count == 0:
                no_incoming.append(to_vertex)

    return result_list


#   Kruskal's algorithm that first orders the array by the weight of each vertex
#   then appends the vertex if it has not already been included into the list
def kruskalls_algorythm(graph):
    edgelist = []
    #Adds the list of vertices to a list to be sorted later
    for i in range(len(graph.adj_list)):
        temp = graph.adj_list[i]
        while temp is not None:
            edgelist.append(temp)
            temp = temp.next
    #   Sorts the list by weight of each node
    edgelist.sort(key = lambda x : x.weight)
    #   Allows you to check that the inputed list is
    #   sorted correctly
    # for i in range(len(edgelist)):
    #     print(edgelist[i].source)
    #     print(edgelist[i].item)
    #     print(edgelist[i].weight)
    #     print()
    t = []
    #   writes the vertices that connect in order without
    #   creating a circuit
    for i in range(len(edgelist)):
        circuit = False
        for j in range(len(t)):
            if t[j].source == edgelist[i].item:
                circuit = True
        if not circuit:
            t.append(edgelist[i])

    #   Prints the finished list
    print("answer list")
    for i in range(len(t)):
        print(t[i].source)
        print(t[i].item)
        print()


#   Creates the graph from the file by turning the line into an array
#   and placing the values accordingly into the array of the graph
#   input should be:
#   source, dest, weight
def creategraph(filename):
    graph = GraphAL(0,True)
    if not os.path.isfile(filename):
        print("File not found")
    with open(filename) as ins:
        for vertice in ins:
            verticeexists = False
            dest = False
            vertice = vertice.replace("\n", "")
            vertice = vertice.replace(" ", "")
            vertice = vertice.split(",")

            for i in range(len(graph.adj_list)):
                if graph.adj_list[i] == vertice[0]:
                    verticeexists = True
                if graph.adj_list[i] == vertice[1]:
                    dest = True
            if verticeexists is False and dest is False:
                graph.add_vertex()
                graph.add_vertex()
            elif (verticeexists is False and Dest is True) or (verticeexists is True and Dest is False):
                graph.add_vertex()
            graph.add_edge(int(vertice[0]), int(vertice[1]), int(vertice[2]))
    return graph

# def main():
#     file = input("Please write name of file")
#     filetree = creategraph(file)
#     print("Graph from file")
#     print(filetree)
#       Manuel input of the graph and its vertices
#     title = GraphAL(0, True)
#     title.add_vertex()
#     title.add_vertex()
#     title.add_edge(0,1,1)
#     title.add_vertex()
#     title.add_edge(1,0,4)
#     title.add_edge(1,2,2)
#     title.add_vertex()
#     title.add_edge(0,3,2)
#     title.add_edge(3, 2, 1)
#     print(title)
#     print()
#     print("Solution:")
#     kruskalls_algorythm(title)
#
#     print(title.adj_list[1].next.item)
#     print(title.adj_list[1].next.weight)
#
#
# main()