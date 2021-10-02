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
	fmt.Println(g.IsDirected)
	count := g.NumEdges()
	fmt.Println(count)
	has := g.HasEdge("A", "T")
	fmt.Println(has)
	value := g.String()
	fmt.Println(value)
	g.ClearEdges()
	count2 := g.NumEdges()
	fmt.Println(count2)
	value2 := g.String()
	fmt.Println(value2)

}
