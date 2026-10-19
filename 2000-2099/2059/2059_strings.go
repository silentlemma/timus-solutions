package main

import (
	"bufio"
	"io"
	"os"
	"strconv"
)

const maxWordLength = 200000
const maxNodes = 2*maxWordLength + 2
const maxInputBytes = 8 * 1024 * 1024
const outputBatch = 65536

type tree struct {
	length, link, first, next, label, a, b []int32
	x, y, z                                int
}

func newTree() *tree {
	t := &tree{length: make([]int32, maxNodes), link: make([]int32, maxNodes),
		first: make([]int32, maxNodes), next: make([]int32, maxNodes), label: make([]int32, maxNodes),
		a: make([]int32, maxNodes), b: make([]int32, maxNodes)}
	t.length[0] = -1
	return t
}

func (t *tree) solve(a, b []byte) {
	t.x, t.y, t.z = 0, 0, 0
	if len(a) == 1 && len(b) == 1 {
		if a[0] == b[0] {
			t.y = 1
		} else {
			t.x, t.z = 1, 1
		}
		return
	}
	t.first[0], t.first[1] = 0, 0
	t.a[0], t.a[1], t.b[0], t.b[1] = 0, 0, 0, 0
	nodes := int32(2)
	for pass := 0; pass < 2; pass++ {
		word, counts := a, t.a
		if pass == 1 {
			word, counts = b, t.b
		}
		last := int32(1)
		for end, character := range word {
			letter, node := int32(character), last
			for end-int(t.length[node])-1 < 0 || word[end-int(t.length[node])-1] != character {
				node = t.link[node]
			}
			found := t.first[node]
			for found != 0 && t.label[found] != letter {
				found = t.next[found]
			}
			if found == 0 {
				found = nodes
				nodes++
				size, suffix := t.length[node]+2, int32(1)
				if size != 1 {
					candidate := t.link[node]
					for end-int(t.length[candidate])-1 < 0 || word[end-int(t.length[candidate])-1] != character {
						candidate = t.link[candidate]
					}
					suffix = t.first[candidate]
					for t.label[suffix] != letter {
						suffix = t.next[suffix]
					}
				}
				t.length[found], t.link[found], t.first[found] = size, suffix, 0
				t.next[found], t.label[found], t.first[node] = t.first[node], letter, found
				t.a[found], t.b[found] = 0, 0
			}
			last = found
			counts[found]++
		}
	}
	for node := nodes - 1; node >= 2; node-- {
		ca, cb, suffix := t.a[node], t.b[node], t.link[node]
		t.a[suffix] += ca
		t.b[suffix] += cb
		if ca > cb {
			t.x++
		} else if ca == cb {
			t.y++
		} else {
			t.z++
		}
	}
}

func nextLine(raw []byte, at *int) []byte {
	begin := *at
	for *at < len(raw) && raw[*at] != '\n' {
		*at++
	}
	end := *at
	if *at < len(raw) {
		*at++
	}
	if end > begin && raw[end-1] == '\r' {
		end--
	}
	return raw[begin:end]
}

func main() {
	raw := make([]byte, maxInputBytes)
	size, _ := io.ReadFull(os.Stdin, raw)
	raw = raw[:size]
	at := 0
	tests, _ := strconv.Atoi(string(nextLine(raw, &at)))
	t := newTree()
	writer := bufio.NewWriterSize(os.Stdout, outputBatch)
	output := make([]byte, 0, outputBatch)
	for index := 1; index <= tests; index++ {
		a, b := nextLine(raw, &at), nextLine(raw, &at)
		t.solve(a, b)
		output = append(output, "Case #"...)
		output = strconv.AppendInt(output, int64(index), 10)
		output = append(output, ':', ' ')
		output = strconv.AppendInt(output, int64(t.x), 10)
		output = append(output, ' ')
		output = strconv.AppendInt(output, int64(t.y), 10)
		output = append(output, ' ')
		output = strconv.AppendInt(output, int64(t.z), 10)
		output = append(output, '\n')
		if len(output) >= outputBatch {
			writer.Write(output)
			output = output[:0]
		}
	}
	writer.Write(output)
	writer.Flush()
}
