package main

import (
	"io"
	"io/ioutil"
)

import (
	"bufio"

	"os"
	"sort"
	"strconv"
)

type edge struct{ a, b, length int }

func main() {
	in := bufio.NewReader(os.Stdin)
	var n, m int
	fastScan(in, &n, &m)
	edges := make([]edge, m)
	for k := range edges {
		fastScan(in, &edges[k].a, &edges[k].b, &edges[k].length)
	}
	sort.SliceStable(edges, func(x, y int) bool { return edges[x].length < edges[y].length })
	parent := make([]int, n+1)
	for v := range parent {
		parent[v] = v
	}
	find := func(v int) int {
		for parent[v] != v {
			parent[v] = parent[parent[v]]
			v = parent[v]
		}
		return v
	}
	// Kruskal's tree: its longest cable is the smallest possible longest cable
	// of any plan that connects every hub
	var chosen []edge
	for _, e := range edges {
		if ra, rb := find(e.a), find(e.b); ra != rb {
			parent[ra] = rb
			chosen = append(chosen, e)
		}
	}
	out := bufio.NewWriter(os.Stdout)
	defer out.Flush()
	out.WriteString(strconv.Itoa(chosen[len(chosen)-1].length) + "\n")
	out.WriteString(strconv.Itoa(len(chosen)) + "\n")
	for _, e := range chosen {
		out.WriteString(strconv.Itoa(e.a) + " " + strconv.Itoa(e.b) + "\n")
	}
}

var fastInputData []byte
var fastInputPosition int
var fastInputLoaded bool

// Read the single input stream once and convert tokens without fmt reflection.
func fastScan(reader io.Reader, targets ...interface{}) (int, error) {
	if !fastInputLoaded {
		var err error
		fastInputData, err = ioutil.ReadAll(reader)
		if err != nil {
			return 0, err
		}
		fastInputLoaded = true
	}
	for index, target := range targets {
		for fastInputPosition < len(fastInputData) && fastInputData[fastInputPosition] <= ' ' {
			fastInputPosition++
		}
		start := fastInputPosition
		for fastInputPosition < len(fastInputData) && fastInputData[fastInputPosition] > ' ' {
			fastInputPosition++
		}
		if start == fastInputPosition {
			return index, io.EOF
		}
		word := string(fastInputData[start:fastInputPosition])
		var err error
		switch value := target.(type) {
		case *string:
			*value = word
		case *int:
			*value, err = strconv.Atoi(word)
		case *int64:
			*value, err = strconv.ParseInt(word, 10, 64)
		case *uint64:
			*value, err = strconv.ParseUint(word, 10, 64)
		case *float64:
			*value, err = strconv.ParseFloat(word, 64)
		default:
			panic("unsupported input type")
		}
		if err != nil {
			return index, err
		}
	}
	return len(targets), nil
}
