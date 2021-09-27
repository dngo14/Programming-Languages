from Graph import *

class Graph:
    is_directed = ...

    class Node:
        x = None
        y = None
        def __init__ (self, x, y):
            self.x = x
            self.y = y
    nodes = {}

    class Neighbor:
        value = None
        node = None
        neighbor = None
        #neighborlist = list()
        #valuelist = list()

        def __init__ (self, value, node, neighbor):
            self.value = value
            self.node = node
            self.neighbor = neighbor
            #self.neighborlist = neighborlist
            #self.valuelist = valuelist

    adj_list = {}
    newadj_list = {}

    def __init__ (self, graph):
        self.graph = graph
        self.x = 0
        self.y = 0
        self.name = 0
        for line in self.graph:
            if "x" and "y" in line:
                words = line.split(" ")
                self.name = words[0]
                self.x = words[2]
                self.y = words[4]

                self.nodes[self.name] = self.Node(self.x,self.y)
                
        
        self.value = 0
        self.node = 0
        self.neighbor = 0
        for line in self.graph:
            if "value" in line:
                words = line.split(" ")
                self.name = words[0]
                self.value = words[2]
                self.node = words[0][0]
                self.neighbor = words[0][1]

                self.adj_list[self.name] = self.Neighbor(self.value, self.node, self.neighbor)

        #new code after discussion in class but I got to work with my old code as well
        for key, value in self.nodes.items():
            self.newadj_list[key] = list()
        for key, value in self.newadj_list.items():
            for line in self.graph:
                if "value" in line:
                    if key == line[0]:
                        self.value = line.rsplit(' ', 1)[1]
                        self.neighbor = line[1]
                        self.newadj_list[key].append(self.Neighbor(self.value, 0, self.neighbor))           


    def num_edges(self):
        self.count = 0
        return len(self.adj_list)

    
    def has_edge(self, x, y):
        for key, value in self.adj_list.items():
            if x == value.node:
                if y == value.neighbor:
                    return True
            else:
                return False
    
    def clear_edges(self):
        self.adj_list.clear()
    
    def __str__ (self):
        returnstring = 0
        if self.is_directed == True:
            returnstring = "directed true\n"  
        else:
            returnstring = "directed false\n"
        for key, value in self.nodes.items():
            returnstring += "{} fx {} fy {}\n".format(str(key), str(value.x), str(value.y))
        for key, value in self.adj_list.items():
            returnstring += "{} value {}\n".format(str(key), str(value.value))

        return returnstring.strip()
    
    def printme(self):
        for key, value in self.nodes.items():
            print(key)
            print(value.x)
    
    def explore_to_goal(self, node, end, path):
        visted[node] = True
        path2 = path.copy()
        path2.append(node)
        if node == end:
            return path2
        for key, value in g.adj_list.items():
            if key[0] == node:
                if visted[value.neighbor] == False:
                    path3 = self.explore_to_goal(value.neighbor, end, path2)
                    if len(path3) > 0:
                        return path3
        return ()

    def find_path(self, start, end):
        for key, value in visted.items():
            visted[key] = False
        path = list()
        return self.explore_to_goal(start, end, path)

    def show_nbrs(self, node):
        string = ""
        for key, value in self.adj_list.items():
            pair = {}
            if key[0] == node:
                if value.value == None:
                    string+=(f"{value.neighbor}{{}} ")
                else:
                    pair['value'] = value.value
                    string+=(f"{value.neighbor}{pair} ")
        print(string.rstrip())
    
    def edge_len(self, node, neighbor):
        for key,value in self.adj_list.items():
            if key[0] == node and key[1] == neighbor:
                if int(value.value) >= 0:
                    return int(value.value)
        print("Warning in edge_len:  unable to find edge from {} to {}\n0".format(node, neighbor))

    def set_edge_len(self, node, neighbor, value):
        for key,values in self.adj_list.items():
            if key[0] == node and key[1] == neighbor:
                values.value = int(value)
                return
        print("Warning in set_edge_len:  unable to find edge from {} to {}".format(node, neighbor))

    def add_edge(self, node, neighbor):
        self.adj_list[node+neighbor] = self.Neighbor(None, None, neighbor)
    
    def remove_edge(self, node, neighbor):
        for key,values in self.adj_list.items():
            if key[0] == node and key[1] == neighbor:
                del self.adj_list[key]
                return
    
    def sort_adj_list(self):
        self.adj_list = {key: value for key, value in sorted(self.adj_list.items())}

s = open("input_graph3").read()

def parse_graph(s):
    s = s.split("\n")
    x = s[0].split(" ")
    graph = Graph(s)
    if x[1] == "true":
        graph.is_directed = True
    else:
        graph.is_directed = False
    return graph

