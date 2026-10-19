package main

import "fmt"

const percent = 100

func main() {
	var b, c, d, k, p int64
	fmt.Scan(&b, &c, &d, &k, &p)
	// the usual insurance for the next k years; registering the accident costs
	// p percent of it on top, paying cash costs b on top
	usual := k*c + d*k*(k+1)/2
	// both sides times 100, so everything stays in integers
	gap := usual*p - b*percent
	if gap > 0 {
		fmt.Println("Cash")
	} else {
		fmt.Println("Insurance")
		gap = -gap
	}
	fmt.Printf("%d.%02d\n", gap/percent, gap%percent)
}
