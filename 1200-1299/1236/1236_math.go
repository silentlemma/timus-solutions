package main

import (
	"bufio"
	"encoding/hex"
	"fmt"
	"os"
	"strings"
)

const space = ' '

func main() {
	in := bufio.NewReader(os.Stdin)
	var s1, s2 string
	fmt.Fscan(in, &s1, &s2)
	short, _ := hex.DecodeString(s1)
	long, _ := hex.DecodeString(s2)
	// the long message is a space followed by the short one, so its first
	// byte gives the first key byte, and byte i+1 of the long message hides
	// the same clear byte as byte i of the short one
	key := make([]byte, len(long))
	key[0] = long[0] ^ space
	for i, e := range short {
		key[i+1] = long[i+1] ^ e ^ key[i]
	}
	fmt.Println(strings.ToUpper(hex.EncodeToString(key)))
}