g = parse_graph(s)
visted = {}
for key, value in g.nodes.items():
    visted[key] = False

def explore(g, node, visted):
    print('(' + node,end="")
    visted[node] = True
    for key, value in g.adj_list.items():
        if key[0] == node:
            if visted[value.neighbor] == False:
                explore(g, value.neighbor, visted)

    #code for new adj_list that is better defined
    # if len(g.newadj_list[node])!=0:
    #     for neighbor in g.newadj_list[node]:
    #         if visted[neighbor.neighbor] == False:
    #             explore(g, neighbor.neighbor, visted)
    print(')',end="")

def DFS(g, node):
    for key, value in visted.items():
        visted[key] = False
    for key, value in visted.items():
        if visted[key] == False:
            explore(g, node, visted)

def get_path_capacity(path, graph):
    length = 0
    compare = 0
    
    minimum = int(graph.adj_list[path[0]+path[1]].value)
    while length < len(path)-1:
        for key, value in graph.adj_list.items():
            if key[0] == path[length] and key[1] == path[length+1]:
                compare = int(value.value)
                if minimum > compare:
                    minimum = compare
        length+=1
    return minimum

def add_path_to(path, graph, number):
    length = 0
    len1 = 0
    # while length < len(path)-1:
    #     for key, value in graph.adj_list.items():
    #         if key[0] == path[length] and key[1] == path[length+1]:
    #             value.value = int(value.value)+number
            
    #     length+=1
    while length < len(path)-1:
        for key, value in list(graph.adj_list.items()):
            if key[0] == path[length] and key[1] == path[length+1]:
                value.value = int(value.value)+number
            elif key[0] == path[length+1] and key[1] == path[length]:
                len1 = int(value.value)
                if len1 > number:
                    value.value = len1 - number
                else:
                    del graph.adj_list[key]
                    if len1 < number:
                        graph.adj_list[key[0]+path[length+1]] = graph.Neighbor((number - len1), key[0], path[length])
            #else:
            #    graph.adj_list[key[0]+path[length+1]] = graph.Neighbor(number, key[0], path[length])
            
        length+=1
def update_residues(path, graph, number):
    length = 0
    # while length < len(path)-1:
    #     for key, value in list(graph.adj_list.items()):
    #         if path[length+1] == key[1]:
    #             len1 = int(value.value)
    #             if len1 == number:
    #                 del graph.adj_list[key]
    #             else:
    #                 value.value = len1 - number  
    #         if key[0] == path[length+1] and key[1] == path[length]:
    #             value.value = int(value.value)+number
    #         else:
    #             graph.adj_list[path[length+1]+key[0]] = graph.Neighbor(number, path[length], key[0])
        # for key, value in list(graph.adj_list.items()):
        #     if key[1] == path[length]:
        #         len1 = int(value.value)
        #         if len1 == number:
        #             del graph.adj_list[key]
        #         else:
        #             value.value = len1 - number  
        #         if key[0] == path[length]:
        #             value.value = int(value.value)+number
        #         else:
        #             graph.adj_list[path[length]+key[0]] = graph.Neighbor(number, path[length], key[0])
        #length+=1
       
    for edge in path:
        for key, value in list(graph.adj_list.items()):
            if edge in key:
                if edge == key[1]:
                    len1 = int(value.value)
                    if len1 == number:
                        del graph.adj_list[key]
                    else:
                        value.value = len1 - number
                    if key[0] == edge:
                        value.value = int(value.value)+number
                    else:
                        graph.adj_list[edge+key[0]] = graph.Neighbor(number, edge, key[0])

def max_flow(graph, source, sink):
    g2 = graph.adj_list.copy()
    x = 1
    while x > 0:
        path = graph.find_path(source, sink)
        if len(path) < 0:
            return g2
        capacity = get_path_capacity(path, graph)
        add_path_to(path, g2, capacity)
        update_residues(path, graph, capacity)

def main():
    s = open("input_graph3").read()
    y = s.split("\n")
    x = Graph(y)
    # for line in y:
    #     if "x" and "y" in line:
    #         words = line.split(" ")
    #         print(words)
    # x.printme()
    # for line in y:
    #     if "value" in line:
    #         words = line.split(" ")
    #         print(words[0][0])
    #print(x.newadj_list)
    # for key, value in x.newadj_list.items():
    #     print(key)
        # if len(value)!=0:
        #     print(value[0].neighbor)
    #explore(g, 'C', visted)
    #DFS(g, "S")
    #x.remove_edge("A", "D")
    #x.show_nbrs("A")
    update_residues(["S", "B", "A"], x, 2)
    print(x)
    



if __name__ == "__main__":
    main()