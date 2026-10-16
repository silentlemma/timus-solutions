use std::collections::HashMap;
use std::io::{self, Read};

const WORD: usize = 64;
const FIELDS: usize = 3; // x, y and the price of a route

struct State {
    n: usize,
    words: usize,
    edges: Vec<(u32, usize, usize)>,
    // reach[x]: the targets x pays for, as a bit set
    reach: Vec<Vec<u64>>,
    size: Vec<usize>,
    into: Vec<Vec<(usize, usize)>>,
    rare: Vec<usize>,
    full: Vec<u64>,
    now: usize,
}

impl State {
    fn feasible(&self, m: usize) -> bool {
        let half = (self.n + 1) / 2;
        for a in 0..self.n {
            // one operator of a covering pair pays for at least half
            if self.size[a] < half {
                continue;
            }
            let missing: Vec<u64> =
                self.full.iter().zip(self.reach[a].iter()).map(|(f, r)| f ^ r).collect();
            if missing.iter().all(|&w| w == 0) {
                return true;
            }
            let t = *self.rare.iter().find(|&&y| missing[y / WORD] >> (y % WORD) & 1 == 1).unwrap();
            for &(i, b) in self.into[t].iter() {
                if i < m && (0..self.words).all(|w| self.reach[b][w] & missing[w] == missing[w]) {
                    return true;
                }
            }
        }
        false
    }

    // take the edges between two prefixes in or out
    fn shift(&mut self, to: usize) {
        while self.now < to {
            let (_, x, y) = self.edges[self.now];
            self.reach[x][y / WORD] ^= 1 << (y % WORD);
            self.size[x] += 1;
            self.now += 1;
        }
        while self.now > to {
            let (_, x, y) = self.edges[self.now - 1];
            self.reach[x][y / WORD] ^= 1 << (y % WORD);
            self.size[x] -= 1;
            self.now -= 1;
        }
    }
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let v: Vec<usize> = input.split_ascii_whitespace().map(|x| x.parse().unwrap()).collect();
    let (n, k) = (v[0], v[1]);
    let mut cheapest: HashMap<usize, u32> = HashMap::new();
    for route in v[2..].chunks(FIELDS).take(k) {
        let key = (route[0] - 1) * n + route[1] - 1;
        let c = route[2] as u32;
        let entry = cheapest.entry(key).or_insert(c);
        *entry = (*entry).min(c);
    }
    // the edges sorted by cost; the first m of them are those of cost up to
    // the m-th cost
    let mut edges: Vec<(u32, usize, usize)> =
        cheapest.iter().map(|(&key, &c)| (c, key / n, key % n)).collect();
    edges.sort_unstable();
    let words = (n + WORD - 1) / WORD;
    let mut into = vec![Vec::new(); n];
    for (i, &(_, x, y)) in edges.iter().enumerate() {
        into[y].push((i, x));
    }
    // the target with the fewest ways in comes first when picking a witness
    let mut rare: Vec<usize> = (0..n).collect();
    rare.sort_by_key(|&y| into[y].len());
    let mut full = vec![u64::MAX; words];
    if n % WORD != 0 {
        full[words - 1] = (1 << (n % WORD)) - 1;
    }
    let total = edges.len();
    let mut state = State {
        n,
        words,
        edges,
        reach: vec![vec![0; words]; n],
        size: vec![0; n],
        into,
        rare,
        full,
        now: 0,
    };
    state.shift(total);
    if total == 0 || !state.feasible(total) {
        println!("No solution");
        return;
    }
    let (mut lo, mut hi) = (1, total);
    while lo < hi {
        let mid = (lo + hi) / 2;
        state.shift(mid);
        if state.feasible(mid) {
            hi = mid;
        } else {
            lo = mid + 1;
        }
    }
    println!("{}", state.edges[lo - 1].0);
}
