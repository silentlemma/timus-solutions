package main

import (
	"fmt"
	"io/ioutil"
	"os"
)

func number(data []byte, pos *int) uint16 {
	i := *pos
	for i < len(data) && data[i] <= ' ' {
		i++
	}
	var value uint16
	for i < len(data) && data[i] >= '0' && data[i] <= '9' {
		value = value*10 + uint16(data[i]-'0')
		i++
	}
	*pos = i
	return value
}

func main() {
	data, err := ioutil.ReadAll(os.Stdin)
	if err != nil {
		return
	}
	pos := 0
	size := number(data, &pos)
	parent := make([]uint16, int(size)+1)
	height := make([]uint16, int(size)+1)
	deepest := make([]uint16, int(size)+1)
	for v := uint16(2); v <= size; v++ {
		parent[v] = number(data, &pos)
		deepest[v] = v
	}
	var diameter uint16
	endpoint := uint16(1)
	// Children have larger numbers, so a child's height is final here.
	for v := size; v > 1; v-- {
		above := parent[v]
		arm := height[v] + 1
		across := arm + height[above]
		if across > diameter {
			diameter = across
			// The longer arm reaches the middle without going above the fork.
			endpoint = deepest[v]
			if height[above] > arm {
				endpoint = deepest[above]
			}
		}
		if arm > height[above] {
			height[above] = arm
			deepest[above] = deepest[v]
		}
	}
	for step := uint16(0); step < diameter/2; step++ {
		endpoint = parent[endpoint]
	}
	if diameter%2 == 0 {
		fmt.Println(endpoint)
	} else {
		fmt.Println(parent[endpoint], endpoint)
	}
}
