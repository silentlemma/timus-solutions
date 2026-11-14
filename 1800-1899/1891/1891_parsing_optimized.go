package main

import "syscall"

type valueType uint8

const (
	auto valueType = iota
	integer
	real
	text
)

const (
	letterBits = 6
	wordBits   = 64
	typeBits   = 2
	tableSize  = 256
	lineBuffer = 512
	decimal    = 10
	maxNames   = 100
	maxName    = 20
	maxType    = len("string")
)

const hashMultiplier uint64 = 11400714819323198485
const hashShift = 56

var typeNames = [...]string{"auto", "int", "real", "string"}

type symbol struct{ high, low uint64 }

// Store the case-sensitive name exactly in two words, with nonzero digits.
func pack(name []byte) symbol {
	var key symbol
	for _, c := range name {
		var digit byte
		if c >= 'a' {
			digit = c - 'a' + 1
		} else {
			digit = c - 'A' + 1 + ('z' - 'a' + 1)
		}
		key.high = key.high<<letterBits | key.low>>(wordBits-letterBits)
		key.low = key.low<<letterBits | uint64(digit)
	}
	return key
}

type signature struct {
	name symbol
	args uint32
}

type entry struct {
	key  signature
	kind valueType
}

type symbols [tableSize]entry

func (table *symbols) slot(key signature) *entry {
	hash := (key.name.low ^ key.name.high*hashMultiplier) + uint64(key.args)
	index := int(hash * hashMultiplier >> hashShift)
	for table[index].kind != auto && table[index].key != key {
		index = (index + 1) & (tableSize - 1)
	}
	return &table[index]
}

func letter(c byte) bool {
	return 'a' <= c && c <= 'z' || 'A' <= c && c <= 'Z'
}

func word(line *[]byte) []byte {
	s := *line
	for len(s) != 0 && !letter(s[0]) {
		s = s[1:]
	}
	end := 0
	for end < len(s) && letter(s[end]) {
		end++
	}
	*line = s[end:]
	return s[:end]
}

func kind(s []byte) valueType {
	switch string(s) {
	case "int":
		return integer
	case "real":
		return real
	case "string":
		return text
	}
	return auto
}

const inputSize = 4096

var input [inputSize]byte
var offset, end int
var lineBytes [lineBuffer]byte
var functions, variables symbols

func nextLine() []byte {
	line := lineBytes[:0]
	for {
		if offset == end {
			size, err := syscall.Read(syscall.Stdin, input[:])
			if err == syscall.EINTR {
				continue
			}
			if size <= 0 {
				return line
			}
			offset, end = 0, size
		}
		first := offset
		for offset < end && input[offset] != '\n' {
			offset++
		}
		line = append(line, input[first:offset]...)
		if offset < end {
			offset++
			return line
		}
	}
}

func lineCount(line []byte) int {
	value := 0
	for _, digit := range line {
		if '0' <= digit && digit <= '9' {
			value = value*decimal + int(digit-'0')
		}
	}
	return value
}

func appendNumber(output []byte, value int) []byte {
	const digitsInLine = 3
	var digits [digitsInLine]byte
	start := len(digits)
	for value != 0 {
		start--
		digits[start] = '0' + byte(value%decimal)
		value /= decimal
	}
	return append(output, digits[start:]...)
}

func write(data []byte) {
	for len(data) > 0 {
		n, err := syscall.Write(syscall.Stdout, data)
		if err == syscall.EINTR {
			continue
		}
		if n <= 0 {
			return
		}
		data = data[n:]
	}
}

func main() {
	headers := lineCount(nextLine())
	for i := 0; i < headers; i++ {
		line := nextLine()
		key := signature{name: pack(word(&line))}
		last := kind(word(&line))
		for token := word(&line); len(token) != 0; token = word(&line) {
			key.args = key.args<<typeBits | uint32(last)
			last = kind(token)
		}
		*functions.slot(key) = entry{key, last}
	}
	declarations := lineCount(nextLine())
	var output [maxNames * (maxName + len(" : ") + maxType + 1)]byte
	inferred := output[:0]
	for i := 1; i <= declarations; i++ {
		line := nextLine()
		declared, name := kind(word(&line)), word(&line)
		variable := signature{name: pack(name)}
		destination := variables.slot(variable)
		key := signature{name: pack(word(&line))}
		message := ""
		if destination.kind != auto {
			message = "Double declaration"
		}
		for token := word(&line); message == "" && len(token) != 0; token = word(&line) {
			arg := variables.slot(signature{name: pack(token)}).kind
			if arg == auto {
				message = "Unknown variable"
			} else {
				key.args = key.args<<typeBits | uint32(arg)
			}
		}
		if message == "" {
			result := functions.slot(key).kind
			switch {
			case result == auto:
				message = "No such function"
			case declared != auto && declared != result:
				message = "Invalid initialization"
			default:
				*destination = entry{variable, result}
				if declared == auto {
					inferred = append(inferred, name...)
					inferred = append(inferred, " : "...)
					inferred = append(inferred, typeNames[result]...)
					inferred = append(inferred, '\n')
				}
			}
		}
		if message != "" {
			inferred = append(inferred[:0], "Error on line "...)
			inferred = appendNumber(inferred, i)
			inferred = append(inferred, ": "...)
			inferred = append(inferred, message...)
			inferred = append(inferred, '\n')
			write(inferred)
			return
		}
	}
	write(inferred)
}
