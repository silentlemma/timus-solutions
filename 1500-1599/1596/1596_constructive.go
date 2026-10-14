package main

import (
	"bufio"
	"fmt"
	"os"
)

var moves = [8][2]int{{2, 1}, {2, -1}, {-2, 1}, {-2, -1}, {1, 2}, {1, -2}, {-1, 2}, {-1, -2}}

const (
	smallest = 6 // blocks have sides from 6 to 11
	largest  = 11
	usual    = 8 // the side of most blocks
)

type base struct {
	rows, cols int
	dirs       string
}

// tours holds a closed tour of each block, one direction per cell, row by
// row; each also moves between (1, C-2) and (3, C-1) and between (R-2, 1)
// and (R-1, 3).
var tours = []base{
	{6, 6, "516516177626345432322514745366748838"},
	{6, 7, "126211617888687268332123613455535887774734"},
	{6, 8, "156525625787878632685264127421145455883877487738"},
	{6, 9, "525156562757868786141163114342262714356735766348744348"},
	{6, 10, "556115556257672287163424233814322854521275386366367487338348"},
	{6, 11, "125226211667788756851812825437134352432148325565585858834747478784"},
	{7, 6, "116666158528336332126534147312556438337788"},
	{7, 8, "11661266128715123333873452624362143688245563556837774734"},
	{7, 10, "5516556512727728771234861362421271874312342717441255648367663433883888"},
	{8, 6, "126622128728734724522744732166128234355534778734"},
	{8, 7, "12622661788818121283432113381717834146362855655343377734"},
	{8, 8, "5555252277676782341516143461671431235782347475123566686634843888"},
	{8, 9, "156621166128768118325484734558514386176784638115862826756575534378747734"},
	{8, 10, "555652261252775177883414455718146168622454458828421243721838378566556477" +
		"88778734"},
	{8, 11, "116662165221282781178233737743114526745667445427488466211556814536356553" +
		"6554637834743834"},
	{9, 6, "115512778712328368375416145866743166322536345566748834"},
	{9, 8, "526552625776871814421814376757325221862834336814121754123453673677884388"},
	{9, 10, "521155651277721177121447381442346256131232743336123475463762115476451234" +
		"634666663388843888"},
	{10, 6, "156562128782323124724264143538136836522836123184558534777734"},
	{10, 7, "1165666178881852127343275786147156414184647278636121582454855347778734"},
	{10, 8, "116665661287151233336234126743821435166417326418325482341275223254854534" +
		"77387744"},
	{10, 9, "121656562728868782522322244141474584171774636315184232128757744128487518" +
		"558535636774747838"},
	{10, 10, "555115126272672887183481637114174111473651442722227743332224346238641814" +
		"7852623474656655363788477834"},
	{10, 11, "156615161265287888281832161667434137351141361467476413652742763564322481" +
		"58332128548285385558538556677743774434"},
	{11, 6, "525616727218144732741518124114328348755412744164513512336636348848"},
	{11, 8, "556555221767871234551414377326121342683614848512328564843255651214333312" +
		"5463466637388388"},
	{11, 10, "115652561672817812183283864332113571213814383628145214766724124444362814" +
		"83166638126883872455555355847774777734"},
}

// sides cuts a side into pieces from 6 to 11 long, all even if it is even.
func sides(length int) []int {
	var out []int
	for length >= usual+smallest {
		out = append(out, usual)
		length -= usual
	}
	if length > largest {
		out = append(out, smallest)
		length -= smallest
	}
	return append(out, length)
}

func main() {
	var n, m int
	if _, err := fmt.Scan(&n, &m); err != nil {
		return
	}
	w := bufio.NewWriter(os.Stdout)
	defer w.Flush()
	if n*m%2 == 1 {
		fmt.Fprintln(w, "No solution")
		return
	}
	// the tour as an undirected cycle: the two neighbours of every cell
	one := make([]int32, n*m)
	two := make([]int32, n*m)
	rows, cols := sides(n), sides(m)
	top := 0
	for _, h := range rows {
		left := 0
		for _, wd := range cols {
			var tour string
			for _, b := range tours {
				if b.rows == h && b.cols == wd {
					tour = b.dirs
				}
			}
			for i := 0; i < h; i++ {
				for j := 0; j < wd; j++ {
					mv := moves[tour[i*wd+j]-'1']
					u := (top+i)*m + left + j
					v := u + mv[0]*m + mv[1]
					one[u] = int32(v) // the next cell of u
					two[v] = int32(u) // the cell before v
				}
			}
			left += wd
		}
		top += h
	}
	swap := func(u, old, now int) {
		if int(one[u]) == old {
			one[u] = int32(now)
		} else {
			two[u] = int32(now)
		}
	}
	// join drops the moves a-b and c-d of two cycles and adds a-c and b-d
	join := func(a, b, c, d int) {
		swap(a, b, c)
		swap(b, a, d)
		swap(c, d, a)
		swap(d, c, b)
	}
	top = 0
	for _, h := range rows {
		left := cols[0]
		for _, wd := range cols[1:] {
			// the left block's move (1, C-2)-(3, C-1) and the right block's
			// corner move (0, 0)-(2, 1) give way to two moves across
			a, c := (top+1)*m+left-2, top*m+left
			join(a, a+2*m+1, c, c+2*m+1)
			left += wd
		}
		top += h
	}
	top = rows[0]
	for _, h := range rows[1:] {
		// the top block's (R-2, 1)-(R-1, 3) and the bottom block's (0, 0)-(1, 2)
		a, c := (top-2)*m+1, top*m
		join(a, a+m+2, c, c+m+2)
		top += h
	}
	// walk the cycle from the top left cell and write each move
	out := make([]byte, 2*n*m)
	prev, cur := -1, 0
	for k := 0; k < n*m; k++ {
		next := int(one[cur])
		if next == prev {
			next = int(two[cur])
		}
		dr, dc := next/m-cur/m, next%m-cur%m
		for d, mv := range moves {
			if mv[0] == dr && mv[1] == dc {
				out[2*cur] = byte('1' + d)
			}
		}
		out[2*cur+1] = ' '
		if cur%m == m-1 {
			out[2*cur+1] = '\n'
		}
		prev, cur = cur, next
	}
	w.Write(out)
}
