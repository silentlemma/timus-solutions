package main

import (
	"bufio"
	"fmt"
	"math/bits"
	"os"
	"strconv"
	"strings"
)

// the places a stick can take in one cell of the picture
const (
	top = 1 << iota
	middle
	bottom
	upperLeft
	upperRight
	lowerLeft
	lowerRight
	upperSlash
	lowerSlash
	plusUpright
	equalUpper
	equalLower
)

const (
	sides      = upperLeft | upperRight | lowerLeft | lowerRight
	plusShape  = middle | plusUpright // the bar lies where a middle stick does
	equalShape = equalUpper | equalLower
	longest    = 8 // digits in a number
	base       = 10
	none       = -1
)

var digitShape = [base]uint{
	top | sides | bottom,
	upperSlash | upperRight | lowerRight,
	top | upperRight | lowerSlash | bottom,
	top | upperSlash | middle | lowerSlash,
	upperLeft | upperRight | middle | lowerRight,
	top | upperLeft | middle | lowerRight | bottom,
	upperSlash | middle | lowerLeft | lowerRight | bottom,
	top | upperSlash | lowerLeft,
	top | sides | middle | bottom,
	top | upperLeft | upperRight | middle | lowerSlash,
}

func shapeOf(c byte) uint {
	switch c {
	case '+':
		return plusShape
	case '=':
		return equalShape
	}
	return digitShape[c-'0']
}

func sticks(shape uint) int { return bits.OnesCount(shape) }

type step struct {
	kept                         int // sticks kept in place so far, none if unreachable
	dx, dy, dz, carry, usedSoFar int
}

func solve(text string, k int) string {
	n := len(text)
	cells := make([]uint, n)
	total := 0
	for i := range cells {
		cells[i] = shapeOf(text[i])
		total += sticks(cells[i])
	}
	kept := func(pos int, shape uint) int { return sticks(cells[pos] & shape) }
	for lenX := 1; lenX <= longest; lenX++ {
		for lenY := 1; lenY <= longest; lenY++ {
			lenZ := n - 2 - lenX - lenY
			// no leading zeros, so z has at least as many digits as x and y
			if lenZ < lenX || lenZ < lenY || lenZ > longest {
				continue
			}
			plus, equal := lenX, lenX+lenY+1
			// table[col][carry][used]: the best way to fill col columns from the right
			table := make([][2][]step, lenZ+1)
			for col := range table {
				for carry := range table[col] {
					table[col][carry] = make([]step, total+1)
					for used := range table[col][carry] {
						table[col][carry][used].kept = none
					}
				}
			}
			signs := sticks(plusShape) + sticks(equalShape)
			table[0][0][signs].kept = kept(plus, plusShape) + kept(equal, equalShape)
			for col := 0; col < lenZ; col++ {
				posX, posY, posZ := none, none, n-1-col
				if col < lenX {
					posX = lenX - 1 - col
				}
				if col < lenY {
					posY = lenX + lenY - col
				}
				for carry := 0; carry < 2; carry++ {
					for used := 0; used <= total; used++ {
						have := table[col][carry][used].kept
						if have == none {
							continue
						}
						for dx := 0; dx < base; dx++ {
							if posX == none && dx > 0 || posX != none && dx == 0 && col == lenX-1 && lenX > 1 {
								continue
							}
							for dy := 0; dy < base; dy++ {
								if posY == none && dy > 0 || posY != none && dy == 0 && col == lenY-1 && lenY > 1 {
									continue
								}
								dz, out := (dx+dy+carry)%base, (dx+dy+carry)/base
								if dz == 0 && col == lenZ-1 && lenZ > 1 {
									continue
								}
								more, gain := sticks(digitShape[dz]), kept(posZ, digitShape[dz])
								if posX != none {
									more += sticks(digitShape[dx])
									gain += kept(posX, digitShape[dx])
								}
								if posY != none {
									more += sticks(digitShape[dy])
									gain += kept(posY, digitShape[dy])
								}
								if used+more > total {
									continue
								}
								next := &table[col+1][out][used+more]
								if next.kept < have+gain {
									*next = step{have + gain, dx, dy, dz, carry, used}
								}
							}
						}
					}
				}
			}
			// every stick must be used, and the moved ones are those not kept
			last := table[lenZ][0][total]
			if last.kept == none || total-last.kept > k {
				continue
			}
			x, y, z := make([]byte, lenX), make([]byte, lenY), make([]byte, lenZ)
			carry, used := 0, total
			for col := lenZ; col > 0; col-- {
				s := table[col][carry][used]
				c := col - 1
				if c < lenX {
					x[lenX-1-c] = byte('0' + s.dx)
				}
				if c < lenY {
					y[lenY-1-c] = byte('0' + s.dy)
				}
				z[lenZ-1-c] = byte('0' + s.dz)
				carry, used = s.carry, s.usedSoFar
			}
			return string(x) + "+" + string(y) + "=" + string(z)
		}
	}
	return "Impossible"
}

func main() {
	// the expression may be written with spaces, K comes last
	var tokens []string
	in := bufio.NewScanner(os.Stdin)
	in.Split(bufio.ScanWords)
	for in.Scan() {
		tokens = append(tokens, in.Text())
	}
	k, _ := strconv.Atoi(tokens[len(tokens)-1])
	fmt.Println(solve(strings.Join(tokens[:len(tokens)-1], ""), k))
}
