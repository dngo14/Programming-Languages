package graph

//package main

import (
	"fmt"
	"strconv"
	"strings"
)

// import (
//     "fmt"
//     "strings"
//   )
//var g *Graph = New(G0)
//var g2 *Graph = New(G0)

type Graph struct {
	IsDirected bool
	nodes      []Node
}

type Node struct {
	ID       string
	attrs    Attr
	Incident []edge
}

type edge struct {
	attrs  Attr
	Source *Node
	Target *Node
}

type Attr struct {
	x, y, value int
	name        string
	//value int
}

func (g *Graph) isdirected() bool {
	if g.IsDirected == true {
		return true
	} else {
		return false
	}
}

func (g *Graph) NumEdges() int {
	count := 0
	for i := 0; i < len(g.nodes); i++ {
		for j := 0; j < len(g.nodes[i].Incident); j++ {
			count += 1
		}
	}
	return count
}

func (g *Graph) HasEdge(x, y string) bool {
	for i := 0; i < len(g.nodes)-1; i++ {
		if g.nodes[i].ID == x {
			for j := 0; j < len(g.nodes[i].Incident); j++ {
				if g.nodes[i].Incident[j].Target.ID == y {
					return true
				} else {
					return false
				}
			}
		}
	}
	return false
}

func (g *Graph) String() string {
	stringvalue := "directed "
	stringvalue += strconv.FormatBool(g.IsDirected) + "\n"
	for i := 0; i < len(g.nodes); i++ {
		x := strconv.Itoa(g.nodes[i].attrs.x)
		y := strconv.Itoa(g.nodes[i].attrs.y)
		stringvalue += g.nodes[i].ID + " x " + x + " y " + y + "\n"
	}
	for i := 0; i < len(g.nodes); i++ {
		if len(g.nodes[i].Incident) > 0 {
			for j := 0; j < len(g.nodes[i].Incident); j++ {
				mainnode := g.nodes[i].Incident[j].Source.ID
				neighbor := g.nodes[i].Incident[j].Target.ID
				value := strconv.Itoa(g.nodes[i].Incident[j].attrs.value)
				stringvalue += mainnode + neighbor + " value " + value + "\n"
			}
		}
	}
	//stringvalue = strings.TrimSuffix(stringvalue, "\n")
	return stringvalue
}

func (g *Graph) ClearEdges() {
	for i := 0; i < len(g.nodes); i++ {
		if len(g.nodes[i].Incident) > 0 {
			for j := 0; j < len(g.nodes[i].Incident); j++ {
				g.nodes[i].Incident = nil
			}
		}
	}
}

func (g *Graph) Node(ID string) *Node {
	var node *Node
	for i := 0; i < len(g.nodes); i++ {
		if ID == g.nodes[i].ID {
			node = &g.nodes[i]
			return node
		}
	}
	return node
}

func (g *Graph) Edge(ID0 string, ID1 string) *edge {
	var edge *edge
	for i := 0; i < len(g.nodes); i++ {
		if ID0 == g.nodes[i].ID {
			for j := 0; j < len(g.nodes[i].Incident); j++ {
				if g.nodes[i].Incident[j].Target.ID == ID1 {
					edge = &g.nodes[i].Incident[j]
					return edge
				}
			}
		}
	}
	return edge
}

func (n *Node) String() string {
	var stringnode string
	stringnode += n.ID + " attrs: x " + strconv.Itoa(n.attrs.x) + " y " + strconv.Itoa(n.attrs.y) + "  incident: "
	for j := 0; j < len(n.Incident); j++ {
		stringnode += " " + n.Incident[j].Target.ID + "(value " + strconv.Itoa(n.Incident[j].attrs.value) + ")"
	}
	return stringnode
}

func (g *Graph) NbrsOf(ID string) {
	var stringneighbors string = "["
	for i := 0; i < len(g.nodes); i++ {
		if ID == g.nodes[i].ID {
			for j := 0; j < len(g.nodes[i].Incident); j++ {
				stringneighbors += g.nodes[i].Incident[j].Target.ID + " "
			}
			stringneighbors = strings.TrimSpace(stringneighbors)
			stringneighbors += "]"
		}
	}
	fmt.Println(stringneighbors)
}

var visted map[string]bool

func explore(g *Graph, node string) {
	fmt.Print("(" + node)
	if visted == nil {
		visted = make(map[string]bool)
		for i := 0; i < len(g.nodes); i++ {
			visted[g.nodes[i].ID] = false
			//fmt.Println(visted)
		}
	}
	visted[node] = true
	//fmt.Println(visted)

	for i := 0; i < len(g.nodes); i++ {
		if g.nodes[i].ID == node {
			for j := 0; j < len(g.nodes[i].Incident); j++ {
				if visted[g.nodes[i].Incident[j].Target.ID] == false {
					explore(g, g.nodes[i].Incident[j].Target.ID)
				}
			}
		}
	}
	fmt.Print(")")
}

func (g *Graph) ClearVisited() {
	for index, _ := range visted {
		visted[index] = false
	}
}

