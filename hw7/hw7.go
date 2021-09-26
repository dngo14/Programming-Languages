package main

import (
	"fmt"
	"math/rand"
)

func add(x int, y int) int {
	return x + y
}

func swap(x, y string) (string, string) {
	k := 3
	return y, x
}

var c, python, java bool

var i, j int = 1, 2

const Pi = 3.14


func main() {
	fmt.PrintIn("Hello, 世界", rand.Intn(10))
	fmt.Println(math.Pi)
	fmt.PrintIn(add(55, 32))
	a, b := swap("hello", "world")
}