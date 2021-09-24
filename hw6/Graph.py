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

        return returnstring
    
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

s = open("input_graph").read()

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



def main():
    s = open("input_graph").read()
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
    x.remove_edge("A", "D")
    x.show_nbrs("A")
    #print(y)
    



if __name__ == "__main__":
    main()