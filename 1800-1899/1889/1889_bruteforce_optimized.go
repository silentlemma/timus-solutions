package main

import "os"

const (
	maxPhrases = 1000
	maxName    = 20
	tableSize  = 2048
	inputSize  = 64
	outputSize = 128
	maxDigits  = 4
	fnvOffset  = uint32(2166136261)
	fnvPrime   = uint32(16777619)
)

type group struct {
	name        [maxName]byte
	first, last uint16
}

var (
	input         [inputSize]byte
	inputPosition int
	inputLength   int
	groups        [maxPhrases]group
	table         [tableSize]uint16
	unknown       = [maxName]byte{'u', 'n', 'k', 'n', 'o', 'w', 'n'}
)

func nextByte() byte {
	if inputPosition == inputLength {
		inputLength, _ = os.Stdin.Read(input[:])
		inputPosition = 0
		if inputLength == 0 {
			return 0
		}
	}
	value := input[inputPosition]
	inputPosition++
	return value
}

func nextInt() int {
	c := nextByte()
	for c != 0 && c <= ' ' {
		c = nextByte()
	}
	value := 0
	for c >= '0' && c <= '9' {
		value = value*10 + int(c-'0')
		c = nextByte()
	}
	return value
}

func nextName() ([maxName]byte, uint32) {
	c := nextByte()
	for c != 0 && c <= ' ' {
		c = nextByte()
	}
	var name [maxName]byte
	length := 0
	hash := fnvOffset
	for c >= 'a' && c <= 'z' {
		name[length] = c
		length++
		hash = (hash ^ uint32(c)) * fnvPrime
		c = nextByte()
	}
	return name, hash
}

func appendNumber(output []byte, value int) []byte {
	var digits [maxDigits]byte
	position := len(digits)
	for {
		position--
		digits[position] = '0' + byte(value%10)
		value /= 10
		if value == 0 {
			break
		}
	}
	return append(output, digits[position:]...)
}

func main() {
	n := nextInt()
	count := 0
	for i := 0; i < n; i++ {
		name, hash := nextName()
		if name == unknown {
			continue
		}
		if count > 0 && groups[count-1].name == name {
			groups[count-1].last = uint16(i)
			continue
		}
		// A language cannot reappear after a different known language.
		slot := hash & (tableSize - 1)
		for table[slot] != 0 {
			if groups[table[slot]-1].name == name {
				os.Stdout.WriteString("Igor is wrong.\n")
				return
			}
			slot = (slot + 1) & (tableSize - 1)
		}
		groups[count] = group{name, uint16(i), uint16(i)}
		count++
		table[slot] = uint16(count)
	}
	var storage [outputSize]byte
	output := storage[:0]
	for languages := 1; languages <= n; languages++ {
		if languages < count || n%languages != 0 {
			continue
		}
		length := uint16(n / languages)
		last := -1
		valid := true
		for _, item := range groups[:count] {
			block := int(item.first / length)
			if block == last || item.last/length != uint16(block) {
				valid = false
				break
			}
			last = block
		}
		if valid {
			if len(output) > 0 {
				output = append(output, ' ')
			}
			output = appendNumber(output, languages)
		}
	}
	if len(output) == 0 {
		os.Stdout.WriteString("Igor is wrong.\n")
	} else {
		os.Stdout.Write(append(output, '\n'))
	}
}
