package main

import (
	"math/big"
	"os"
	"strings"
)

const decimalScale int64 = 100

type exchange struct {
	from, to  int
	rate, fee int64
}

func scaled(text string, places int) *big.Int {
	parts := strings.SplitN(text, ".", 2)
	fraction := ""
	if len(parts) == 2 {
		fraction = parts[1]
	}
	value, _ := new(big.Int).SetString(parts[0]+fraction+strings.Repeat("0", places-len(fraction)), 10)
	return value
}

func main() {
	n, m, s := integer(), integer(), integer()
	text := token()
	places := 2
	if dot := strings.IndexByte(text, '.'); dot >= 0 && len(text)-dot-1 > places {
		places = len(text) - dot - 1
	}
	v := scaled(text, places)
	unit := scaled("1", places-2)
	hundred := big.NewInt(decimalScale)
	var edges []exchange
	for k := 0; k < m; k++ {
		a, b := integer(), integer()
		rab, cab := hundredths(token()), hundredths(token())
		rba, cba := hundredths(token()), hundredths(token())
		edges = append(edges, exchange{a, b, rab, cab},
			exchange{b, a, rba, cba})
	}
	// All amounts share an exact denominator, multiplied by 100 each pass.
	// A change on pass n means a reachable gaining cycle.
	// Reuse two independent amount buffers and scratch integers across passes.
	best, after := make([]big.Int, n+1), make([]big.Int, n+1)
	present, nextPresent := make([]bool, n+1), make([]bool, n+1)
	best[s].Set(v)
	present[s] = true
	var fee, rate, cost, got big.Int
	changed := false
	for pass := 0; pass < n; pass++ {
		for currency := range best {
			nextPresent[currency] = present[currency]
			if present[currency] {
				after[currency].Mul(&best[currency], hundred)
			}
		}
		changed = false
		for _, e := range edges {
			if !present[e.from] {
				continue
			}
			fee.SetInt64(e.fee)
			cost.Mul(unit, &fee)
			if best[e.from].Cmp(&cost) >= 0 {
				got.Sub(&best[e.from], &cost)
				rate.SetInt64(e.rate)
				got.Mul(&got, &rate)
				if !nextPresent[e.to] || got.Cmp(&after[e.to]) > 0 {
					after[e.to].Set(&got)
					nextPresent[e.to] = true
					changed = true
				}
			}
		}
		best, after = after, best
		present, nextPresent = nextPresent, present
		unit.Mul(unit, hundred)
		v.Mul(v, hundred)
		if best[s].Cmp(v) > 0 || !changed {
			break
		}
	}
	if best[s].Cmp(v) > 0 || changed {
		writeBytes([]byte("YES\n"))
	} else {
		writeBytes([]byte("NO\n"))
	}
}
func hundredths(text string) int64 {
	negative := text[0] == '-'
	if negative || text[0] == '+' {
		text = text[1:]
	}
	value, places := int64(0), -1
	for _, ch := range text {
		if ch == '.' {
			places = 0
			continue
		}
		value = value*10 + int64(ch-'0')
		if places >= 0 {
			places++
		}
	}
	if places < 0 {
		places = 0
	}
	for places < 2 {
		value *= 10
		places++
	}
	if negative {
		return -value
	}
	return value
}

const inputBufferBytes = 256

var inputBuffer [inputBufferBytes]byte
var inputPosition, inputLength int

// Keep only a bounded refill buffer and the current token; Read may return partial data.
// Refill a fixed byte buffer; EOF is separate from every possible input byte.
func nextByte() int {
	if inputPosition == inputLength {
		inputLength, _ = os.Stdin.Read(inputBuffer[:])
		inputPosition = 0
		if inputLength == 0 {
			return -1
		}
	}
	ch := inputBuffer[inputPosition]
	inputPosition++
	return int(ch)
}

// Read the single input stream once and convert tokens without fmt reflection.
// Parse decimal input directly to avoid fmt's reflection and token allocations.
func integer() int {
	position, length := inputPosition, inputLength
	for {
		for position < length && inputBuffer[position] <= ' ' {
			position++
		}
		if position < length {
			break
		}
		length, _ = os.Stdin.Read(inputBuffer[:])
		position = 0
		if length == 0 {
			inputPosition, inputLength = 0, 0
			return 0
		}
	}
	negative := inputBuffer[position] == '-'
	if negative || inputBuffer[position] == '+' {
		position++
	}
	value := 0
	for {
		// Keep the cursor local until the number ends or the current block is exhausted.
		for position < length {
			ch := inputBuffer[position]
			if ch < '0' || ch > '9' {
				inputPosition, inputLength = position, length
				if negative {
					return value
				}
				return -value
			}
			value = value*10 - int(ch-'0')
			position++
		}
		length, _ = os.Stdin.Read(inputBuffer[:])
		position = 0
		if length == 0 {
			inputPosition, inputLength = 0, 0
			if negative {
				return value
			}
			return -value
		}
	}
}

func token() string {
	ch := nextByte()
	for ch >= 0 && ch <= ' ' {
		ch = nextByte()
	}
	var bytes []byte
	for ch > ' ' {
		bytes = append(bytes, byte(ch))
		ch = nextByte()
	}
	return string(bytes)
}

// Reuse one output buffer; io.Writer cannot retain it after Write returns.
func writeBytes(data []byte) {
	for len(data) > 0 {
		count, err := os.Stdout.Write(data)
		if count > 0 {
			data = data[count:]
		}
		if err != nil || count == 0 {
			return
		}
	}
}
