package main

import (
	"bytes"
	"os"
	"sort"
	"strconv"
)

const (
	maxRecords = 1000
	nameSize   = 30
	inputSize  = 4096
	outputSize = 16
	decimal    = 10
	removed    = '6'
	renumbered = '7'
)

type record struct {
	name      [nameSize]byte
	mandatory bool
}

type records []record

func (r records) Len() int           { return len(r) }
func (r records) Swap(i, j int)      { r[i], r[j] = r[j], r[i] }
func (r records) Less(i, j int) bool { return bytes.Compare(r[i].name[:], r[j].name[:]) < 0 }

var input [inputSize]byte
var cursor, available int
var storage [maxRecords]record

func nextByte() byte {
	if cursor == available {
		available, _ = os.Stdin.Read(input[:])
		cursor = 0
		if available == 0 {
			return 0
		}
	}
	ch := input[cursor]
	cursor++
	return ch
}

func nextToken() (token [nameSize]byte) {
	ch := nextByte()
	for ch != 0 && ch <= ' ' {
		ch = nextByte()
	}
	for i := 0; ch > ' '; i++ {
		token[i] = ch
		ch = nextByte()
	}
	return token
}

func main() {
	var count int
	for _, ch := range nextToken() {
		if ch == 0 {
			break
		}
		count = count*decimal + int(ch-'0')
	}
	changed := records(storage[:0])
	for i := 0; i < count; i++ {
		name := nextToken()
		verdict := nextToken()
		switch verdict[0] {
		case 'A':
			changed = append(changed, record{name: name})
		case 'M', 'T', 'W':
			test := nextToken()
			if test[0] == removed || test[0] == renumbered {
				changed = append(changed, record{name: name, mandatory: test[0] == renumbered})
			}
		}
	}
	sort.Sort(changed)

	least, most := 0, 0
	for i := 0; i < len(changed); {
		mandatory := changed[i].mandatory
		j := i + 1
		for j < len(changed) && changed[j].name == changed[i].name {
			mandatory = mandatory || changed[j].mandatory
			j++
		}
		if mandatory {
			least++
		}
		most++
		i = j
	}
	var output [outputSize]byte
	line := strconv.AppendInt(output[:0], int64(least), decimal)
	line = strconv.AppendInt(append(line, ' '), int64(most), decimal)
	os.Stdout.Write(append(line, '\n'))
}
