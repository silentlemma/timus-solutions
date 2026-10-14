package main

import "fmt"

const mod = 1000000007

func power(b, e int64) int64 {
	r := int64(1)
	for b %= mod; e > 0; e >>= 1 {
		if e&1 == 1 {
			r = r * b % mod
		}
		b = b * b % mod
	}
	return r
}

// rootsPoly is the monic polynomial, lowest coefficient first, whose roots
// are 4 cos^2(j pi / (m + 1)) for j = 1 .. ceil(m / 2).
func rootsPoly(m int) []int64 {
	// S_k(x) = U_k(x / 2) grows by S_(k+1) = x S_k - S_(k-1) from S_0 = 1 and
	// S_1 = x, and its roots are 2 cos(j pi / (m + 1)) for j = 1 .. m
	prev, cur := []int64{1}, []int64{0, 1}
	for k := 1; k < m; k++ {
		next := make([]int64, len(cur)+1)
		copy(next[1:], cur)
		for i, c := range prev {
			next[i] = (next[i] - c + mod) % mod
		}
		prev, cur = cur, next
	}
	// the roots come in pairs +-x, plus 0 when m is odd, so an extra factor x
	// when m is odd makes every power even, and x^2 -> y keeps one per pair
	if m%2 == 1 {
		cur = append([]int64{0}, cur...)
	}
	var result []int64
	for i := 0; i < len(cur); i += 2 {
		result = append(result, cur[i])
	}
	return result
}

func det(a [][]int64) int64 {
	size := len(a)
	result := int64(1)
	for col := 0; col < size; col++ {
		pivot := col
		for pivot < size && a[pivot][col] == 0 {
			pivot++
		}
		if pivot == size {
			return 0
		}
		if pivot != col {
			a[pivot], a[col] = a[col], a[pivot]
			result = (mod - result) % mod
		}
		result = result * a[col][col] % mod
		inv := power(a[col][col], mod-2)
		for r := col + 1; r < size; r++ {
			f := a[r][col] * inv % mod
			if f == 0 {
				continue
			}
			for c := col; c < size; c++ {
				a[r][c] = ((a[r][c]-f*a[col][c])%mod + mod) % mod
			}
		}
	}
	return result
}

// resultant is Res(p, q) as the determinant of the Sylvester matrix.
func resultant(p, q []int64) int64 {
	d, e := len(p)-1, len(q)-1
	size := d + e
	var rows [][]int64
	for i := 0; i < e; i++ {
		row := make([]int64, size)
		for k := 0; k <= d; k++ {
			row[i+k] = p[d-k]
		}
		rows = append(rows, row)
	}
	for i := 0; i < d; i++ {
		row := make([]int64, size)
		for k := 0; k <= e; k++ {
			row[i+k] = q[e-k]
		}
		rows = append(rows, row)
	}
	return det(rows)
}

func main() {
	var m, n int
	if _, err := fmt.Scan(&m, &n); err != nil {
		return
	}
	// Kasteleyn: the number of tilings is the product of a_j + b_k over the
	// roots a_j of rootsPoly(m) and b_k of rootsPoly(n), which is the
	// resultant of the first with the monic polynomial whose roots are -b_k
	p, q := rootsPoly(m), rootsPoly(n)
	// (-1)^e q(-y) is monic with roots -b_k: coefficient i gets (-1)^(e - i)
	e := len(q) - 1
	for i := range q {
		if (e-i)%2 == 1 {
			q[i] = (mod - q[i]) % mod
		}
	}
	fmt.Println(resultant(p, q))
}
