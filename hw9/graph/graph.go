//package graph

package main

import (
	"fmt"
	"strings"
)

// import (
//     "fmt"
//     "strings"
//   )
//var g *Graph = New(G0)
//var g2 *Graph = New(G0)

type Graph struct {
	isDirected bool
	nodes      []Node
}

type Node struct {
	ID       string
	attrs    []Attr
	Incident []edge
}

type edge struct {
	attrs  []Attr
	Source *Node
	Target *Node
}

type Attr struct {
	x, y, value int
}

// func (g *Graph) NumEdges() {
// 	//graph := strings.Split(G0, "\n")
// 	g.isDirected = true
// }

func New(x string) *Graph {
	graphdata := strings.Split(x, "\n")
	//iftrue := strings.Split(graphdata[1], " ")
	//fmt.Println(graphdata)
	graph := Graph{}
	if strings.Contains(x, "true") == true {
		graph.isDirected = true
	} else {
		graph.isDirected = false
	}

	for i := 0; i < len(graphdata)-1; i++ {
		if strings.Contains(graphdata[i], "x") {
			strings := strings.Split(graphdata[i], " ")
			x := strings[6]
			y := strings[8]
			fmt.Println(x, y)
			graph.nodes = append(graph.nodes, Node{strings[0], nil, nil})
		}
	}

	// for index, value := range graphdata {
	// 	for index2, value2 := range graph.nodes {
	// 		if strings.Contains(graphdata[index], "value") {
	// 			node := strings.Split(graphdata[index], "")
	// 			if node[0] == graph.nodes[index2].ID {
	// 				graph.nodes[index2].Incident = append(graph.nodes[index2].Incident, edge{nil, &, &graph.nodes})
	// 			}
	// 		}
	// 	}
	// }
	fmt.Println(len(graph.nodes))

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
	fmt.Println(g.isDirected)
}
