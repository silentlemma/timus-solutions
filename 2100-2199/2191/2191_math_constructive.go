package main

import (
	"bufio"
	"os"
	"strconv"
)

const digits = 18

// number appends a nonnegative fraction with at most digits decimals, truncated.
func number(out []byte, numerator, denominator int64) []byte {
	out = strconv.AppendInt(out, numerator/denominator, 10)
	rest := numerator % denominator
	if rest == 0 {
		return out
	}
	out = append(out, '.')
	for i := 0; i < digits; i++ {
		rest *= 10
		out = append(out, byte('0'+rest/denominator))
		rest %= denominator
	}
	for out[len(out)-1] == '0' {
		out = out[:len(out)-1]
	}
	if out[len(out)-1] == '.' {
		out = out[:len(out)-1]
	}
	return out
}

func main() {
	scanner := bufio.NewScanner(os.Stdin)
	scanner.Split(bufio.ScanWords)
	next := func() int64 {
		scanner.Scan()
		v, _ := strconv.Atoi(scanner.Text())
		return int64(v)
	}
	n := int(next())
	xs := make([]int64, n)
	ys := make([]int64, n)
	for i := 0; i < n; i++ {
		xs[i], ys[i] = next(), next()
	}
	var out []byte

	// term writes c |x - root| with c = numerator / denominator.
	term := func(numerator, denominator, root int64, constant bool) {
		if numerator < 0 {
			out = append(out, '-')
			numerator = -numerator
		} else if len(out) > 0 {
			out = append(out, '+')
		}
		out = append(out, '|')
		if constant {
			out = append(out, "0x+"...)
			out = number(out, numerator, denominator)
		} else {
			shift := numerator * root
			out = number(out, numerator, denominator)
			if shift >= 0 {
				out = append(out, "x-"...)
			} else {
				out = append(out, "x+"...)
				shift = -shift
			}
			out = number(out, shift, denominator)
		}
		out = append(out, '|')
	}

	// A kink at x_i where the slope turns from s to t is (t - s) / 2 |x - x_i|.
	for i := 1; i+1 < n; i++ {
		leftDx, leftDy := xs[i]-xs[i-1], ys[i]-ys[i-1]
		rightDx, rightDy := xs[i+1]-xs[i], ys[i+1]-ys[i]
		term(rightDy*leftDx-leftDy*rightDx, 2*leftDx*rightDx, xs[i], false)
	}

	firstDx, firstDy := xs[1]-xs[0], ys[1]-ys[0]
	lastDx, lastDy := xs[n-1]-xs[n-2], ys[n-1]-ys[n-2]
	// On [x_1, x_N] the kinks add (t - s) / 2 times x - x_i; the term at x_1
	// restores the first slope and a constant fixes the value at x_1.
	term(firstDy*lastDx+lastDy*firstDx, 2*firstDx*lastDx, xs[0], false)
	span := xs[n-2] - xs[0]
	term(2*ys[0]*lastDx-lastDy*span+(ys[n-2]-ys[0])*lastDx, 2*lastDx, 0, true)
	out = append(out, '\n')
	os.Stdout.Write(out)
}
