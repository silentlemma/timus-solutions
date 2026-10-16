use std::io::{self, Read, Write};

const ALPHABET: usize = 26;
const NONE: usize = usize::MAX;

// suffix automaton; first[v] is the end of the first occurrence of v, and
// prefix[i] the state of the prefix ending at i
struct Automaton {
    next: Vec<[usize; ALPHABET]>,
    link: Vec<usize>,
    len: Vec<usize>,
    first: Vec<usize>,
    prefix: Vec<usize>,
    last: usize,
}

impl Automaton {
    fn new(s: &[u8]) -> Self {
        let mut a = Automaton {
            next: Vec::new(),
            link: Vec::new(),
            len: Vec::new(),
            first: Vec::new(),
            prefix: Vec::new(),
            last: 0,
        };
        a.add(NONE, 0, 0);
        for (i, &ch) in s.iter().enumerate() {
            a.extend((ch - b'a') as usize, i);
            a.prefix.push(a.last);
        }
        a
    }

    fn add(&mut self, parent: usize, length: usize, end: usize) -> usize {
        self.next.push([NONE; ALPHABET]);
        self.link.push(parent);
        self.len.push(length);
        self.first.push(end);
        self.len.len() - 1
    }

    fn extend(&mut self, c: usize, end: usize) {
        let cur = self.add(0, self.len[self.last] + 1, end);
        let mut p = self.last;
        while p != NONE && self.next[p][c] == NONE {
            self.next[p][c] = cur;
            p = self.link[p];
        }
        if p != NONE {
            let q = self.next[p][c];
            if self.len[p] + 1 == self.len[q] {
                self.link[cur] = q;
            } else {
                let clone = self.add(self.link[q], self.len[p] + 1, self.first[q]);
                self.next[clone] = self.next[q];
                while p != NONE && self.next[p][c] == q {
                    self.next[p][c] = clone;
                    p = self.link[p];
                }
                self.link[q] = clone;
                self.link[cur] = clone;
            }
        }
        self.last = cur;
    }
}

// adds to a range of positions and sums a prefix
struct Fenwick {
    plain: Vec<i64>,
    scaled: Vec<i64>,
}

impl Fenwick {
    fn point(tree: &mut [i64], at: usize, value: i64) {
        let mut at = at + 1;
        while at < tree.len() {
            tree[at] += value;
            at += at & at.wrapping_neg();
        }
    }

    fn sum(&self, count: usize) -> i64 {
        let (mut a, mut b) = (0i64, 0i64);
        let mut at = count;
        while at > 0 {
            a += self.plain[at];
            b += self.scaled[at];
            at -= at & at.wrapping_neg();
        }
        a * count as i64 - b
    }

    fn add(&mut self, from: usize, to: usize, value: i64) {
        if from >= to {
            return;
        }
        Self::point(&mut self.plain, from, value);
        Self::point(&mut self.plain, to, -value);
        Self::point(&mut self.scaled, from, value * from as i64);
        Self::point(&mut self.scaled, to, -value * to as i64);
    }
}

struct Edge {
    source: usize,
    dest: usize,
    from: usize,
    to: usize,
    distinct: i64,
}

