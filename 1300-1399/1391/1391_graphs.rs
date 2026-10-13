use std::io::{self, Read};

const LONGEST: usize = 16; // the longest cycle counted: no snake of length 18 gets out
const SHORTEST: usize = 4; // the shortest cycle on a grid
const LAST_SNAKE: usize = 17; // snakes of lengths 2 .. 17 are answered

struct Search {
    w: usize,
    root: usize,
    limit: usize,
    near: Vec<Vec<usize>>,
    dist: Vec<i64>,
    rank: Vec<usize>,
    best: Vec<i64>,
    on_path: Vec<bool>,
    needed: Vec<bool>,
}

impl Search {
    fn walk(&mut self, v: usize, steps: usize) {
        for i in 0..self.near[v].len() {
            let u = self.near[v][i];
            if u == self.root {
                if steps + 1 >= SHORTEST && self.needed[steps + 1] {
                    self.best[steps + 1] = self.dist[self.root];
                    self.needed[steps + 1] = false;
                }
                continue;
            }
            let (w, root) = (self.w, self.root);
            let away = (u / w).abs_diff(root / w) + (u % w).abs_diff(root % w);
            if !self.on_path[u] && self.rank[u] > self.rank[root] && steps + 1 + away <= self.limit
            {
                self.on_path[u] = true;
                self.walk(u, steps + 1);
                self.on_path[u] = false;
            }
        }
    }
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut it = input.split_ascii_whitespace();
    let mut num = || it.next().unwrap().parse::<usize>().unwrap();
    let (h, w, r0, c0) = (num(), num(), num(), num());
    let rows: Vec<&[u8]> = it.take(h).map(|s| s.as_bytes()).collect();
    let start = (r0 - 1) * w + c0 - 1;
    let mut free: Vec<bool> = (0..h * w).map(|v| rows[v / w][v % w] == b'.').collect();
    free[start] = true;
    let mut near = vec![Vec::new(); h * w];
    for v in 0..h * w {
        let (r, c) = ((v / w) as i64, (v % w) as i64);
        for (dr, dc) in [(-1i64, 0i64), (1, 0), (0, -1), (0, 1)] {
            let (nr, nc) = (r + dr, c + dc);
            if nr >= 0 && nr < h as i64 && nc >= 0 && nc < w as i64 {
                let u = nr as usize * w + nc as usize;
                if free[u] {
                    near[v].push(u);
                }
            }
        }
    }
    // distances from the entrance
    let mut dist = vec![-1i64; h * w];
    dist[start] = 0;
    let mut order = vec![start];
    let mut i = 0;
    while i < order.len() {
        let v = order[i];
        for &u in &near[v] {
            if dist[u] < 0 {
                dist[u] = dist[v] + 1;
                order.push(u);
            }
        }
        i += 1;
    }
    // rank: breadth-first position; a cycle is found from its first cell in this order
    let mut rank = vec![order.len(); h * w];
    for (i, &v) in order.iter().enumerate() {
        rank[v] = i;
    }
    let mut needed = vec![false; LONGEST + 1];
    for c in (SHORTEST..=LONGEST).step_by(2) {
        needed[c] = true;
    }
    let mut s = Search {
        w,
        root: 0,
        limit: 0,
        near,
        dist,
        rank,
        best: vec![-1; LONGEST + 1],
        on_path: vec![false; h * w],
        needed,
    };
    for &v in &order {
        s.limit = (SHORTEST..=LONGEST)
            .filter(|&c| s.needed[c])
            .max()
            .unwrap_or(0);
        if s.limit == 0 {
            break;
        }
        s.root = v;
        s.on_path[v] = true;
        s.walk(v, 0);
        s.on_path[v] = false;
    }
    let mut out = String::new();
    for length in 2..=LAST_SNAKE {
        let answer = (length..=LONGEST)
            .filter(|&c| s.best[c] >= 0)
            .map(|c| 2 * s.best[c] + c as i64)
            .min()
            .unwrap_or(-1);
        out.push_str(&format!("{}\n", answer));
    }
    print!("{}", out);
}
