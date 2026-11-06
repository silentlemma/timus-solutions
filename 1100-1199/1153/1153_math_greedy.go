package main

import "os"

const (
	maxAnswerDigits = 300
	capacity        = 2*maxAnswerDigits + 2
	inputSize       = 1024
	base            = 10
	pairBase        = base * base
	rootScale       = 2 * base
	discriminantMul = 8
)

type decimal struct {
	digits [capacity]uint16
	length int
}

var (
	input              [inputSize]byte
	inputPosition      int
	inputLength        int
	discriminant, root decimal
	remainder, trial   decimal
	output             [maxAnswerDigits + 2]byte
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

func (value *decimal) trim() {
	for value.length > 0 && value.digits[value.length-1] == 0 {
		value.length--
	}
}

func (value *decimal) scaledAdd(source *decimal, multiplier, add int) {
	length := source.length
	value.length = length
	carry := add
	for i := 0; i < length; i++ {
		current := int(source.digits[i])*multiplier + carry
		value.digits[i] = uint16(current % base)
		carry = current / base
	}
	for carry != 0 {
		value.digits[value.length] = uint16(carry % base)
		value.length++
		carry /= base
	}
	value.trim()
}

func (value *decimal) compare(other *decimal) int {
	if value.length < other.length {
		return -1
	}
	if value.length > other.length {
		return 1
	}
	for i := value.length - 1; i >= 0; i-- {
		if value.digits[i] < other.digits[i] {
			return -1
		}
		if value.digits[i] > other.digits[i] {
			return 1
		}
	}
	return 0
}

func (value *decimal) subtract(other *decimal) {
	borrow := 0
	for i := 0; i < value.length; i++ {
		current := int(value.digits[i]) - borrow
		if i < other.length {
			current -= int(other.digits[i])
		}
		borrow = 0
		if current < 0 {
			current += base
			borrow = 1
		}
		value.digits[i] = uint16(current)
	}
	value.trim()
}

func main() {
	c := nextByte()
	for c != 0 && c <= ' ' {
		c = nextByte()
	}
	for c >= '0' && c <= '9' {
		discriminant.digits[discriminant.length] = uint16(c - '0')
		discriminant.length++
		c = nextByte()
	}
	for left, right := 0, discriminant.length-1; left < right; left, right = left+1, right-1 {
		discriminant.digits[left], discriminant.digits[right] =
			discriminant.digits[right], discriminant.digits[left]
	}
	discriminant.trim()
	discriminant.scaledAdd(&discriminant, discriminantMul, 1)
	for group := (discriminant.length+1)/2 - 1; group >= 0; group-- {
		position := 2 * group
		pair := int(discriminant.digits[position])
		if position+1 < discriminant.length {
			pair += base * int(discriminant.digits[position+1])
		}
		remainder.scaledAdd(&remainder, pairBase, pair)
		// Appending digit x to the root consumes (20*root + x)*x of the remainder.
		digit := base - 1
		for digit > 0 {
			trial.scaledAdd(&root, rootScale*digit, digit*digit)
			if trial.compare(&remainder) <= 0 {
				remainder.subtract(&trial)
				break
			}
			digit--
		}
		root.scaledAdd(&root, base, digit)
	}
	// The exact root is 2*N + 1; subtract one, then halve from the highest digit.
	for i := 0; ; i++ {
		if root.digits[i] != 0 {
			root.digits[i]--
			break
		}
		root.digits[i] = base - 1
	}
	carry := 0
	for i := root.length - 1; i >= 0; i-- {
		current := carry*base + int(root.digits[i])
		root.digits[i] = uint16(current / 2)
		carry = current % 2
	}
	root.trim()
	for i := 0; i < root.length; i++ {
		output[i] = '0' + byte(root.digits[root.length-1-i])
	}
	output[root.length] = '\n'
	os.Stdout.Write(output[:root.length+1])
}
