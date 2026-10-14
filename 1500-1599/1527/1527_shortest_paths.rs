use std::cmp::Reverse;
use std::collections::BinaryHeap;
use std::io::{self, Read};

const NONE: usize = usize::MAX;

#[derive(Clone, Copy)]
struct Road {
    from: usize,
    to: usize,
    toll: usize,
    time: usize,
    height: usize,
}

struct Map {
    n: usize,
    s: usize,
    f: usize,
    budget: usize,
    limit: usize,
    roads: Vec<Road>,
    out: Vec<Vec<usize>>,
}

impl Map {
    // a route from s to f within the limits using roads no higher than
    // height, as road numbers
    fn route(&self, height: usize) -> Option<Vec<usize>> {
        // best[v][c]: the least time to v with c tolls paid
        let mut best = vec![vec![NONE; self.budget + 1]; self.n + 1];
        let mut came_by = vec![vec![NONE; self.budget + 1]; self.n + 1];
        best[self.s][0] = 0;
        let mut heap = BinaryHeap::new();
        heap.push(Reverse((0, 0, self.s)));
        while let Some(Reverse((time, paid, v))) = heap.pop() {
            if best[v][paid] != time {
                continue;
            }
            // a state is useless if fewer tolls already reach v as fast
            if best[v][..paid].iter().any(|&b| b != NONE && b <= time) {
                continue;
            }
            if v == self.f {
                let (mut path, mut v, mut paid) = (Vec::new(), v, paid);
                while came_by[v][paid] != NONE {
                    let idx = came_by[v][paid];
                    path.push(idx + 1);
                    paid -= self.roads[idx].toll;
                    v = self.roads[idx].from;
                }
                path.reverse();
                return Some(path);
            }
            for &idx in &self.out[v] {
                let r = self.roads[idx];
                let (w, h, nt, np) = (r.to, r.height, time + r.time, paid + r.toll);
                if h <= height
                    && np <= self.budget
                    && nt <= self.limit
                    && (best[w][np] == NONE || nt < best[w][np])
                {
                    best[w][np] = nt;
                    came_by[w][np] = idx;
                    heap.push(Reverse((nt, np, w)));
                }
            }
        }
        None
    }
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut it = input
        .split_ascii_whitespace()
        .map(|t| t.parse::<usize>().unwrap());
    let mut next = || it.next().unwrap();
    let (n, m, s, f, budget, limit) = (next(), next(), next(), next(), next(), next());
    let roads: Vec<Road> = (0..m)
        .map(|_| Road {
            from: next(),
            to: next(),
            toll: next(),
            time: next(),
            height: next(),
        })
        .collect();
    if s == f {
        println!("0\n0\n");
        return;
    }
    let mut out = vec![Vec::new(); n + 1];
    for (i, r) in roads.iter().enumerate() {
        out[r.from].push(i);
    }
    // shorter parallel roads first, to avoid obsolete heap entries
    for edges in &mut out {
        edges.sort_by_key(|&i| roads[i].time);
    }
    let mut heights: Vec<usize> = roads.iter().map(|r| r.height).collect();
    heights.sort_unstable();
    // a cheapest route repeats no city, so it pays at most n - 1 tolls
    let map = Map {
        n,
        s,
        f,
        budget: budget.min(n - 1),
        limit,
        roads,
        out,
    };
    if map.route(heights[m - 1]).is_none() {
        println!("-1");
        return;
    }
    let (mut lo, mut hi) = (0, m - 1);
    while lo < hi {
        let mid = (lo + hi) / 2;
        if map.route(heights[mid]).is_some() {
            hi = mid;
        } else {
            lo = mid + 1;
        }
    }
    let path = map.route(heights[lo]).unwrap();
    let list: Vec<String> = path.iter().map(|x| x.to_string()).collect();
    println!("{}\n{}\n{}", heights[lo], path.len(), list.join(" "));
}
