package main

import (
	"fmt"
	"io/ioutil"
	"os"
)

type fastInput struct {
	data []byte
	pos  int
}

func (in *fastInput) nextInt64() int64 {
	for in.pos < len(in.data) && in.data[in.pos] <= ' ' {
		in.pos++
	}
	var value int64
	for in.pos < len(in.data) && in.data[in.pos] > ' ' {
		value = value*10 + int64(in.data[in.pos]-'0')
		in.pos++
	}
	return value
}

type productWindow struct {
	bound   int64
	product int64
	left    int
}

func (window *productWindow) advance(values []int64, index int) {
	value := values[index]
	if value > window.bound {
		window.left = index + 1
		window.product = 1
		return
	}
	// Divide before multiplying to keep the product within the bound.
	for window.product > window.bound/value {
		window.product /= values[window.left]
		window.left++
	}
	window.product *= value
}

func main() {
	data, _ := ioutil.ReadAll(os.Stdin)
	in := fastInput{data: data}
	n := int(in.nextInt64())
	lower := in.nextInt64()
	upper := in.nextInt64()
	values := make([]int64, n)
	for i := range values {
		values[i] = in.nextInt64()
	}

	unreachable := n + 1
	dp := make([]int, n+1)
	for i := 1; i <= n; i++ {
		dp[i] = unreachable
	}
	queue := make([]int, n+1)
	head, tail, nextCut := 0, 0, 0
	large := productWindow{bound: upper, product: 1}
	small := productWindow{bound: lower - 1, product: 1}
	for i := range values {
		large.advance(values, i)
		small.advance(values, i)
		// Eligible cuts form a moving interval, so a minimum deque is enough.
		for nextCut < small.left && nextCut <= i {
			if dp[nextCut] != unreachable {
				for head < tail && dp[queue[tail-1]] >= dp[nextCut] {
					tail--
				}
				queue[tail] = nextCut
				tail++
			}
			nextCut++
		}
		for head < tail && queue[head] < large.left {
			head++
		}
		if head < tail {
			dp[i+1] = dp[queue[head]] + 1
		}
	}
	if dp[n] == unreachable {
		fmt.Println(-1)
	} else {
		fmt.Println(dp[n])
	}
}