func DFS(g *Graph) {
	for _, value := range g.nodes {
		if visted[value.ID] == false {
			explore(g, value.ID)
		}
	}
}

func FindPath(g *Graph, start string, goal string) []string {
	if visted == nil {
		visted = make(map[string]bool)
		for i := 0; i < len(g.nodes); i++ {
			visted[g.nodes[i].ID] = false
			//fmt.Println(visted)
		}
	}
	var list1 []string
	return explore_to_goal(g, start, goal, list1)
}

func explore_to_goal(g *Graph, start string, goal string, list []string) []string {
	visted[start] = true
	list2 := make([]string, len(list))
	copy(list2, list)
	list2 = append(list2, start)
	if start == goal {
		return list2
	}
	for i := 0; i < len(g.nodes); i++ {
		if g.nodes[i].ID == start {
			for j := 0; j < len(g.nodes[i].Incident); j++ {
				if visted[g.nodes[i].Incident[j].Target.ID] == false {
					list3 := explore_to_goal(g, g.nodes[i].Incident[j].Target.ID, goal, list2)
					if len(list3) > 0 {
						return list3
					}
				}
			}
		}
	}
	var nilsclice []string
	return nilsclice
}

func GetPathCapacity(list []string, g *Graph) int {
	//length := 0
	minimum := 0
	// for i := 0; i < len(g.nodes); i++ {
	// 	if g.nodes[i].ID == list[0] {
	// 		for j := 0; j < len(g.nodes[i].Incident); j++ {
	// 			if g.nodes[i].Incident[j].Target.ID == list[1] {
	// 				minimum = g.nodes[i].Incident[j].attrs.value
	// 			}
	// 		}
	// 	}
	// }
	count := 0
	for count <= len(list)-1 {
		for i := 0; i < len(g.nodes); i++ {
			if g.nodes[i].ID == list[count] {
				for j := 0; j < len(g.nodes[i].Incident); j++ {
					if g.nodes[i].Incident[j].Target.ID == list[count+1] {
						if minimum >= g.nodes[i].Incident[j].Target.attrs.value {
							minimum = g.nodes[i].Incident[j].attrs.value
						}
					}
				}
			}
		}
		count = count + 1
	}
	return minimum
}

func New(x string) *Graph {
	graphdata := strings.Split(x, "\n")
	//iftrue := strings.Split(graphdata[1], " ")
	//fmt.Println(graphdata)
	graph := Graph{}
	if strings.Contains(x, "true") == true {
		graph.IsDirected = true
	} else {
		graph.IsDirected = false
	}
	for i := 0; i < len(graphdata); i++ {
		if strings.Contains(graphdata[i], "x") {
			strings := strings.Fields(graphdata[i])
			x := strings[2]
			xint, _ := strconv.Atoi(x)
			y := strings[4]
			yint, _ := strconv.Atoi(y)
			graph.nodes = append(graph.nodes, Node{strings[0], Attr{xint, yint, 0, ""}, nil})

		}
	}

	for index, _ := range graphdata {
		for index2, _ := range graph.nodes {
			if strings.Contains(graphdata[index], "value") {
				//node := strings.Split(graphdata[index], "")
				node := strings.Fields(graphdata[index])
				mainnode := strings.Split(node[0], "")
				//fmt.Println(graph.nodes[index2].ID)
				if mainnode[0] == graph.nodes[index2].ID {
					neighbor := mainnode[1]
					source := &graph.nodes[index2]
					length, _ := strconv.Atoi(node[len(node)-1])
					var neighboraddress *Node
					for index3, _ := range graph.nodes {
						if neighbor == graph.nodes[index3].ID {
							neighboraddress = &graph.nodes[index3]
							break
						}
					}
					graph.nodes[index2].Incident = append(graph.nodes[index2].Incident, edge{Attr{0, 0, length, ""}, source, neighboraddress})
				}
			}
		}
	}
	//fmt.Println(graph.nodes[0].Incident[0])

	return &graph
}

func main() {
	const G0 = `
    Graph 7 11 true
    A x 190 y 50
    B x 170 y 210
    C x 170 y 370
    D x 390 y 50
    E x 410 y 370
    S x 50 y 210
    T x 550 y 210
    AD value 2
    BA value 10
    BD value 1
    CE value 5
    DC value 1
    DE value 1
    DT value 2
    ET value 5
    SA value 3
    SB value 3
    SC value 4
    `
	var g *Graph = New(G0)
	// fmt.Println(g.IsDirected)
	// count := g.NumEdges()
	// fmt.Println(count)
	// has := g.HasEdge("A", "T")
	// fmt.Println(has)
	// value := g.String()
	// fmt.Println(value)
	// g.ClearEdges()
	// count2 := g.NumEdges()
	// fmt.Println(count2)
	// value2 := g.String()
	// fmt.Println(value2)
	x := FindPath(g, "S", "T")
	fmt.Println(x)
	y := GetPathCapacity([]string{"S", "A", "D", "T"}, g)
	fmt.Println(y)
}
