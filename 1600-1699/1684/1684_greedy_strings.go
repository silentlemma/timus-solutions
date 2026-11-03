package main

import (
	"bufio"
	"io/ioutil"
	"os"
)

const bufferSize = 4096
const cut uint32 = 1 << 31

func main() {
	raw, _ := ioutil.ReadAll(os.Stdin)
	position := 0
	token := func() []byte {
		for position < len(raw) && raw[position] <= ' ' {
			position++
		}
		begin := position
		for position < len(raw) && raw[position] > ' ' {
			position++
		}
		return raw[begin:position]
	}
	word, text := token(), token()
	size, n := len(word), len(text)
	prefix := make([]uint32, size)
	matched := make([]uint32, n+1)
	for i := 1; i < size; i++ {
		k := prefix[i-1]
		for k > 0 && word[k] != word[i] {
			k = prefix[k-1]
		}
		if word[k] == word[i] {
			k++
		}
		prefix[i] = k
	}
	k := uint32(0)
	for end := 1; end <= n; end++ {
		for k > 0 && (int(k) == size || word[k] != text[end-1]) {
			k = prefix[k-1]
		}
		if word[k] == text[end-1] {
			k++
		}
		matched[end] = k
	}
	out := bufio.NewWriterSize(os.Stdout, bufferSize)
	defer out.Flush()
	for end := n; end > 0; {
		length := matched[end]
		if length == 0 {
			out.WriteString("Yes\n")
			return
		}
		// The high bit is free because every matched length is at most 75000.
		matched[end] |= cut
		end -= int(length)
	}
	out.WriteString("No\n")
	begin := 0
	for end := 1; end <= n; end++ {
		if matched[end]&cut != 0 {
			if begin > 0 {
				out.WriteByte(' ')
			}
			out.Write(text[begin:end])
			begin = end
		}
	}
	out.WriteByte('\n')
}
