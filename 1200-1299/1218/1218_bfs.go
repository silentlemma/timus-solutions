package main

import "os"

const (
	maxFighters = 200
	maxName     = 30
	parameters  = 3
	bufferSize  = 4096
)

type fighter struct {
	name   [maxName]byte
	length int
	stats  [parameters]int32
}

type reader struct {
	buffer [bufferSize]byte
	pos    int
	size   int
}

func (in *reader) nextByte() byte {
	if in.pos == in.size {
		in.size, _ = os.Stdin.Read(in.buffer[:])
		in.pos = 0
		if in.size == 0 {
			return 0
		}
	}
	c := in.buffer[in.pos]
	in.pos++
	return c
}

func (in *reader) number() int32 {
	c := in.nextByte()
	for c != 0 && c <= ' ' {
		c = in.nextByte()
	}
	sign := int32(1)
	if c == '-' || c == '+' {
		if c == '-' {
			sign = -1
		}
		c = in.nextByte()
	}
	var value int32
	for c >= '0' && c <= '9' {
		value = 10*value + int32(c-'0')
		c = in.nextByte()
	}
	return sign * value
}

func (in *reader) readName(person *fighter) {
	c := in.nextByte()
	for c != 0 && c <= ' ' {
		c = in.nextByte()
	}
	for c > ' ' {
		person.name[person.length] = c
		person.length++
		c = in.nextByte()
	}
}

func beats(a, b *fighter) bool {
	wins := 0
	for i, value := range a.stats {
		if value > b.stats[i] {
			wins++
		}
	}
	return wins >= 2
}

func main() {
	var input reader
	n := int(input.number())
	var fighters [maxFighters]fighter
	for i := 0; i < n; i++ {
		input.readName(&fighters[i])
		for j := range fighters[i].stats {
			fighters[i].stats[j] = input.number()
		}
	}
	candidate := 0
	for i := 1; i < n; i++ {
		if beats(&fighters[i], &fighters[candidate]) {
			candidate = i
		}
	}
	// Reverse reachability from this candidate gives the source component.
	var winner [maxFighters]bool
	var queue [maxFighters]byte
	winner[candidate], queue[0] = true, byte(candidate)
	end := 1
	for head := 0; head < end; head++ {
		for i := 0; i < n; i++ {
			if !winner[i] && beats(&fighters[i], &fighters[queue[head]]) {
				winner[i] = true
				queue[end] = byte(i)
				end++
			}
		}
	}
	var output [maxFighters * (maxName + 1)]byte
	used := 0
	for i := 0; i < n; i++ {
		if winner[i] {
			used += copy(output[used:], fighters[i].name[:fighters[i].length])
			output[used] = '\n'
			used++
		}
	}
	os.Stdout.Write(output[:used])
}
