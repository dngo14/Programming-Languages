package main

import (
	"fmt"
	"math"
	"runtime"
	"time"
)

func add(x int, y int) int {
	return x + y
}

func sqrt(x float64) string {
	if x < 0 {
		return sqrt(-x) + "i"
	}
	return fmt.Sprint(math.Sqrt(x))
}

func pow(x, n, lim float64) float64 {
	if v := math.Pow(x, n); v < lim {
		return v
	}
	return lim
}

func pow2(x, n, lim float64) float64 {
	if v := math.Pow(x, n); v < lim {
		return v
	} else {
		fmt.Printf("%g >= %g\n", v, lim)
	}
	return lim
}

func Sqrt(x float64) float64 {
	z := float64(1)
	for i := 1; i <= 10; i++ {
		z -= (z*z - x) / (2 * z)
		fmt.Printf("Iteration %v, value = %v\n", i, z)
	}
	return z
}

type Vertex struct {
	X int
	Y int
}

var m = map[string]Vertex{
	"Bell Labs": {40, -74},
	"Google":    {37, -122},
}

func main() {
	var x int = 2
	fmt.Println(x)

	sum := 0
	for i := 0; i < 10; i++ {
		sum += 1
	}
	fmt.Println(sum)

	x = add(2, 3)
	fmt.Println(x)

	for sum < 1000 {
		sum += sum
	}
	fmt.Println(sum)

	for sum < 1000 {
		sum += sum
	}
	fmt.Println(sum)

	fmt.Println(sqrt(2), sqrt(-4))

	fmt.Println(
		pow(3, 2, 10),
		pow(3, 3, 20),
	)

	fmt.Println(
		pow2(3, 2, 10),
		pow2(3, 3, 20),
	)

	fmt.Println(Sqrt(2))

	switch os := runtime.GOOS; os {
	case "darwin":
		fmt.Println("OS X.")
	case "linux":
		fmt.Println("Linux.")
	default:
		fmt.Printf("%s.\n", os)
	}

	t := time.Now()
	switch {
	case t.Hour() < 12:
		fmt.Println("Good morning!")
	case t.Hour() < 17:
		fmt.Println("Good afternoon.")
	default:
		fmt.Println("Good evening.")
	}

	//defer fmt.Println("world")

	fmt.Println("hello")

	fmt.Println("counting")

	//for i := 0; i < 10; i++ {
	//	defer fmt.Println(i)
	//}

	fmt.Println("done")

	i, j := 42, 2701

	p := &i         // point to i
	fmt.Println(*p) // read i through the pointer
	*p = 21         // set i through the pointer
	fmt.Println(i)  // see the new value of i

	p = &j         // point to j
	*p = *p / 37   // divide j through the pointer
	fmt.Println(j) // see the new value of j

	fmt.Println(Vertex{1, 2})
	v := Vertex{1, 2}
	v.X = 4
	fmt.Println(v.X)

	k := &v
	k.X = 1e9
	fmt.Println(v)

	var a [10]int
	a[0] = 2

	primes := [6]int{}
	primes[0] = 2
	fmt.Println(primes)

	var s []int = primes[1:4]
	fmt.Println(s)

	q := []int{2, 3, 5, 7, 11, 13}
	q = q[1:4]
	fmt.Println(q)

	l := make([]int, 5)
	fmt.Println(l)

	var s1 []int
	s1 = append(s1, 2, 3, 4)
	fmt.Printf("Your values are %d", s1)

	pow := []int{1, 2, 4, 8, 16, 32, 64, 128}
	for i, v := range pow {
		fmt.Printf("index: %d value: %d", i, v)
	}
	for i, _ := range pow {
		fmt.Println(i)
	}
	for _, value := range pow {
		fmt.Println(value)
	}

	vm := map[string]Vertex{
		"Bell Labs": Vertex{
			40, 74,
		},
		"Google": Vertex{
			37, 122,
		},
	}
	fmt.Println(vm)

	m := make(map[string]int)

	m["Answer"] = 42
	fmt.Println("The value:", m["Answer"])

	m["Answer"] = 48
	fmt.Println("The value:", m["Answer"])

	delete(m, "Answer")
	fmt.Println("The value:", m["Answer"])

	v2, ok := m["Answer"]
	fmt.Println("The value:", v2, "Present?", ok)
}
