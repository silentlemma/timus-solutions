package main

import "syscall"

const (
	maxCoord   = 10
	side       = maxCoord + 2
	maxPixels  = maxCoord * maxCoord
	inputSize  = 64
	outputSize = 1024
	maxDigits  = 3
	letters    = "RTLB"
)

var (
	delta         = [len(letters)]int{side, 1, -side, -1}
	input         [inputSize]byte
	inputPosition int
	inputLength   int
	output        [outputSize]byte
	outputLength  int
)

// Use standard handles directly; retry interrupts and finish short writes.
func readInput(buffer []byte) int {
	for {
		count, err := syscall.Read(syscall.Stdin, buffer)
		if count > 0 {
			return count
		}
		if err != syscall.EINTR {
			return 0
		}
	}
}

func writeAll(buffer []byte) {
	for len(buffer) > 0 {
		count, err := syscall.Write(syscall.Stdout, buffer)
		if count > 0 {
			buffer = buffer[count:]
		}
		if err == syscall.EINTR {
			continue
		}
		if count <= 0 {
			return
		}
	}
}

func nextByte() byte {
	if inputPosition == inputLength {
		inputLength = readInput(input[:])
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

func header() (int, int) {
	c := nextByte()
	for c != 0 && c <= ' ' {
		c = nextByte()
	}
	first := 0
	for c >= '0' && c <= '9' {
		first = first*10 + int(c-'0')
		c = nextByte()
	}
	for c != 0 && c != '\n' && c <= ' ' {
		c = nextByte()
	}
	second := -1
	if c >= '0' && c <= '9' {
		second = 0
		for c >= '0' && c <= '9' {
			second = second*10 + int(c-'0')
			c = nextByte()
		}
	}
	for c != 0 && c != '\n' {
		c = nextByte()
	}
	return first, second
}

func writeByte(value byte) {
	output[outputLength] = value
	outputLength++
}

func writeNumber(value int) {
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
	for ; position < len(digits); position++ {
		writeByte(digits[position])
	}
}

func writeCoordinates(pixel int) {
	writeNumber(pixel / side)
	writeByte(' ')
	writeNumber(pixel % side)
	writeByte('\n')
}

func describe(count int) {
	var black [side * side]bool
	start := len(black)
	for i := 0; i < count; i++ {
		pixel := nextInt()*side + nextInt()
		black[pixel] = true
		if pixel < start {
			start = pixel
		}
	}
	var queue [maxPixels]byte
	queue[0] = byte(start)
	black[start] = false
	writeCoordinates(start)
	end := 1
	for head := 0; head < count; head++ {
		for d, step := range delta {
			next := int(queue[head]) + step
			if black[next] {
				black[next] = false
				queue[end] = byte(next)
				end++
				writeByte(letters[d])
			}
		}
		if head+1 == count {
			writeByte('.')
		} else {
			writeByte(',')
		}
		writeByte('\n')
	}
}

func list(start int) {
	var black [side * side]bool
	var queue [maxPixels]byte
	queue[0] = byte(start)
	black[start] = true
	end := 1
	for head := 0; head < end; head++ {
		for {
			code := nextByte()
			if code == ',' || code == '.' || code == 0 {
				break
			}
			for d, step := range delta {
				if code == letters[d] {
					next := int(queue[head]) + step
					black[next] = true
					queue[end] = byte(next)
					end++
					break
				}
			}
		}
	}
	writeNumber(end)
	writeByte('\n')
	for pixel, present := range black {
		if present {
			writeCoordinates(pixel)
		}
	}
}

func main() {
	first, second := header()
	if second < 0 {
		describe(first)
	} else {
		list(first*side + second)
	}
	writeAll(output[:outputLength])
}
