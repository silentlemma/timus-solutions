package main

import (
	"bufio"
	"fmt"
	"os"
)

const modulus int64 = 40961

func power(base, exponent int64) int64 {
	result := int64(1)
	for exponent > 0 {
		if exponent&1 != 0 {
			result = result * base % modulus
		}
		base = base * base % modulus
		exponent /= 2
	}
	return result
}

func main() {
	reader := bufio.NewReader(os.Stdin)
	var text string
	fmt.Fscan(reader, &text)
	n := len(text)
	row := make([]int64, n)
	ones := int64(0)
	for i := range text {
		row[i] = int64(text[i] - '0')
		ones += row[i]
	}

	factorial := int64(1)
	for i := 1; i <= n; i++ {
		factorial = factorial * int64(i) % modulus
	}
	inverseFactorial := make([]int64, n+1)
	inverseFactorial[n] = power(factorial, modulus-2)
	for i := n; i > 0; i-- {
		inverseFactorial[i-1] = inverseFactorial[i] * int64(i) % modulus
	}

	answer := make([]int64, n+1)
	total := int64(1)
	onesTotal := ones
	for k := n - 1; k > 0; k-- {
		squares := int64(0)
		// Scaling each row by (n-k)! removes division from the recurrence.
		for i := 0; i < k; i++ {
			value := (int64(k-i)*row[i] + int64(i+1)*row[i+1]) % modulus
			row[i] = value
			squares += value * value
		}
		total = total * int64(k+1) % modulus
		onesTotal = onesTotal * int64(k) % modulus
		difference := (total*onesTotal - squares%modulus + modulus) % modulus
		inverse := inverseFactorial[n-k]
		answer[k] = difference * inverse % modulus * inverse % modulus
	}

	writer := bufio.NewWriter(os.Stdout)
	for k := 1; k <= n; k++ {
		if k > 1 {
			fmt.Fprint(writer, " ")
		}
		fmt.Fprint(writer, answer[k])
	}
	fmt.Fprintln(writer)
	writer.Flush()
}
