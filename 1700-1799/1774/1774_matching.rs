use std::collections::VecDeque;
use std::io::{self, Read};

const SHAVES: i32 = 2;

struct Flow {
    to: Vec<usize>,
    cap: Vec<i32>,
    out: Vec<Vec<usize>>,
    level: Vec<i32>,
    at: Vec<usize>,
}

impl Flow {
    fn new(size: usize) -> Flow {
        Flow {
            to: Vec::new(),
            cap: Vec::new(),
            out: vec![Vec::new(); size],
            level: Vec::new(),
            at: Vec::new(),
        }
    }

    fn add(&mut self, a: usize, b: usize, cap: i32) -> usize {
        self.out[a].push(self.to.len());
        self.to.push(b);
        self.cap.push(cap);
        self.out[b].push(self.to.len());
        self.to.push(a);
        self.cap.push(0);
        self.to.len() - 2
    }

    fn push(&mut self, v: usize, sink: usize, limit: i32) -> i32 {
        if v == sink {
            return limit;
        }
        while self.at[v] < self.out[v].len() {
            let e = self.out[v][self.at[v]];
            let w = self.to[e];
            if self.cap[e] > 0 && self.level[w] == self.level[v] + 1 {
                let got = self.push(w, sink, limit.min(self.cap[e]));
                if got > 0 {
                    self.cap[e] -= got;
                    self.cap[e ^ 1] += got;
                    return got;
                }
            }
            self.at[v] += 1;
        }
        0
    }

    fn max_flow(&mut self, source: usize, sink: usize) -> i32 {
        let mut total = 0;
        loop {
            self.level = vec![-1; self.out.len()];
            self.level[source] = 0;
            let mut queue = VecDeque::from(vec![source]);
            while let Some(v) = queue.pop_front() {
                for &e in &self.out[v] {
                    if self.cap[e] > 0 && self.level[self.to[e]] < 0 {
                        self.level[self.to[e]] = self.level[v] + 1;
                        queue.push_back(self.to[e]);
                    }
                }
            }
            if self.level[sink] < 0 {
                return total;
            }
            self.at = vec![0; self.out.len()];
            loop {
                let got = self.push(source, sink, SHAVES);
                if got == 0 {
                    break;
                }
                total += got;
            }
        }
    }
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut words = input.split_ascii_whitespace().map(|w| w.parse::<i32>().unwrap());
    let mut next = || words.next().unwrap();
    let (n, k) = (next() as usize, next());
    let mut come = Vec::new();
    let mut stay = Vec::new();
    for _ in 0..n {
        come.push(next());
        stay.push(next());
    }
    // minutes between consecutive arrivals and departures see the same mages,
    // so they form blocks: a block of L minutes shaves k L times, at most
    // min(L, 2) of them on one mage
    let mut cuts: Vec<i32> = come.iter().zip(&stay).flat_map(|(&t, &s)| [t, t + s]).collect();
    cuts.sort();
    cuts.dedup();
    let blocks = cuts.len() - 1;
    let (source, sink) = (n + blocks, n + blocks + 1);
    let mut flow = Flow::new(sink + 1);
    let mut links: Vec<Vec<(usize, usize)>> = vec![Vec::new(); n];
    for i in 0..n {
        flow.add(source, i, SHAVES);
        for j in 0..blocks {
            if come[i] <= cuts[j] && cuts[j + 1] <= come[i] + stay[i] {
                let cap = (cuts[j + 1] - cuts[j]).min(SHAVES);
                links[i].push((j, flow.add(i, n + j, cap)));
            }
        }
    }
    for j in 0..blocks {
        flow.add(n + j, sink, k * (cuts[j + 1] - cuts[j]));
    }
    if flow.max_flow(source, sink) < SHAVES * n as i32 {
        println!("No");
        return;
    }
    // inside a block the shaves are dealt out round the minutes, so the two
    // shaves of one mage fall on different minutes and no minute gets more
    // than k of them
    let mut dealt = vec![0; blocks];
    let mut out = String::from("Yes\n");
    for i in 0..n {
        let mut times = Vec::new();
        for &(j, e) in &links[i] {
            for _ in 0..flow.cap[e ^ 1] {
                times.push(cuts[j] + dealt[j] % (cuts[j + 1] - cuts[j]));
                dealt[j] += 1;
            }
        }
        times.sort();
        out.push_str(&format!("{} {}\n", times[0], times[1]));
    }
    print!("{}", out);
}
