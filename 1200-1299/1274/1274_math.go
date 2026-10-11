package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

// parse reads "-7 3/4", "-7/11" or "11" as a numerator and denominator
func parse(line string) (int64, int64) {
	line = strings.TrimSpace(line)
	sign := int64(1)
	if strings.HasPrefix(line, "-") {
		sign = -1
	}
	var whole, num, den int64 = 0, 0, 1
	for _, token := range strings.Fields(strings.TrimLeft(line, "-")) {
		if slash := strings.IndexByte(token, '/'); slash >= 0 {
			n, _ := strconv.Atoi(token[:slash])
			d, _ := strconv.Atoi(token[slash+1:])
			num, den = int64(n), int64(d)
		} else {
			w, _ := strconv.Atoi(token)
			whole = int64(w)
		}
	}
	return sign * (whole*den + num), den
}

func gcd(a, b int64) int64 {
	for b != 0 {
		a, b = b, a%b
	}
	return a
}

func show(num, den int64) string {
	if den < 0 {
		num, den = -num, -den
	}
	sign := ""
	if num < 0 {
		sign, num = "-", -num
	}
	g := gcd(num, den)
	num, den = num/g, den/g
	whole, rest := num/den, num%den
	switch {
	case rest == 0:
		return fmt.Sprintf("%s%d", sign, whole)
	case whole == 0:
		return fmt.Sprintf("%s%d/%d", sign, rest, den)
	}
	return fmt.Sprintf("%s%d %d/%d", sign, whole, rest, den)
}

func main() {
	in := bufio.NewReader(os.Stdin)
	first, _ := in.ReadString('\n')
	op, _ := in.ReadString('\n')
	second, _ := in.ReadString('\n')
	an, ad := parse(first)
	bn, bd := parse(second)
	var num, den int64
	switch strings.TrimSpace(op) {
	case "+":
		num, den = an*bd+bn*ad, ad*bd
	case "-":
		num, den = an*bd-bn*ad, ad*bd
	case "*":
		num, den = an*bn, ad*bd
	default:
		num, den = an*bd, ad*bn
	}
	fmt.Println(show(num, den))
}
