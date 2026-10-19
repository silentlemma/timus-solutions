package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

const decimalPlaces = 12

func probability(numerator, denominator int64) string {
	fraction, remainder, scale := int64(0), numerator, int64(1)
	for digit := 0; digit < decimalPlaces; digit++ {
		remainder *= 10
		fraction = fraction*10 + remainder/denominator
		remainder %= denominator
		scale *= 10
	}
	if 2*remainder >= denominator {
		fraction++
	}
	integer := strconv.FormatInt(fraction/scale, 10)
	fraction %= scale
	if fraction == 0 {
		return integer
	}
	digits := strconv.FormatInt(fraction, 10)
	digits = strings.Repeat("0", decimalPlaces-len(digits)) + digits
	return integer + "." + strings.TrimRight(digits, "0")
}

func main() {
	in := bufio.NewReader(os.Stdin)
	var speed, distance, widthEngels, widthMarx int64
	var greenEngels, yellowEngels, greenMarx, yellowMarx int64
	fmt.Fscan(in, &speed, &distance, &widthEngels, &widthMarx)
	fmt.Fscan(in, &greenEngels, &yellowEngels, &greenMarx, &yellowMarx)
	period := greenEngels + yellowEngels + greenMarx + yellowMarx
	denominator := speed * period
	// Only the phase lengths and the time to cross Marx affect the comparison.
	crosswalk := speed*(greenEngels+yellowMarx) - widthMarx
	fmt.Println(probability(crosswalk, denominator), probability(widthMarx, denominator))
}
