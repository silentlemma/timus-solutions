package main

import (
	"math"
	"os"
	"strconv"
)

const (
	gravity     = 9.81
	centimetres = 100
	seconds     = 60
	steps       = 100
	turn        = 4
)

func main() {
	length, _ := strconv.ParseFloat(token(), 64)
	height, _ := strconv.ParseFloat(token(), 64)
	turns, _ := strconv.ParseFloat(token(), 64)
	if butterSide(length, height, turns) {
		writeBytes([]byte("butter\n"))
	} else {
		writeBytes([]byte("bread\n"))
	}
}

func butterSide(length, height, turns float64) bool {
	half := length / centimetres / 2
	top := height / centimetres
	omega := turns * 2 * math.Pi / seconds
	quarter := math.Pi / 2 / omega
	// the height of the lowest end of the toast at time t
	gap := func(t float64) float64 {
		return top - gravity*t*t/2 - half*math.Abs(math.Sin(omega*t))
	}
	// d gap / dt in quarter k, where the angle within the half turn is
	// omega*t - (k / 2)*pi
	slope := func(t float64, k int) float64 {
		return -gravity*t - half*omega*math.Cos(omega*t-float64(k/2)*math.Pi)
	}
	// d slope / dt, falling through an odd quarter
	// Solve bend=0 once: in every odd quarter the slope peaks at b-asin(ratio)/omega.
	ratio := gravity / (half * omega * omega)
	hasPeak := ratio < 1
	peakOffset := 0.0
	if hasPeak {
		peakOffset = math.Asin(ratio) / omega
	}
	k := 0
	for {
		a, b := float64(k)*quarter, float64(k+1)*quarter
		lowest := gap(b)
		if k%2 == 1 && hasPeak {
			// the end rises again here: the slope of the gap is concave, so
			// find its peak; where it turns positive, the gap has a minimum
			lo := b - peakOffset
			if lo < a {
				lo = a
			}
			if lo > b {
				lo = b
			}
			if slope(lo, k) > 0 {
				lo, hi := a, lo
				for i := 0; i < steps; i++ {
					mid := (lo + hi) / 2
					if slope(mid, k) < 0 {
						lo = mid
					} else {
						hi = mid
					}
				}
				lowest = math.Min(lowest, gap(lo))
			}
		}
		if lowest <= 0 {
			break
		}
		k++
	}
	// in quarters 0 and 3 of a turn the butter faces down
	inTurn := k % turn
	return inTurn == 0 || inTurn == turn-1
}

// Read the single input stream once and convert tokens without fmt reflection.

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
