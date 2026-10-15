package main

import "fmt"

// everyone on the far side of Vasya can be made to trip except the two
// seats at the far end, who always come in from their own end
const safe = 2

func main() {
	var n, k int
	fmt.Scan(&n, &k)
	far := k - 1
	if n-k > far {
		far = n - k
	}
	if far < safe {
		far = safe
	}
	fmt.Println(far - safe)
}
