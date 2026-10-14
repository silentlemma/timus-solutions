package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

// lines lists the lines of the map in the order of their stations; the
// circle line closes on itself
var lines = []string{
	"Pobedy I_Pyatiletki_square Zvezda Uralskaya Shevchenko Teatralnaya Kuybyshevskaya " +
		"Oborony_square Mayakovskaya Parkovaya Botanicheskaya Samolyotnaya Vtorchermet " +
		"Keramicheskaya",
	"Bakinskih_Komissarov Prospekt_Kosmonavtov Uralmash Mashinostroiteley Uralskaya Dinamo " +
		"1905_year_square Geologicheskaya Bazhovskaya Chkalovskaya Botanicheskaya " +
		"Shcherbakovskaya Uktusskie_Gory Nizhne_Isetskaya Himmash",
	"Taganskaya Elmash Turbinnaya Pionerskaya Shevchenko 1905_year_square Moskovskaya " +
		"Central_stadium Kraulya Metallurgov MEGA",
	"7_klyuchey Sortirovochnaya China_town Zarechny City 1905_year_square Kuybyshevskaya " +
		"Sibirskaya Siniye_kamni Lechebnaya Varshavskaya Kompressornaya Koltsovo",
	"Kalinovskaya Italyanskaya Ozyornaya Shefskaya Komsomolskaya Gagarinskaya Teatralnaya " +
		"Geologicheskaya Posadskaya Volgogradskaya Yugo_zapadnaya Akademicheskaya",
	"Zelyony_ostrov Tatishchevskaya Verh_Isetskaya Kommunarov_square 1905_year_square " +
		"Teatralnaya Vostochnaya Vtuzgorodok Kamennye_palatki University",
	"Vilonovskaya Gagarinskaya Vostochnaya Kuybyshevskaya Geologicheskaya Dvorets_sporta " +
		"Aviatsionnaya Voennaya Sovhoznaya",
}

const circle = "Uralskaya Pionerskaya Gagarinskaya Vtuzgorodok Sibirskaya Oborony_square " +
	"Bazhovskaya Dvorets_sporta Posadskaya Moskovskaya Kommunarov_square City"

func main() {
	adj := map[string][]string{}
	join := func(a, b string) {
		adj[a] = append(adj[a], b)
		adj[b] = append(adj[b], a)
	}
	for _, line := range lines {
		stops := strings.Fields(line)
		for i := 0; i+1 < len(stops); i++ {
			join(stops[i], stops[i+1])
		}
	}
	ring := strings.Fields(circle)
	for i := range ring {
		join(ring[i], ring[(i+1)%len(ring)])
	}
	// every run between neighbouring stations takes a minute and changes are
	// free, so the answer is the number of runs on a shortest path
	dist := map[string]map[string]int{}
	for start := range adj {
		seen := map[string]int{start: 0}
		queue := []string{start}
		for head := 0; head < len(queue); head++ {
			v := queue[head]
			for _, u := range adj[v] {
				if _, ok := seen[u]; !ok {
					seen[u] = seen[v] + 1
					queue = append(queue, u)
				}
			}
		}
		dist[start] = seen
	}
	in := bufio.NewReader(os.Stdin)
	out := bufio.NewWriter(os.Stdout)
	defer out.Flush()
	var n int
	fmt.Fscan(in, &n)
	for i := 0; i < n; i++ {
		var a, b string
		fmt.Fscan(in, &a, &b)
		fmt.Fprintln(out, dist[a][b])
	}
}
