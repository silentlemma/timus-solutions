package main

import (
	"syscall"
)

const rawInputSize = 256
const rawOutputSize = 128
const decimalSize = 32
const radix = 10

var rawInput [rawInputSize]byte
var rawPosition, rawLength int
var rawOutput [rawOutputSize]byte
var rawUsed int

func byteIn() byte {
	if rawPosition == rawLength {
		// Global arrays stay live and never move across the raw system call.
		n, failure := syscall.Read(syscall.Stdin, rawInput[:])
		if failure != nil || n == 0 {
			return 0
		}
		rawPosition, rawLength = 0, int(n)
	}
	ch := rawInput[rawPosition]
	rawPosition++
	return ch
}
func nextInt() int {
	ch := byteIn()
	for ch != 0 && ch <= ' ' {
		ch = byteIn()
	}
	value := 0
	for ch >= '0' && ch <= '9' {
		value = value*radix + int(ch-'0')
		ch = byteIn()
	}
	return value
}
func flush() {
	at := 0
	for at < rawUsed {
		n, failure := syscall.Write(syscall.Stdout, rawOutput[at:rawUsed])
		if failure != nil || n == 0 {
			break
		}
		at += int(n)
	}
	rawUsed = 0
}
func byteOut(ch byte) {
	if rawUsed == len(rawOutput) {
		flush()
	}
	rawOutput[rawUsed] = ch
	rawUsed++
}
func numberOut(value int64) {
	var digits [decimalSize]byte
	at := len(digits)
	for {
		at--
		digits[at] = byte(value%radix) + '0'
		value /= radix
		if value == 0 {
			break
		}
	}
	for ; at < len(digits); at++ {
		byteOut(digits[at])
	}
}

const textLimit = 128
const roles = 3
const clauses = 2

var sentence [textLimit]byte
var spans [clauses][roles][2]int
var conjunction [clauses][2]int
var firstLetter = true

func emitSpan(start, end int) {
	for i := start; i < end; i++ {
		ch := sentence[i]
		if firstLetter {
			ch = ch - 'a' + 'A'
			firstLetter = false
		}
		byteOut(ch)
	}
}
func main() {
	length := 0
	for ch := byteIn(); ch != 0 && ch != '\n'; ch = byteIn() {
		if ch >= 'A' && ch <= 'Z' {
			ch = ch - 'A' + 'a'
		}
		sentence[length] = ch
		length++
	}
	clause := 0
	for i := 0; i < length; {
		ch := sentence[i]
		if ch <= ' ' {
			i++
			continue
		}
		if ch == ',' {
			clause++
			i++
			continue
		}
		role := -1
		close := byte(0)
		if ch == '{' {
			role = 0
			close = '}'
		} else if ch == '(' {
			role = 1
			close = ')'
		} else if ch == '[' {
			role = 2
			close = ']'
		}
		if role >= 0 {
			i++
			start := i
			for sentence[i] != close {
				i++
			}
			spans[clause][role] = [2]int{start, i}
			i++
		} else {
			start := i
			for i < length && sentence[i] >= 'a' && sentence[i] <= 'z' {
				i++
			}
			conjunction[clause] = [2]int{start, i}
		}
	}
	for part := 0; part <= clause; part++ {
		if part > 0 {
			byteOut(',')
			byteOut(' ')
		}
		separated := false
		if span := conjunction[part]; span[1] > span[0] {
			emitSpan(span[0], span[1])
			separated = true
		}
		for role := 0; role < roles; role++ {
			if separated {
				byteOut(' ')
			}
			span := spans[part][role]
			emitSpan(span[0], span[1])
			separated = true
		}
	}
	byteOut('\n')
	flush()
}
