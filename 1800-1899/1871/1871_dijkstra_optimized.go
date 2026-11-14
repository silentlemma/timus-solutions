package main

import (
	"bufio"
	"io/ioutil"
	"math/bits"
	"os"
	"strconv"
	"strings"
)

const maxLength = 140
const maxUsers = 100
const wordBits = 64
const prefixLength = len("RT @: ")

type users [(maxUsers + wordBits - 1) / wordBits]uint64

func (set *users) add(user int) {
	set[user/wordBits] |= 1 << (user % wordBits)
}

func (set users) contains(user int) bool {
	return set[user/wordBits]&(1<<(user%wordBits)) != 0
}

func main() {
	raw, err := ioutil.ReadAll(os.Stdin)
	if err != nil {
		return
	}
	input := string(raw)
	pos := 0
	next := func() string {
		for pos < len(input) && input[pos] <= ' ' {
			pos++
		}
		start := pos
		for pos < len(input) && input[pos] > ' ' {
			pos++
		}
		return input[start:pos]
	}
	n, err := strconv.Atoi(next())
	if err != nil || n < 1 || n > maxUsers {
		return
	}
	var names [maxUsers]string
	var starts [maxUsers]int
	var counts [maxUsers]int
	var followers [maxUsers]users
	index := make(map[string]int, n)
	for user := 0; user < n; user++ {
		name := next()
		names[user] = name
		index[name] = user
		counts[user], _ = strconv.Atoi(next())
		starts[user] = pos
		for i := 0; i < counts[user]; i++ {
			next()
		}
	}
	line := strings.IndexByte(input[pos:], '\n')
	tweet := strings.TrimRight(input[pos+line+1:], "\r\n")
	for user := 0; user < n; user++ {
		pos = starts[user]
		for i := 0; i < counts[user]; i++ {
			followers[user].add(index[next()])
		}
	}
	var buckets [maxLength + 1]users
	var sent, knows users
	buckets[len(tweet)].add(0)
	knows.add(0)
	// All retweet costs are positive. Process each sender at its first length.
	for length := len(tweet); length <= maxLength; length++ {
		for block, mask := range buckets[length] {
			for pending := mask &^ sent[block]; pending != 0; pending &= pending - 1 {
				user := block*wordBits + bits.TrailingZeros64(pending)
				sent.add(user)
				longer := length + prefixLength + len(names[user])
				for part, audience := range followers[user] {
					knows[part] |= audience
					if longer <= maxLength {
						buckets[longer][part] |= audience &^ sent[part]
					}
				}
			}
		}
	}
	count := 0
	for _, mask := range knows {
		count += bits.OnesCount64(mask)
	}
	output := bufio.NewWriter(os.Stdout)
	output.WriteString(strconv.Itoa(count) + "\n")
	for user, name := range names[:n] {
		if knows.contains(user) {
			output.WriteString(name + "\n")
		}
	}
	output.Flush()
}