fn swagness(s: &[u8]) -> i64 {
    let n = s.len();
    let sam = Automaton::new(s);
    let states = sam.len.len();
    let mut order: Vec<usize> = (0..states).collect();
    order.sort_by_key(|&v| sam.len[v]);

    // a state with exactly one way out is squeezed into the edge through it
    let mut only = vec![NONE; states];
    let mut keep = vec![false; states];
    for v in 0..states {
        let mut ways = 0;
        for &t in sam.next[v].iter() {
            if t != NONE {
                ways += 1;
                only[v] = t;
            }
        }
        keep[v] = v == 0 || ways != 1;
    }
    let mut target = vec![0; states];
    let mut extra = vec![0; states];
    for &v in order.iter().rev() {
        if keep[v] {
            target[v] = v;
        } else {
            target[v] = target[only[v]];
            extra[v] = 1 + extra[only[v]];
        }
    }
    // the compressed edges and, for each, its label s[from .. to]
    let mut edges: Vec<Edge> = Vec::new();
    for u in 0..states {
        if !keep[u] {
            continue;
        }
        for &t in sam.next[u].iter() {
            if t == NONE {
                continue;
            }
            let dest = target[t];
            let to = sam.first[dest];
            edges.push(Edge { source: u, dest, from: to - extra[t], to, distinct: 0 });
        }
    }

    // the suffix link tree in Euler order
    let mut children: Vec<Vec<usize>> = vec![Vec::new(); states];
    for v in 1..states {
        children[sam.link[v]].push(v);
    }
    let mut tin = vec![0; states];
    let mut tout = vec![0; states];
    let mut timer = 1;
    let mut stack: Vec<(usize, usize)> = vec![(0, 0)];
    while let Some(&(v, at)) = stack.last() {
        if at == children[v].len() {
            tout[v] = timer;
            stack.pop();
            continue;
        }
        let child = children[v][at];
        stack.last_mut().unwrap().1 += 1;
        tin[child] = timer;
        timer += 1;
        stack.push((child, 0));
    }
    // the latest end seen in a subtree, as a segment tree of maxima
    let size = states.next_power_of_two();
    let mut latest = vec![0usize; 2 * size];

    let mut by_end: Vec<Vec<usize>> = vec![Vec::new(); n + 1];
    for (e, edge) in edges.iter().enumerate() {
        by_end[edge.to + 1].push(e);
    }
    // count[p]: distinct substrings of s[0 .. end) whose last occurrence
    // starts at p; the states on one suffix link path that share their
    // last end form chains, and top[end] is the state just above a chain
    let mut count = Fenwick { plain: vec![0; n + 1], scaled: vec![0; n + 1] };
    let mut seen = vec![false; states];
    seen[0] = true;
    let mut top = vec![0usize; n + 1];
    for end in 1..=n {
        let v = sam.prefix[end - 1];
        count.add(end - sam.len[v], end, 1);
        let mut u = v;
        while !seen[u] {
            seen[u] = true;
            u = sam.link[u];
        }
        while u != 0 {
            let (mut lo, mut hi) = (tin[u] + size, tout[u] + size);
            let mut was = 0;
            while lo < hi {
                if lo & 1 == 1 {
                    was = was.max(latest[lo]);
                    lo += 1;
                }
                if hi & 1 == 1 {
                    hi -= 1;
                    was = was.max(latest[hi]);
                }
                lo /= 2;
                hi /= 2;
            }
            let above = top[was];
            count.add(was - sam.len[u], was - sam.len[above], -1);
            top[was] = u;
            u = above;
        }
        let mut at = tin[v] + size;
        latest[at] = end;
        while at > 1 {
            latest[at / 2] = latest[at].max(latest[at ^ 1]);
            at /= 2;
        }
        top[end] = 0;
        for &e in by_end[end].iter() {
            edges[e].distinct = count.sum(end) - count.sum(edges[e].from);
        }
    }

    // each compressed edge stands for as many tree edges as there are
    // paths from the root to its source
    let mut out: Vec<Vec<usize>> = vec![Vec::new(); states];
    for (e, edge) in edges.iter().enumerate() {
        out[edge.source].push(e);
    }
    let mut paths = vec![0i64; states];
    paths[0] = 1;
    let mut total = 0i64;
    for &v in order.iter() {
        if !keep[v] || paths[v] == 0 {
            continue;
        }
        for &e in out[v].iter() {
            total += paths[v] * edges[e].distinct;
            paths[edges[e].dest] += paths[v];
        }
    }
    total
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut words = input.split_ascii_whitespace();
    let n: usize = words.next().unwrap().parse().unwrap();
    let mut out = String::new();
    for word in words.take(n) {
        out.push_str(&swagness(word.as_bytes()).to_string());
        out.push('\n');
    }
    io::stdout().write_all(out.as_bytes()).unwrap();
}
