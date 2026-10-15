use std::fmt::Write as _;
use std::io::{self, Read};

const WRAP: usize = 4; // a fifth bacterium leaves one: counts go 1, 2, 3, 4, 1, ...

#[derive(PartialEq, Clone, Copy)]
enum Kind {
    Bad,
    First,  // before all free neighbours
    Last,   // after all of them
    Either, // an inner cell showing 1: before all or after all
    Wait,
}

struct Canvas {
    m: usize,
    adj: Vec<Vec<usize>>,
    // need[v]: how many free neighbours v must see settled after it, modulo
    // 4, stored as 1..4 like the picture; deg[v]: free neighbours
    need: Vec<usize>,
    deg: Vec<usize>,
    alive: Vec<bool>,
}

impl Canvas {
    fn kind(&self, v: usize) -> Kind {
        let (d, k) = (self.deg[v], self.need[v]);
        if k != 1 && k - 1 > d {
            Kind::Bad
        } else if d < WRAP && k == d + 1 {
            Kind::First
        } else if d < WRAP && k == 1 {
            Kind::Last
        } else if d == WRAP && k == 1 {
            Kind::Either
        } else {
            Kind::Wait
        }
    }

    /// settle v before (first) or after all its free neighbours
    fn take(&mut self, v: usize, first: bool) {
        self.alive[v] = false;
        for i in 0..self.adj[v].len() {
            let u = self.adj[v][i];
            if self.alive[u] {
                self.deg[u] -= 1;
                if !first {
                    // u now sees v settle after it
                    self.need[u] = if self.need[u] == 1 { WRAP } else { self.need[u] - 1 };
                }
            }
        }
    }

    /// necessary: the later-neighbour counts must add up to the edges, and
    /// touching undecided cells must split into firsts and lasts
    fn counts_fit(&self, cells: &[usize]) -> bool {
        let total = self.alive.len();
        let (mut edges, mut fixed) = (0usize, 0usize);
        let mut open = vec![false; total];
        let mut open_cells = Vec::new();
        for &v in cells {
            edges += self.deg[v];
            if self.kind(v) == Kind::Either {
                open[v] = true;
                open_cells.push(v);
            } else {
                fixed += self.need[v] - 1;
            }
        }
        let edges = edges / 2;
        let firsts = edges.wrapping_sub(fixed);
        if edges < fixed || firsts % WRAP != 0 || firsts / WRAP > open_cells.len() {
            return false;
        }
        let mut reach = vec![false; open_cells.len() + 1]; // s firsts possible so far
        reach[0] = true;
        let mut seen = vec![false; total];
        for &s in &open_cells {
            if seen[s] {
                continue;
            }
            seen[s] = true;
            let mut group = vec![s];
            let mut colour = [0usize; 2];
            let mut i = 0;
            while i < group.len() {
                let v = group[i];
                i += 1;
                colour[(v / self.m + v % self.m) % 2] += 1;
                for &u in &self.adj[v] {
                    if self.alive[u] && open[u] && !seen[u] {
                        seen[u] = true;
                        group.push(u);
                    }
                }
            }
            let mut next = vec![false; reach.len()];
            for t in 0..reach.len() {
                for &c in &colour {
                    if reach[t] && t + c < next.len() {
                        next[t + c] = true;
                    }
                }
            }
            reach = next;
        }
        reach[(edges - fixed) / WRAP]
    }

    fn components(&self, cells: &[usize]) -> Vec<Vec<usize>> {
        let mut inside = vec![false; self.alive.len()];
        let mut seen = vec![false; self.alive.len()];
        for &v in cells {
            inside[v] = true;
        }
        let mut parts = Vec::new();
        for &s in cells {
            if seen[s] {
                continue;
            }
            seen[s] = true;
            let mut part = vec![s];
            let mut i = 0;
            while i < part.len() {
                let v = part[i];
                i += 1;
                for &u in &self.adj[v] {
                    if inside[u] && self.alive[u] && !seen[u] {
                        seen[u] = true;
                        part.push(u);
                    }
                }
            }
            parts.push(part);
        }
        parts
    }

    /// an order of the free cells, or None
    fn solve(&mut self, mut cells: Vec<usize>) -> Option<Vec<usize>> {
        let (mut head, mut tail) = (Vec::new(), Vec::new());
        loop {
            let mut queue: Vec<usize> = cells
                .iter()
                .cloned()
                .filter(|&v| !matches!(self.kind(v), Kind::Either | Kind::Wait))
                .collect();
            let mut moved = false;
            while let Some(v) = queue.pop() {
                if !self.alive[v] {
                    continue;
                }
                let k = self.kind(v);
                if k == Kind::Bad {
                    return None;
                }
                if k != Kind::First && k != Kind::Last {
                    continue;
                }
                self.take(v, k == Kind::First);
                if k == Kind::First {
                    head.push(v);
                } else {
                    tail.push(v);
                }
                moved = true;
                queue.extend(self.adj[v].iter().filter(|&&u| self.alive[u]));
            }
            cells.retain(|&v| self.alive[v]);
            if !moved || cells.is_empty() {
                break;
            }
        }
        let mut middle = Vec::new();
        if !cells.is_empty() {
            let parts = self.components(&cells);
            if parts.len() > 1 {
                for part in parts {
                    middle.extend(self.solve(part)?);
                }
            } else {
                // the first cell of any order comes before all its neighbours,
                // so with no forced cell left it must be an undecided one
                let pick = *cells.iter().find(|&&v| self.kind(v) == Kind::Either)?;
                if !self.counts_fit(&cells) {
                    return None;
                }
                // an undecided cell comes before or after all its neighbours
                // in any order, so trying both ways for one misses nothing
                let rest: Vec<usize> = cells.iter().cloned().filter(|&v| v != pick).collect();
                let mut found = None;
                for &first in &[true, false] {
                    let saved = (self.need.clone(), self.deg.clone(), self.alive.clone());
                    self.take(pick, first);
                    let order = self.solve(rest.clone());
                    self.need = saved.0;
                    self.deg = saved.1;
                    self.alive = saved.2;
                    if let Some(mut order) = order {
                        if first {
                            order.insert(0, pick);
                        } else {
                            order.push(pick);
                        }
                        found = Some(order);
                        break;
                    }
                }
                middle = found?;
            }
        }
        head.extend(middle);
        head.extend(tail.iter().rev());
        Some(head)
    }
}

fn main() {
    let mut text = String::new();
    io::stdin().read_to_string(&mut text).unwrap();
    let nums: Vec<usize> = text.split_ascii_whitespace().map(|w| w.parse().unwrap()).collect();
    let (n, m) = (nums[0], nums[1]);
    let mut adj = vec![Vec::new(); n * m];
    for v in 0..n * m {
        let (r, c) = (v / m, v % m);
        if r > 0 {
            adj[v].push(v - m);
        }
        if r + 1 < n {
            adj[v].push(v + m);
        }
        if c > 0 {
            adj[v].push(v - 1);
        }
        if c + 1 < m {
            adj[v].push(v + 1);
        }
    }
    let deg = adj.iter().map(|a| a.len()).collect();
    let mut canvas = Canvas {
        m,
        adj,
        need: nums[2..2 + n * m].to_vec(),
        deg,
        alive: vec![true; n * m],
    };
    match canvas.solve((0..n * m).collect()) {
        None => println!("No"),
        Some(order) => {
            let mut out = String::from("Yes\n");
            for v in order {
                writeln!(out, "{} {}", v / m + 1, v % m + 1).unwrap();
            }
            print!("{}", out);
        }
    }
}
