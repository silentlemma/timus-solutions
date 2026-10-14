use std::cmp::Reverse;
use std::collections::BinaryHeap;
use std::fmt::Write as _;
use std::io::{self, Read};

const INF: i64 = 1 << 62;

struct Scanner {
    data: Vec<u8>,
    pos: usize,
}

impl Scanner {
    fn number(&mut self) -> i64 {
        while !self.data[self.pos].is_ascii_digit() {
            self.pos += 1;
        }
        let mut v = 0i64;
        while self.pos < self.data.len() && self.data[self.pos].is_ascii_digit() {
            v = v * 10 + (self.data[self.pos] - b'0') as i64;
            self.pos += 1;
        }
        v
    }
}

fn main() {
    let mut data = Vec::new();
    io::stdin().read_to_end(&mut data).unwrap();
    let mut sc = Scanner { data, pos: 0 };
    let n = sc.number() as usize;
    let (mut origin, mut target) = (Vec::new(), Vec::new());
    let (mut cap, mut flow, mut cost) = (Vec::new(), Vec::new(), Vec::new());
    let mut out = vec![Vec::new(); n + 1];
    let mut into = vec![Vec::new(); n + 1];
    // outflow minus inflow of every station
    let mut balance = vec![0i64; n + 1];
    // each pipe ends with a comma or a dot, each station with a dot
    let mut i = 1;
    while i <= n {
        let c = sc.data[sc.pos];
        if c.is_ascii_digit() {
            let (e, a) = (target.len(), sc.number() as usize);
            let b = sc.number();
            let f = sc.number();
            let d = sc.number();
            out[i].push(e);
            into[a].push(e);
            origin.push(i);
            target.push(a);
            cap.push(b);
            flow.push(f);
            cost.push(d);
            balance[i] += f;
            balance[a] -= f;
            continue;
        }
        if c == b'.' {
            i += 1;
        }
        sc.pos += 1;
    }

    // one more unit from any station with a well to station n through the
    // residual network: a pipe with spare room is free, a full one costs d,
    // and pushing back existing flow is free
    let mut dist = vec![INF; n + 1];
    let mut came: Vec<Option<(usize, i64)>> = vec![None; n + 1];
    let mut heap = BinaryHeap::new();
    for i in 1..n {
        if balance[i] > 0 {
            dist[i] = 0;
            heap.push(Reverse((0i64, i)));
        }
    }
    while let Some(Reverse((du, u))) = heap.pop() {
        if du > dist[u] {
            continue;
        }
        for &e in &out[u] {
            let nd = du + if flow[e] == cap[e] { cost[e] } else { 0 };
            let v = target[e];
            if nd < dist[v] {
                dist[v] = nd;
                came[v] = Some((e, 1));
                heap.push(Reverse((nd, v)));
            }
        }
        for &e in &into[u] {
            let v = origin[e];
            if flow[e] > 0 && du < dist[v] {
                dist[v] = du;
                came[v] = Some((e, -1));
                heap.push(Reverse((du, v)));
            }
        }
    }
    if dist[n] == INF {
        println!("Impossible");
        return;
    }
    let mut v = n;
    while let Some((e, step)) = came[v] {
        flow[e] += step;
        v = if step == 1 { origin[e] } else { target[e] };
    }
    let mut res = String::new();
    writeln!(res, "{}", dist[n]).unwrap();
    for pipes in &out[1..] {
        let parts: Vec<String> = pipes
            .iter()
            .map(|&e| format!("{} {}", target[e], flow[e]))
            .collect();
        writeln!(res, "{}.", parts.join(", ")).unwrap();
    }
    print!("{}", res);
}
