package main

import "os"

const (
	limbBits   = 30
	limbBase   = uint64(1) << limbBits
	limbMask   = limbBase - 1
	maxSquares = 50
	inputSize  = 4096
	indexBytes = 3
	pointDen   = 4
	squareDen  = 8
)

type integer struct {
	digits   []uint32
	negative bool
}

func (value *integer) resize(length int) {
	if cap(value.digits) < length {
		value.digits = make([]uint32, length)
	} else {
		value.digits = value.digits[:length]
	}
}

func (value *integer) normalize() {
	for len(value.digits) > 0 && value.digits[len(value.digits)-1] == 0 {
		value.digits = value.digits[:len(value.digits)-1]
	}
	if len(value.digits) == 0 {
		value.negative = false
	}
}

func (value integer) magnitude(other integer) int {
	if len(value.digits) < len(other.digits) {
		return -1
	}
	if len(value.digits) > len(other.digits) {
		return 1
	}
	for i := len(value.digits) - 1; i >= 0; i-- {
		if value.digits[i] < other.digits[i] {
			return -1
		}
		if value.digits[i] > other.digits[i] {
			return 1
		}
	}
	return 0
}

func (value *integer) setSmall(number int64) {
	value.negative = number < 0
	if number < 0 {
		number = -number
	}
	value.digits = value.digits[:0]
	for magnitude := uint64(number); magnitude != 0; magnitude >>= limbBits {
		value.digits = append(value.digits, uint32(magnitude&limbMask))
	}
	value.normalize()
}

func (value *integer) set(source integer) {
	value.resize(len(source.digits))
	copy(value.digits, source.digits)
	value.negative = source.negative
}

func (value *integer) multiplySmall(source integer, multiplier int64) {
	negative := source.negative != (multiplier < 0)
	if multiplier < 0 {
		multiplier = -multiplier
	}
	length := len(source.digits)
	value.resize(length + 2)
	var carry uint64
	for i := 0; i < length; i++ {
		current := uint64(source.digits[i])*uint64(multiplier) + carry
		value.digits[i] = uint32(current & limbMask)
		carry = current >> limbBits
	}
	for carry != 0 {
		value.digits[length] = uint32(carry & limbMask)
		length++
		carry >>= limbBits
	}
	value.digits = value.digits[:length]
	value.negative = negative
	value.normalize()
}

func (value *integer) add(a, b integer) {
	if a.negative == b.negative {
		length := len(a.digits)
		if len(b.digits) > length {
			length = len(b.digits)
		}
		value.resize(length + 1)
		var carry uint64
		for i := 0; i < length; i++ {
			current := carry
			if i < len(a.digits) {
				current += uint64(a.digits[i])
			}
			if i < len(b.digits) {
				current += uint64(b.digits[i])
			}
			value.digits[i] = uint32(current & limbMask)
			carry = current >> limbBits
		}
		value.digits[length] = uint32(carry)
		value.negative = a.negative
	} else {
		if a.magnitude(b) < 0 {
			a, b = b, a
		}
		value.resize(len(a.digits))
		var borrow int64
		for i := range a.digits {
			current := int64(a.digits[i]) - borrow
			if i < len(b.digits) {
				current -= int64(b.digits[i])
			}
			borrow = 0
			if current < 0 {
				current += int64(limbBase)
				borrow = 1
			}
			value.digits[i] = uint32(current)
		}
		value.negative = a.negative
	}
	value.normalize()
}

func (value *integer) subtract(a, b integer) {
	if len(b.digits) > 0 {
		b.negative = !b.negative
	}
	value.add(a, b)
}

func (value *integer) square(source integer) {
	length := len(source.digits)
	value.resize(2 * length)
	for i := range value.digits {
		value.digits[i] = 0
	}
	// Each product and carry fit in uint64 because the limbs contain only 30 bits.
	for i, a := range source.digits {
		var carry uint64
		for j, b := range source.digits {
			current := uint64(a)*uint64(b) + uint64(value.digits[i+j]) + carry
			value.digits[i+j] = uint32(current & limbMask)
			carry = current >> limbBits
		}
		value.digits[i+length] = uint32(carry)
	}
	value.negative = false
	value.normalize()
}

