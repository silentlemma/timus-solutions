package main

import "os"

const (
	maxLength  = 10000
	bufferSize = 4096
	hexRadix   = 16
	digits     = "0123456789ABCDEF"
)

type input struct {
	bytes            [bufferSize]byte
	position, length int
}

func (in *input) next() byte {
	if in.position == in.length {
		in.length, _ = os.Stdin.Read(in.bytes[:])
		in.position = 0
		if in.length == 0 {
			return 0
		}
	}
	c := in.bytes[in.position]
	in.position++
	return c
}

func hexValue(c byte) byte {
	if c <= '9' {
		return c - '0'
	}
	if c <= 'F' {
		return c - 'A' + 10
	}
	return c - 'a' + 10
}

func (in *input) encoded() byte {
	c := in.next()
	for c != 0 && c <= ' ' {
		c = in.next()
	}
	return hexValue(c)*hexRadix + hexValue(in.next())
}

type output struct {
	bytes [bufferSize]byte
	used  int
}

func (out *output) flush() {
	pending := out.bytes[:out.used]
	for len(pending) > 0 {
		count, err := os.Stdout.Write(pending)
		pending = pending[count:]
		if err != nil || count == 0 {
			break
		}
	}
	out.used = 0
}

func (out *output) key(value byte) {
	if out.used+2 >= bufferSize {
		out.flush()
	}
	out.bytes[out.used] = digits[value/hexRadix]
	out.bytes[out.used+1] = digits[value%hexRadix]
	out.used += 2
}

func main() {
	var in input
	var shorter [maxLength]byte
	length, c := 0, in.next()
	for c != 0 && c <= ' ' {
		c = in.next()
	}
	for c > ' ' {
		high, low := hexValue(c), hexValue(in.next())
		shorter[length] = high*hexRadix + low
		length++
		c = in.next()
	}
	var out output
	previous := in.encoded() ^ ' '
	out.key(previous)
	for i := 0; i < length; i++ {
		// The same plaintext byte cancels; only the preceding key byte is needed.
		previous ^= shorter[i] ^ in.encoded()
		out.key(previous)
	}
	out.bytes[out.used] = '\n'
	out.used++
	out.flush()
}
