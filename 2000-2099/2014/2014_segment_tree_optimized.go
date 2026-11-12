package main

import (
	"bufio"
	"os"
	"sort"
	"strconv"
)

const bufferSize = 8192
const numberReserve = 24
const amountLimit = 50000
const fieldBits = 17
const fieldMask uint64 = (1 << fieldBits) - 1
const daySlots = 32
const hours = 24
const minutes = 60

type chronological []uint64

func (a chronological) Len() int           { return len(a) }
func (a chronological) Less(i, j int) bool { return a[i] < a[j] }
func (a chronological) Swap(i, j int)      { a[i], a[j] = a[j], a[i] }

func number(in *bufio.Reader) int {
	c, _ := in.ReadByte()
	for c != 0 && (c < '0' || c > '9') && c != '-' && c != '+' {
		c, _ = in.ReadByte()
	}
	negative := c == '-'
	if c == '-' || c == '+' {
		c, _ = in.ReadByte()
	}
	value := 0
	for c >= '0' && c <= '9' {
		value = value*10 + int(c-'0')
		c, _ = in.ReadByte()
	}
	if negative {
		return -value
	}
	return value
}

func main() {
	in := bufio.NewReaderSize(os.Stdin, bufferSize)
	n := number(in)
	events := make(chronological, n)
	for i := range events {
		amount, day, month := number(in), number(in), number(in)
		hour, minute := number(in), number(in)
		key := uint64(((month*daySlots+day)*hours+hour)*minutes + minute)
		events[i] = key<<(2*fieldBits) | uint64(i)<<fieldBits | uint64(amount+amountLimit)
	}
	sort.Sort(events)
	ranks := make([]uint32, n)
	for rank, event := range events {
		ranks[(event>>fieldBits)&fieldMask] = uint32(rank)
	}
	size := 1
	for size < n {
		size *= 2
	}
	leaves := make([]int32, size)
	// Leaves need one signed32 amount; only internal summaries need signed64.
	sums, prefixes := make([]int64, size), make([]int64, size)
	output := make([]byte, 0, bufferSize)
	for _, rank32 := range ranks {
		rank := int(rank32)
		leaves[rank] = int32(events[rank]&fieldMask) - amountLimit
		answer := int64(0)
		if size == 1 {
			if leaves[0] < 0 {
				answer = int64(leaves[0])
			}
		} else {
			parent := (size + rank) / 2
			left, right := int64(leaves[rank&^1]), int64(leaves[rank|1])
			sums[parent] = left + right
			best := int64(0)
			if left < best {
				best = left
			}
			if left+right < best {
				best = left + right
			}
			prefixes[parent] = best
			for parent /= 2; parent > 0; parent /= 2 {
				sums[parent] = sums[2*parent] + sums[2*parent+1]
				best, cross := prefixes[2*parent], sums[2*parent]+prefixes[2*parent+1]
				if cross < best {
					best = cross
				}
				prefixes[parent] = best
			}
			answer = prefixes[1]
		}
		if len(output)+numberReserve > cap(output) {
			os.Stdout.Write(output)
			output = output[:0]
		}
		output = strconv.AppendInt(output, answer, 10)
		output = append(output, '\n')
	}
	os.Stdout.Write(output)
}
