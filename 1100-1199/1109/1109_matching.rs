use std::collections::VecDeque;
use std::io::{self, Read};

// Hopcroft-Karp: BFS layers from the free left vertices, then vertex-disjoint
// shortest augmenting paths along the layers
struct Matching {
    adj: Vec<Vec<usize>>,
    match_l: Vec<Option<usize>>,
    match_r: Vec<Option<usize>>,
    dist: Vec<Option<usize>>,
    it: Vec<usize>,
}

impl Matching {
    fn layer(&mut self) -> bool {
        let mut queue = VecDeque::new();
        for v in 0..self.adj.len() {
            self.dist[v] = None;
            if self.match_l[v].is_none() {
                self.dist[v] = Some(0);
                queue.push_back(v);
            }
        }
        let mut found = false;
        while let Some(v) = queue.pop_front() {
            for &u in &self.adj[v] {
                match self.match_r[u] {
                    None => found = true,
                    Some(w) if self.dist[w].is_none() => {
                        self.dist[w] = self.dist[v].map(|d| d + 1);
                        queue.push_back(w);
                    }
                    _ => {}
                }
            }
        }
        found
    }

    fn augment(&mut self, v: usize) -> bool {
        while self.it[v] < self.adj[v].len() {
            let u = self.adj[v][self.it[v]];
            let ok = match self.match_r[u] {
                None => true,
                Some(w) => {
                    self.dist[w].is_some()
                        && self.dist[w] == self.dist[v].map(|d| d + 1)
                        && self.augment(w)
                }
            };
            if ok {
                self.match_l[v] = Some(u);
                self.match_r[u] = Some(v);
                return true;
            }
            self.it[v] += 1;
        }
        self.dist[v] = None;
        false
    }
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut tok = input
        .split_ascii_whitespace()
        .map(|t| t.parse::<usize>().unwrap());
    let mut next = || tok.next().unwrap();
    let (m, n, k) = (next(), next(), next());
    let mut g = Matching {
        adj: vec![Vec::new(); m],
        match_l: vec![None; m],
        match_r: vec![None; n],
        dist: vec![None; m],
        it: vec![0; m],
    };
    for _ in 0..k {
        let (a, b) = (next(), next());
        g.adj[a - 1].push(b - 1);
    }
    let mut size = 0;
    while g.layer() {
        g.it.iter_mut().for_each(|x| *x = 0);
        for v in 0..m {
            if g.match_l[v].is_none() && g.augment(v) {
                size += 1;
            }
        }
    }
    // a minimum edge cover takes a maximum matching and one more edge for
    // every vertex the matching leaves uncovered
    println!("{}", m + n - size);
}
