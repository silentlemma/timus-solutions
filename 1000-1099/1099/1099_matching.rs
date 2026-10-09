use std::collections::{BTreeSet, VecDeque};
use std::io::{self, Read, Write};

const NONE: usize = usize::MAX;

struct Matcher {
    n: usize,
    adj: Vec<Vec<usize>>,
    mate: Vec<usize>,
    parent: Vec<usize>,
    base: Vec<usize>,
    used: Vec<bool>,
    blossom: Vec<bool>,
}

impl Matcher {
    fn lca(&self, mut a: usize, mut b: usize) -> usize {
        let mut seen = vec![false; self.n];
        loop {
            a = self.base[a];
            seen[a] = true;
            if self.mate[a] == NONE {
                break;
            }
            a = self.parent[self.mate[a]];
        }
        loop {
            b = self.base[b];
            if seen[b] {
                return b;
            }
            b = self.parent[self.mate[b]];
        }
    }

    fn mark(&mut self, mut v: usize, b: usize, mut child: usize) {
        while self.base[v] != b {
            let (bv, bm) = (self.base[v], self.base[self.mate[v]]);
            self.blossom[bv] = true;
            self.blossom[bm] = true;
            self.parent[v] = child;
            child = self.mate[v];
            v = self.parent[self.mate[v]];
        }
    }

    /// Edmonds' search from an exposed vertex: an alternating tree whose odd
    /// cycles (blossoms) are shrunk into their base vertex.
    fn find_path(&mut self, root: usize) -> usize {
        let n = self.n;
        self.used = vec![false; n];
        self.parent = vec![NONE; n];
        self.base = (0..n).collect();
        self.used[root] = true;
        let mut queue = VecDeque::from([root]);
        while let Some(v) = queue.pop_front() {
            for k in 0..self.adj[v].len() {
                let to = self.adj[v][k];
                if self.base[v] == self.base[to] || self.mate[v] == to {
                    continue;
                }
                if to == root || (self.mate[to] != NONE && self.parent[self.mate[to]] != NONE) {
                    let b = self.lca(v, to);
                    self.blossom = vec![false; n];
                    self.mark(v, b, to);
                    self.mark(to, b, v);
                    for i in 0..n {
                        if self.blossom[self.base[i]] {
                            self.base[i] = b;
                            if !self.used[i] {
                                self.used[i] = true;
                                queue.push_back(i);
                            }
                        }
                    }
                } else if self.parent[to] == NONE {
                    self.parent[to] = v;
                    if self.mate[to] == NONE {
                        return to;
                    }
                    self.used[self.mate[to]] = true;
                    queue.push_back(self.mate[to]);
                }
            }
        }
        NONE
    }
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let nums: Vec<i64> = input
        .split_ascii_whitespace()
        .map(|t| t.parse().unwrap())
        .collect();
    let n = nums[0] as usize;
    let mut sets = vec![BTreeSet::new(); n];
    for pair in nums[1..].chunks_exact(2) {
        let (a, b) = (pair[0], pair[1]);
        if a != b && a >= 1 && a <= n as i64 && b >= 1 && b <= n as i64 {
            sets[(a - 1) as usize].insert((b - 1) as usize);
            sets[(b - 1) as usize].insert((a - 1) as usize);
        }
    }
    let mut m = Matcher {
        n,
        adj: sets.into_iter().map(|s| s.into_iter().collect()).collect(),
        mate: vec![NONE; n],
        parent: vec![NONE; n],
        base: (0..n).collect(),
        used: vec![false; n],
        blossom: vec![false; n],
    };
    for v in 0..n {
        if m.mate[v] == NONE {
            if let Some(&u) = m.adj[v].iter().find(|&&u| m.mate[u] == NONE) {
                m.mate[u] = v;
                m.mate[v] = u;
            }
        }
    }
    for root in 0..n {
        if m.mate[root] == NONE && !m.adj[root].is_empty() {
            let mut v = m.find_path(root);
            while v != NONE {
                let pv = m.parent[v];
                let next = m.mate[pv];
                m.mate[v] = pv;
                m.mate[pv] = v;
                v = next;
            }
        }
    }
    let pairs: Vec<(usize, usize)> = (0..n)
        .filter(|&v| m.mate[v] != NONE && v < m.mate[v])
        .map(|v| (v + 1, m.mate[v] + 1))
        .collect();
    let mut out = format!("{}\n", 2 * pairs.len());
    for (a, b) in pairs {
        out.push_str(&format!("{} {}\n", a, b));
    }
    io::stdout().write_all(out.as_bytes()).unwrap();
}
