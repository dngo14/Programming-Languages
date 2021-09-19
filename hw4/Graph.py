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
        def __init__ (self, value, node, neighbor):
            self.value = value
            self.node = node
            self.neighbor = neighbor

    adj_list = {}

    def __init__ (self, graph):
        self.graph = graph
        self.x = 0
        self.y = 0
        self.name = 0
        count = 0
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
    


def main():
    s = open("input_graph").read()
    y = s.split("\n")
    x = Graph(y)
    for line in y:
        if "x" and "y" in line:
            words = line.split(" ")
            print(words)
    x.printme()
    # for line in y:
    #     if "value" in line:
    #         words = line.split(" ")
    #         print(words[0][0])



if __name__ == "__main__":
    main()