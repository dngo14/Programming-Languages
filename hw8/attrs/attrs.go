//package attrs

package main

import (
	"fmt"
	"math"
	"strconv"
	"strings"
)

type Attr struct {
	x string
	y int
}

func HasAttr(x []Attr, y string) bool {
	for _, value := range x {
		if value.x == y {
			return true
		}
		//fmt.Print(value)
	}
	return false
}

func RemoveAttr(x []Attr, y string) []Attr {
	var count int
	for index, value := range x {
		if value.x == y {
			count = index
		}
	}
	copylist := append(x[:count], x[count+1:]...)
	return copylist
}

var NonAttrVal = math.MinInt32

func UpdateAttr(x []Attr, y Attr) []Attr {
	var count int = 0
	var attrs []Attr
	for _, value := range x {
		if y.y == math.MinInt32 {
			//x[count] = nil
			attrs = append(x[:count], x[count+1:]...)
			//x = j
			//fmt.Println(j)
			//fmt.Print(attrs)
			return attrs
		} else if value.x == y.x {
			x[count].y = y.y
		}
		count++
	}
	//fmt.Println(x)
	//fmt.Print(x)
	return x
}

func UpdateMultiAttr(x []Attr, y []Attr) []Attr {
	var count int = 0
	for _, value := range x {
		for _, value2 := range y {
			if value.x == value2.x {
				//k := &x[count]
				//k.y = value2.y
				x[count].y = value2.y
			}
		}
		count++
	}
	for i := 0; i < len(x); i++ {
		if x[0].y == math.MinInt32 {
			x = append(x[:i], x[i+1:]...)
			i--
		}
	}
	//fmt.Println(x)
	//fmt.Print(x)
	return x
}

func AttrsFromString(x string) []Attr {
	var attrs []Attr
	s := strings.Split(x, " ")
	//fmt.Println(len(s))
	for i := 0; i < len(s); i = i + 2 {
		num, _ := strconv.Atoi(s[i+1])
		//fmt.Println(num, num2)
		attrs = append(attrs, Attr{s[i], num})
	}
	return attrs
}

func main() {
	attrs := []Attr{{"a", 3}, {"b", 4}}
	//fmt.Println(attrs)
	//y := RemoveAttr(attrs, "a")
	//fmt.Println(y)
	//fmt.Println(NonAttrVal)
	//fmt.Println(attrs)
	x := UpdateAttr(attrs, Attr{"a", 17})
	fmt.Println(x)
	//fmt.Println(attrs)
	//UpdateAttr(attrs, Attr{"a", NonAttrVal})
	//fmt.Println(attrs)
	//UpdateMultiAttr(attrs, []Attr{{"b", 5}, {"a", NonAttrVal}})
	fmt.Println(attrs)
	//AttrsFromString("d 3 e 4")
	//fmt.Println(attrs)
}
