package graph

import (
	"testing"
)

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
var g2 *Graph = New(G0)

func TestIsDirected(t *testing.T) {
	want := true
	got := g.IsDirected
	if got != want {
		t.Fatalf(`g.IsDirected = %v, want %v`, got, want)
	}
}

func TestNumEdges(t *testing.T) {
	want := 11
	got := g.NumEdges()
	if got != want {
		t.Fatalf(`g.NumEdges() = %v, want %v`, got, want)
	}
}

func TestHasEdge(t *testing.T) {
	want := true
	got := g.HasEdge("A", "D")
	if got != want {
		t.Fatalf(`g.HasEdge("A", "D") = %v, want %v`, got, want)
	}
	want = false
	got = g.HasEdge("A", "T")
	if got != want {
		t.Fatalf(`g.HasEdge("A", "T") = %v, want %v`, got, want)
	}
}

func TestClearEdges(t *testing.T) {
	want := 0
	g2.ClearEdges()
	got := g2.NumEdges()
	if got != want {
		t.Fatalf(`after g2.ClearEdges(), g2.NumEdges() = %v, want %v`, got, want)
	}
}

func TestGraphString(t *testing.T) {
	want := `directed true
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
	got := g.String()
	if got != want {
		t.Fatalf(`g.String() = %v, want %v`, got, want)
	}
	want = `directed true
A x 190 y 50
B x 170 y 210
C x 170 y 370
D x 390 y 50
E x 410 y 370
S x 50 y 210
T x 550 y 210
`
	got = g2.String()
	if got != want {
		t.Fatalf(`g2.String() = %v, want %v`, got, want)
	}
}
