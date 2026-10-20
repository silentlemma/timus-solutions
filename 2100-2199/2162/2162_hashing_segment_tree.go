package main

import (
	"fmt"
	"io/ioutil"
	"os"
)

const labelBase int64 = 1000000001
const space byte = ' '

func maximum(first, second int) int {
	if first > second {
		return first
	}
	return second
}

func main() {
	data, _ := ioutil.ReadAll(os.Stdin)
	position := 0
	nextInt := func() int {
		for position < len(data) && data[position] <= space {
			position++
		}
		value := 0
		for position < len(data) && data[position] > space {
			value = value*10 + int(data[position]-'0')
			position++
		}
		return value
	}

	length := nextInt()
	values := make([]int, length)
	tree := make([]int, 2*length)
	for index := range values {
		values[index] = nextInt()
		tree[length+index] = values[index]
	}
	for index := length - 1; index > 0; index-- {
		tree[index] = maximum(tree[2*index], tree[2*index+1])
	}

	goodUntil := make([]int, length)
	for offset := 0; offset < 2; offset++ {
		nextEdge := make(map[int64]int, length/2)
		limit := length
		for start := length - 2 - offset; start >= 0; start -= 2 {
			first, second := values[start], values[start+1]
			if first == 0 || second == 0 || first == second {
				limit = start
			} else {
				if first > second {
					first, second = second, first
				}
				key := int64(first)*labelBase + int64(second)
				if next, found := nextEdge[key]; found && next < limit {
					limit = next
				}
				nextEdge[key] = start
			}
			goodUntil[start] = limit
		}
	}

	answer := 0
	for start := 0; start+1 < length; start++ {
		vertices, edges := values[start], values[start+1]
		if vertices == 0 || edges > (length-start-2)/2 {
			continue
		}
		if edges == 0 {
			answer++
			continue
		}
		end := start + 2 + 2*edges
		if end > goodUntil[start+2] {
			continue
		}
		left, right := length+start+2, length+end
		largest := 0
		for left < right {
			if left%2 == 1 {
				largest = maximum(largest, tree[left])
				left++
			}
			if right%2 == 1 {
				right--
				largest = maximum(largest, tree[right])
			}
			left /= 2
			right /= 2
		}
		if largest <= vertices {
			answer++
		}
	}
	fmt.Println(answer)
}
