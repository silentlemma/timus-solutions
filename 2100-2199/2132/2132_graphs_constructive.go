package main

import (
	"bufio"
	"io/ioutil"
	"os"
	"strconv"
)

const (
	maxLabel   = 100000
	rootParent = -1
	bufferSize = 65536
)

type path struct {
	first  int
	center int
	last   int
}

type scanner struct {
	data     []byte
	position int
}

func (input *scanner) nextInt() (int, bool) {
	for input.position < len(input.data) && input.data[input.position] <= ' ' {
		input.position++
	}
	if input.position == len(input.data) {
		return 0, false
	}
	value := 0
	for input.position < len(input.data) && input.data[input.position] >= '0' {
		value = value*10 + int(input.data[input.position]-'0')
		input.position++
	}
	return value, true
}

func main() {
	data, err := ioutil.ReadAll(os.Stdin)
	if err != nil {
		return
	}
	input := scanner{data: data}
	adjacent := make([][]int, maxLabel+1)
	largest := 0
	for {
		first, ok := input.nextInt()
		if !ok {
			break
		}
		second, _ := input.nextInt()
		adjacent[first] = append(adjacent[first], second)
		adjacent[second] = append(adjacent[second], first)
		if first > largest {
			largest = first
		}
		if second > largest {
			largest = second
		}
	}

	parent := make([]int, largest+1)
	rank := make([]int, largest+1)
	order := make([]int, 0, largest)
	stack := make([]int, 0, largest)
	for root := 1; root <= largest; root++ {
		if parent[root] != 0 || len(adjacent[root]) == 0 {
			continue
		}
		parent[root] = rootParent
		stack = append(stack, root)
		for len(stack) != 0 {
			vertex := stack[len(stack)-1]
			stack = stack[:len(stack)-1]
			rank[vertex] = len(order)
			order = append(order, vertex)
			for _, endpoint := range adjacent[vertex] {
				if parent[endpoint] == 0 {
					parent[endpoint] = vertex
					stack = append(stack, endpoint)
				}
			}
		}
	}

	usedParent := make([]bool, largest+1)
	answer := make([]path, 0)
	writer := bufio.NewWriterSize(os.Stdout, bufferSize)
	defer writer.Flush()
	for position := len(order) - 1; position >= 0; position-- {
		vertex := order[position]
		pending := 0
		for _, endpoint := range adjacent[vertex] {
			if endpoint == parent[vertex] {
				continue
			}
			if parent[endpoint] == vertex {
				if usedParent[endpoint] {
					continue
				}
			} else if rank[endpoint] > rank[vertex] {
				continue
			}
			if pending == 0 {
				pending = endpoint
			} else {
				answer = append(answer, path{pending, vertex, endpoint})
				pending = 0
			}
		}
		if pending != 0 {
			if parent[vertex] == rootParent {
				writer.WriteString(strconv.Itoa(rootParent))
				writer.WriteByte('\n')
				return
			}
			answer = append(answer, path{pending, vertex, parent[vertex]})
			usedParent[vertex] = true
		}
	}

	output := strconv.AppendInt(nil, int64(len(answer)), 10)
	output = append(output, '\n')
	for _, item := range answer {
		output = strconv.AppendInt(output, int64(item.first), 10)
		output = append(output, ' ')
		output = strconv.AppendInt(output, int64(item.center), 10)
		output = append(output, ' ')
		output = strconv.AppendInt(output, int64(item.last), 10)
		output = append(output, '\n')
	}
	writer.Write(output)
}
