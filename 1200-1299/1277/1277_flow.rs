use std::collections::VecDeque;
use std::io::{self, Read};

struct Net {
    head: Vec<usize>,
    to: Vec<usize>,
    cap: Vec<i64>,
    next: Vec<usize>,
    level: Vec<usize>,
    current: Vec<usize>,
}

const NONE: usize = usize::MAX;

impl Net {
    fn arc(&mut self, a: usize, b: usize, c: i64) {
        for (u, v, w) in [(a, b, c), (b, a, 0)] {
            self.to.push(v);
            self.cap.push(w);
            self.next.push(self.head[u]);
            self.head[u] = self.to.len() - 1;
        }
    }

    fn push(&mut self, u: usize, sink: usize, limit: i64) -> i64 {
        if u == sink {
            return limit;
        }
        while self.current[u] != NONE {
            let e = self.current[u];
            let v = self.to[e];
            if self.cap[e] > 0 && self.level[v] == self.level[u] + 1 {
                let got = self.push(v, sink, limit.min(self.cap[e]));
                if got > 0 {
                    self.cap[e] -= got;
                    self.cap[e ^ 1] += got;
                    return got;
                }
            }
            self.current[u] = self.next[e];
        }
        0
    }
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut it = input
        .split_ascii_whitespace()
        .map(|t| t.parse::<i64>().unwrap());
    let mut next = || it.next().unwrap();
    let k = next();
    let (n, m, s, f) = (
        next() as usize,
        next() as usize,
        next() as usize,
        next() as usize,
    );
    let cost: Vec<i64> = (0..n).map(|_| next()).collect();
    if s == f {
        println!("NO");
        return;
    }
    // station v enters at 2v and leaves at 2v + 1; the arc between them
    // costs the police needed there. Museum and refuge cannot be taken,
    // and anything above K counts as too much
    let big = k + 1;
    let mut net = Net {
        head: vec![NONE; 2 * n],
        to: Vec::new(),
        cap: Vec::new(),
        next: Vec::new(),
        level: Vec::new(),
        current: Vec::new(),
    };
    for v in 0..n {
        let c = if v + 1 == s || v + 1 == f {
            big
        } else {
            cost[v].min(big)
        };
        net.arc(2 * v, 2 * v + 1, c);
    }
    for _ in 0..m {
        let (a, b) = (next() as usize - 1, next() as usize - 1);
        net.arc(2 * a + 1, 2 * b, big);
        net.arc(2 * b + 1, 2 * a, big);
    }
    let (source, sink) = (2 * (s - 1) + 1, 2 * (f - 1));
    // Dinic's blocking flows until the flow exceeds K or nothing gets through
    let mut flow = 0;
    while flow <= k {
        net.level = vec![NONE; 2 * n];
        net.level[source] = 0;
        let mut queue = VecDeque::from(vec![source]);
        while let Some(u) = queue.pop_front() {
            let mut e = net.head[u];
            while e != NONE {
                if net.cap[e] > 0 && net.level[net.to[e]] == NONE {
                    net.level[net.to[e]] = net.level[u] + 1;
                    queue.push_back(net.to[e]);
                }
                e = net.next[e];
            }
        }
        if net.level[sink] == NONE {
            break;
        }
        net.current = net.head.clone();
        while flow <= k {
            let got = net.push(source, sink, big);
            if got == 0 {
                break;
            }
            flow += got;
        }
    }
    println!("{}", if flow <= k { "YES" } else { "NO" });
}
