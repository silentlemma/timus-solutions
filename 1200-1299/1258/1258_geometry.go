package main

import (
	"bufio"
	"fmt"
	"math"
	"os"
	"strings"
)

// unfolded is the distance along one axis once the room is mirrored at each hit
func unfolded(start, end, size int, low byte, hits string) int {
	if hits == "" {
		if end > start {
			return end - start
		}
		return start - end
	}
	first, last := size-start, size-end
	if hits[0] == low {
		first = start
	}
	if hits[len(hits)-1] == low {
		last = end
	}
	return first + (len(hits)-1)*size + last
}

func main() {
	in := bufio.NewReader(os.Stdin)
	var w, d, x0, y0, x1, y1 int
	fmt.Fscan(in, &w, &d, &x0, &y0, &x1, &y1)
	var side, ends strings.Builder
	for {
		c, err := in.ReadByte()
		if err != nil {
			break
		}
		switch c {
		case 'L', 'R':
			side.WriteByte(c)
		case 'F', 'B':
			ends.WriteByte(c)
		}
	}
	dx := unfolded(x0, x1, w, 'L', side.String())
	dy := unfolded(y0, y1, d, 'F', ends.String())
	fmt.Printf("%.4f\n", math.Sqrt(float64(dx*dx+dy*dy)))
}
