package main

import (
	"bufio"
	"os"
	"sort"
	"strconv"
)

const maxCoordinate = 1000
const maxDenominator = 4 * maxCoordinate
const scale = maxDenominator * maxDenominator
const halfTurn = 2 * scale
const fullTurn = 4 * scale
const distanceBits = 12
const idBits = 15
const keyShift = distanceBits + idBits
const idMask = (1 << idBits) - 1
const bufferSize = 4096
const outputSize = 32

var in = bufio.NewReaderSize(os.Stdin, bufferSize)

func nextInt() int64 {
	ch, _ := in.ReadByte()
	for ch <= ' ' {
		ch, _ = in.ReadByte()
	}
	sign, value := int64(1), int64(0)
	if ch == '-' {
		sign = -1
		ch, _ = in.ReadByte()
	}
	for ch >= '0' && ch <= '9' {
		value = value*10 + int64(ch-'0')
		ch, _ = in.ReadByte()
	}
	return sign * value
}

func abs(value int64) int64 {
	if value < 0 {
		return -value
	}
	return value
}

func main() {
	n := int(nextInt())
	ox, oy := nextInt(), nextInt()
	keys := make([]uint64, n-1)
	for identity := 2; identity <= n; identity++ {
		dx, dy := nextInt()-ox, nextInt()-oy
		distance := abs(dx) + abs(dy)
		var rank uint64
		if dy > 0 || (dy == 0 && dx > 0) {
			rank = uint64(distance-dx) * scale / uint64(distance)
		} else {
			rank = halfTurn + uint64(distance+dx)*scale/uint64(distance)
		}
		keys[identity-2] = rank<<keyShift | uint64(distance)<<idBits | uint64(identity)
	}
	sort.Slice(keys, func(i, j int) bool { return keys[i] < keys[j] })
	start := 0
	previous := keys[len(keys)-1] >> keyShift
	for i, key := range keys {
		current := key >> keyShift
		gap := current + fullTurn - previous
		if gap >= fullTurn {
			gap -= fullTurn
		}
		if gap >= halfTurn {
			start = i
		}
		previous = current
	}
	out := bufio.NewWriterSize(os.Stdout, bufferSize)
	defer out.Flush()
	var storage [outputSize]byte
	writeInt := func(value int) {
		line := strconv.AppendInt(storage[:0], int64(value), 10)
		line = append(line, '\n')
		out.Write(line)
	}
	writeInt(n)
	writeInt(1)
	for i := start; i < len(keys); i++ {
		writeInt(int(keys[i] & idMask))
	}
	for i := 0; i < start; i++ {
		writeInt(int(keys[i] & idMask))
	}
}
