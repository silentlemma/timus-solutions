package main

import (
	"bufio"
	"fmt"
	"math/bits"
	"os"
	"strings"
)

const (
	roleCount   = 4
	stateCount  = 1 << roleCount
	roleLetters = "WMCR"
)

func main() {
	in := bufio.NewReader(os.Stdin)
	out := bufio.NewWriter(os.Stdout)
	defer out.Flush()

	var memberCount int
	fmt.Fscan(in, &memberCount)
	var reachable [stateCount]bool
	reachable[0] = true
	for member := 0; member < memberCount; member++ {
		var qualifications string
		fmt.Fscan(in, &qualifications)
		skills := 0
		for role := 0; role < roleCount; role++ {
			if strings.ContainsRune(qualifications, rune(roleLetters[role])) {
				skills |= 1 << role
			}
		}
		// Larger masks are visited first, so this member fills at most one role.
		for mask := stateCount - 1; mask >= 0; mask-- {
			if !reachable[mask] {
				continue
			}
			for role := 0; role < roleCount; role++ {
				bit := 1 << role
				if skills&bit != 0 && mask&bit == 0 {
					reachable[mask|bit] = true
				}
			}
		}
	}

	best := 0
	common := stateCount - 1
	for mask := 0; mask < stateCount; mask++ {
		if !reachable[mask] {
			continue
		}
		size := bits.OnesCount(uint(mask))
		if size > best {
			best = size
			common = mask
		} else if size == best {
			common &= mask
		}
	}
	fmt.Fprintln(out, best)
	if best < roleCount {
		names := [roleCount]string{"warrior", "mage", "cleric", "rogue"}
		fmt.Fprint(out, "Looking for")
		for role, name := range names {
			if common&(1<<role) == 0 {
				fmt.Fprint(out, " ", name)
			}
		}
		fmt.Fprintln(out)
	}
}
