use std::fmt::Write as _;
use std::io::{self, Read};

// two people can team up only if their ranks differ by exactly 2, so half
// the rank changes parity along every pair: the graph is bipartite
const GAP: i32 = 2;
const SIDES: i32 = 2;
const NONE: usize = usize::MAX;

struct Matching {
    adj: Vec<Vec<usize>>,
    mate_left: Vec<usize>,
    mate_right: Vec<usize>,
    dist: Vec<i32>,
}

impl Matching {
    fn layers(&mut self) -> bool {
        let mut queue = Vec::new();
        for u in 0..self.adj.len() {
            self.dist[u] = -1;
            if self.mate_left[u] == NONE {
                self.dist[u] = 0;
                queue.push(u);
            }
        }
        let mut found = false;
        let mut h = 0;
        while h < queue.len() {
            let u = queue[h];
            h += 1;
            for &v in &self.adj[u] {
                let w = self.mate_right[v];
                if w == NONE {
                    found = true;
                } else if self.dist[w] < 0 {
                    self.dist[w] = self.dist[u] + 1;
                    queue.push(w);
                }
            }
        }
        found
    }

    fn augment(&mut self, u: usize) -> bool {
        for k in 0..self.adj[u].len() {
            let v = self.adj[u][k];
            let w = self.mate_right[v];
            if w == NONE || (self.dist[w] == self.dist[u] + 1 && self.augment(w)) {
                self.mate_left[u] = v;
                self.mate_right[v] = u;
                return true;
            }
        }
        self.dist[u] = -1;
        false
    }
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut it = input.split_ascii_whitespace();
    let n: usize = it.next().unwrap().parse().unwrap();
    let mut names = Vec::with_capacity(n);
    let mut writes = Vec::with_capacity(n);
    let mut tests = Vec::with_capacity(n);
    let mut ranks = Vec::with_capacity(n);
    let mut left = Vec::new();
    let mut right = Vec::new();
    for i in 0..n {
        names.push(it.next().unwrap());
        let kind = it.next().unwrap();
        let rank: i32 = it.next().unwrap().parse().unwrap();
        writes.push(kind != "testdata");
        tests.push(kind != "statements");
        ranks.push(rank);
        if rank / GAP % SIDES == 0 {
            left.push(i);
        } else {
            right.push(i);
        }
    }
    let adj: Vec<Vec<usize>> = left
        .iter()
        .map(|&a| {
            (0..right.len())
                .filter(|&j| {
                    let b = right[j];
                    (ranks[a] - ranks[b]).abs() == GAP
                        && ((writes[a] && tests[b]) || (writes[b] && tests[a]))
                })
                .collect()
        })
        .collect();
    let mut m = Matching {
        adj,
        mate_left: vec![NONE; left.len()],
        mate_right: vec![NONE; right.len()],
        dist: vec![-1; left.len()],
    };
    let mut total = 0;
    while m.layers() {
        for u in 0..left.len() {
            if m.mate_left[u] == NONE && m.augment(u) {
                total += 1;
            }
        }
    }
    let mut out = String::new();
    writeln!(out, "{}", total).unwrap();
    for u in 0..left.len() {
        let v = m.mate_left[u];
        if v == NONE {
            continue;
        }
        let (a, b) = (left[u], right[v]);
        if writes[a] && tests[b] {
            writeln!(out, "{} {}", names[a], names[b]).unwrap();
        } else {
            writeln!(out, "{} {}", names[b], names[a]).unwrap();
        }
    }
    print!("{}", out);
}
