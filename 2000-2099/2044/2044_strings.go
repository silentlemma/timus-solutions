package main

import (
	"bytes"
	"io/ioutil"
	"os"
	"strconv"
)

const alphabetSize = 26
const outputBuffer = 1 << 16

type node struct {
	next                       [alphabetSize]int32
	length, link, diff, series int32
	cache                      uint32
}

func solve(word []byte) []uint32 {
	n := len(word)
	text := make([]byte, n+1)
	copy(text[1:], word)
	nodes := make([]node, 2, n+2)
	nodes[0].length = -1
	dp := make([]uint32, n+1)
	dp[0] = 1
	last := int32(1)
	for i := 1; i <= n; i++ {
		parent, c := last, int(text[i]-'a')
		for text[i-1-int(nodes[parent].length)] != text[i] {
			parent = nodes[parent].link
		}
		if nodes[parent].next[c] == 0 {
			v := int32(len(nodes))
			nodes[parent].next[c] = v
			nodes = append(nodes, node{})
			nodes[v].length = nodes[parent].length + 2
			if nodes[v].length == 1 {
				nodes[v].link = 1
			} else {
				candidate := nodes[parent].link
				for text[i-1-int(nodes[candidate].length)] != text[i] {
					candidate = nodes[candidate].link
				}
				nodes[v].link = nodes[candidate].next[c]
			}
			suffix := nodes[v].link
			nodes[v].diff = nodes[v].length - nodes[suffix].length
			if nodes[v].diff == nodes[suffix].diff {
				nodes[v].series = nodes[suffix].series
			} else {
				nodes[v].series = suffix
			}
		}
		last = nodes[parent].next[c]
		value := uint32(0)
		for v := last; nodes[v].length > 0; v = nodes[v].series {
			cut := i - int(nodes[nodes[v].series].length) - int(nodes[v].diff)
			nodes[v].cache = dp[cut]
			suffix := nodes[v].link
			if nodes[v].diff == nodes[suffix].diff {
				nodes[v].cache |= nodes[suffix].cache
			}
			value |= nodes[v].cache << 1
		}
		dp[i] = value
	}
	return dp
}

func writeMasks(dp []uint32) {
	out := make([]byte, 0, outputBuffer)
	for _, value := range dp[1:] {
		out = strconv.AppendUint(out, uint64(value>>1), 10)
		out = append(out, '\n')
		if len(out) >= outputBuffer {
			os.Stdout.Write(out)
			out = out[:0]
		}
	}
	if len(out) > 0 {
		os.Stdout.Write(out)
	}
}

func main() {
	data, _ := ioutil.ReadAll(os.Stdin)
	writeMasks(solve(bytes.TrimSpace(data)))
}