type square struct{ x1, y1, x2, y2 int64 }
type fraction struct {
	numerator   integer
	denominator int64
}

var (
	input                   [inputSize]byte
	inputPosition           int
	inputLength             int
	squares                 [maxSquares]square
	distances               [maxSquares]fraction
	order, scratch          [maxSquares]int
	px, py, qx, qy          integer
	a, b, term, coefficient integer
	leftValue, rightValue   integer
	output                  [maxSquares * indexBytes]byte
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

func firstByte() byte {
	c := nextByte()
	for c != 0 && c <= ' ' {
		c = nextByte()
	}
	return c
}

func nextSmall() int64 {
	c := firstByte()
	sign := int64(1)
	if c == '-' || c == '+' {
		if c == '-' {
			sign = -1
		}
		c = nextByte()
	}
	var value int64
	for c >= '0' && c <= '9' {
		value = 10*value + int64(c-'0')
		c = nextByte()
	}
	return sign * value
}

func (value *integer) read() {
	c := firstByte()
	negative := c == '-'
	if c == '-' || c == '+' {
		c = nextByte()
	}
	value.digits = value.digits[:0]
	for c >= '0' && c <= '9' {
		carry := uint64(c - '0')
		for i, digit := range value.digits {
			current := 10*uint64(digit) + carry
			value.digits[i] = uint32(current & limbMask)
			carry = current >> limbBits
		}
		if carry != 0 {
			value.digits = append(value.digits, uint32(carry))
		}
		c = nextByte()
	}
	value.negative = negative
	value.normalize()
}

func projection(destination *integer, x, y, limit int64) {
	destination.multiplySmall(qx, x)
	term.multiplySmall(qy, y)
	destination.add(*destination, term)
	destination.negative = false
	coefficient.setSmall(limit)
	destination.subtract(*destination, coefficient)
	if destination.negative {
		destination.digits = destination.digits[:0]
		destination.negative = false
	}
}

func before(i, j int) bool {
	x, y := &distances[i], &distances[j]
	leftValue.multiplySmall(x.numerator, y.denominator)
	rightValue.multiplySmall(y.numerator, x.denominator)
	comparison := leftValue.magnitude(rightValue)
	return comparison < 0 || (comparison == 0 && i < j)
}

func main() {
	n := int(nextSmall())
	for i := 0; i < n; i++ {
		squares[i] = square{nextSmall(), nextSmall(), nextSmall(), nextSmall()}
	}
	px.read()
	py.read()
	px.multiplySmall(px, 2)
	py.multiplySmall(py, 2)
	for i := 0; i < n; i++ {
		s := squares[i]
		coefficient.setSmall(s.x1 + s.x2)
		qx.subtract(px, coefficient)
		coefficient.setSmall(s.y1 + s.y2)
		qy.subtract(py, coefficient)
		dx, dy := s.x2-s.x1, s.y2-s.y1
		h := dx*dx + dy*dy
		d := &distances[i]
		if h == 0 {
			a.set(qx)
			b.set(qy)
			d.denominator = pointDen
		} else {
			projection(&a, dx-dy, dy+dx, h)
			projection(&b, dx+dy, dy-dx, h)
			d.denominator = squareDen * h
		}
		d.numerator.square(a)
		term.square(b)
		d.numerator.add(d.numerator, term)
		order[i] = i
	}
	// Merge indices so the comparison buffers can be reused without reflection or closures.
	for width := 1; width < n; width *= 2 {
		for start := 0; start < n; start += 2 * width {
			middle, end := start+width, start+2*width
			if middle > n {
				middle = n
			}
			if end > n {
				end = n
			}
			left, right := start, middle
			for index := start; index < end; index++ {
				if left < middle && (right == end || before(order[left], order[right])) {
					scratch[index] = order[left]
					left++
				} else {
					scratch[index] = order[right]
					right++
				}
			}
		}
		copy(order[:n], scratch[:n])
	}
	length := 0
	for i, index := range order[:n] {
		if i != 0 {
			output[length] = ' '
			length++
		}
		value := index + 1
		if value >= 10 {
			output[length] = '0' + byte(value/10)
			length++
		}
		output[length] = '0' + byte(value%10)
		length++
	}
	output[length] = '\n'
	os.Stdout.Write(output[:length+1])
}
