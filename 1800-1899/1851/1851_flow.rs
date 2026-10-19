use std::collections::VecDeque;
use std::io::{self, Read};

// arcs in pairs e, e ^ 1: an undirected edge is two arcs of full capacity,
// each the reverse of the other
struct Network {
    head: Vec<Vec<usize>>,
    target: Vec<usize>,
    cap: Vec<i64>,
    level: Vec<i64>,
    arc: Vec<usize>,
}

impl Network {
    fn link(&mut self, a: usize, b: usize, forward: i64, backward: i64) {
        self.head[a].push(self.target.len());
        self.target.push(b);
        self.cap.push(forward);
        self.head[b].push(self.target.len());
        self.target.push(a);
        self.cap.push(backward);
    }

    fn levels(&mut self, source: usize, sink: usize) -> bool {
        self.level.iter_mut().for_each(|l| *l = -1);
        self.level[source] = 0;
        let mut queue = VecDeque::from(vec![source]);
        while let Some(v) = queue.pop_front() {
            for &e in &self.head[v] {
                let t = self.target[e];
                if self.cap[e] > 0 && self.level[t] < 0 {
                    self.level[t] = self.level[v] + 1;
                    queue.push_back(t);
                }
            }
        }
        self.level[sink] >= 0
    }

    fn push(&mut self, v: usize, sink: usize, amount: i64) -> i64 {
        if v == sink {
            return amount;
        }
        while self.arc[v] < self.head[v].len() {
            let e = self.head[v][self.arc[v]];
            let t = self.target[e];
            if self.cap[e] > 0 && self.level[t] == self.level[v] + 1 {
                let got = self.push(t, sink, amount.min(self.cap[e]));
                if got > 0 {
                    self.cap[e] -= got;
                    self.cap[e ^ 1] += got;
                    return got;
                }
            }
            self.arc[v] += 1;
        }
        0
    }
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut words = input.split_ascii_whitespace();
    let mut s: Vec<u8> = words.next().unwrap().bytes().collect();
    let mut p: Vec<u8> = words.next().unwrap().bytes().collect();
    let (n, m) = (s.len(), p.len());
    // every erased character is a node; a node on the source side becomes
    // 1, on the sink side 0. Characters s[j] and p[i] meet once in every
    // window where j - i is between 0 and n - m, and differing costs 1.
    let mut count = 0;
    let mut number = |c: u8| {
        if c == b'?' {
            count += 1;
            Some(count - 1)
        } else {
            None
        }
    };
    let node_s: Vec<Option<usize>> = s.iter().map(|&c| number(c)).collect();
    let node_p: Vec<Option<usize>> = p.iter().map(|&c| number(c)).collect();
    let (source, sink) = (count, count + 1);
    // pairs with a fixed 1 cost when the node is 0, and with a fixed 0 when 1
    let (mut ones, mut zeros) = (vec![0i64; count], vec![0i64; count]);
    let mut base = 0i64;
    let mut net = Network {
        head: vec![Vec::new(); count + 2],
        target: Vec::new(),
        cap: Vec::new(),
        level: vec![0; count + 2],
        arc: vec![0; count + 2],
    };
    for i in 0..m {
        for j in i..=i + n - m {
            match (node_p[i], node_s[j]) {
                (None, None) => base += (p[i] != s[j]) as i64,
                (Some(w), None) | (None, Some(w)) => {
                    let c = if node_p[i].is_none() { p[i] } else { s[j] };
                    if c == b'1' {
                        ones[w] += 1;
                    } else {
                        zeros[w] += 1;
                    }
                }
                (Some(u), Some(v)) => net.link(u, v, 1, 1),
            }
        }
    }
    for w in 0..count {
        // a node with both kinds of fixed partners pays the smaller anyway
        let both = ones[w].min(zeros[w]);
        base += both;
        if ones[w] > both {
            net.link(source, w, ones[w] - both, 0);
        }
        if zeros[w] > both {
            net.link(w, sink, zeros[w] - both, 0);
        }
    }
    let mut flow = 0i64;
    let limit = (n * m) as i64;
    while net.levels(source, sink) {
        net.arc.iter_mut().for_each(|a| *a = 0);
        loop {
            let got = net.push(source, sink, limit);
            if got == 0 {
                break;
            }
            flow += got;
        }
    }
    // the source side of the last search is a minimum cut
    net.levels(source, sink);
    for (c, node) in s.iter_mut().zip(&node_s).chain(p.iter_mut().zip(&node_p)) {
        if let Some(w) = *node {
            *c = if net.level[w] >= 0 { b'1' } else { b'0' };
        }
    }
    println!("{}", base + flow);
    println!("{}", String::from_utf8(s).unwrap());
    println!("{}", String::from_utf8(p).unwrap());
}
