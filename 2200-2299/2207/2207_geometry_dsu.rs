use std::io::{self, Read};

const INF: i64 = 10_000_000_000;

struct Dsu {
    parent: Vec<i32>,
}

impl Dsu {
    fn new(n: usize) -> Self {
        Self {
            parent: vec![-1; n],
        }
    }

    fn find(&mut self, v: usize) -> usize {
        if self.parent[v] < 0 {
            return v;
        }
        let root = self.find(self.parent[v] as usize);
        self.parent[v] = root as i32;
        root
    }

    fn join(&mut self, u: usize, v: usize) -> bool {
        let (mut a, mut b) = (self.find(u), self.find(v));
        if a == b {
            return false;
        }
        if self.parent[a] > self.parent[b] {
            std::mem::swap(&mut a, &mut b);
        }
        self.parent[a] += self.parent[b];
        self.parent[b] = a as i32;
        true
    }
}

struct Sweep {
    order: Vec<usize>,
    rank: Vec<usize>,
    value: Vec<i64>,
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut tokens = input.split_whitespace().map(|s| s.parse::<i64>().unwrap());
    tokens.next();
    tokens.next();
    let n = tokens.next().unwrap() as usize;
    let m = tokens.next().unwrap() as usize;
    let count = n + m;
    let mut x = vec![0; count];
    let mut y = vec![0; count];
    let mut people = vec![0_i64; count];
    let mut jobs = vec![0_i64; count];
    for i in 0..count {
        x[i] = tokens.next().unwrap();
        y[i] = tokens.next().unwrap();
        let amount = tokens.next().unwrap();
        if i < n {
            people[i] = amount;
        } else {
            jobs[i] = amount;
        }
    }
    let target = people.iter().sum::<i64>().min(jobs.iter().sum::<i64>());
    let mut ys = y.clone();
    ys.sort_unstable();
    ys.dedup();
    let span = ys.len();
    let mut sweeps = Vec::new();
    for sx in [1, -1] {
        for sy in [1, -1] {
            let mut order: Vec<_> = (0..count).collect();
            order.sort_unstable_by_key(|&i| (sx * x[i], sy * y[i]));
            let rank = y
                .iter()
                .map(|v| {
                    let r = ys.binary_search(v).unwrap();
                    if sy == 1 {
                        r + 1
                    } else {
                        span - r
                    }
                })
                .collect();
            let mut value: Vec<_> = (0..count).map(|i| sx * x[i] + sy * y[i]).collect();
            value.push(-INF);
            sweeps.push(Sweep { order, rank, value });
        }
    }

    let mut dsu = Dsu::new(count);
    let mut components = count;
    let mut edges = Vec::new();
    while components > 1 {
        let mut roots: Vec<_> = (0..count).map(|i| dsu.find(i)).collect();
        roots.push(count);
        let mut best = vec![INF; count];
        let mut from = vec![count; count];
        let mut to = vec![count; count];
        for s in &sweeps {
            let mut first = [vec![count; span + 1], vec![count; span + 1]];
            let mut second = first.clone();
            for &i in &s.order {
                let color = usize::from(i >= n);
                let root = roots[i];
                let mut candidate = count;
                let mut k = s.rank[i];
                while k > 0 {
                    let mut v = first[1 - color][k];
                    if roots[v] == root {
                        v = second[1 - color][k];
                    }
                    if s.value[v] > s.value[candidate] {
                        candidate = v;
                    }
                    k &= k - 1;
                }
                if candidate != count && s.value[i] - s.value[candidate] < best[root] {
                    best[root] = s.value[i] - s.value[candidate];
                    from[root] = i;
                    to[root] = candidate;
                }
                // Keep maxima from two distinct frozen components.
                k = s.rank[i];
                while k <= span {
                    let v = first[color][k];
                    if s.value[i] > s.value[v] {
                        if roots[v] != root {
                            second[color][k] = v;
                        }
                        first[color][k] = i;
                    } else if roots[v] != root && s.value[i] > s.value[second[color][k]] {
                        second[color][k] = i;
                    }
                    k += k & k.wrapping_neg();
                }
            }
        }
        for r in 0..count {
            if from[r] != count && dsu.join(from[r], to[r]) {
                edges.push((best[r], from[r], to[r]));
                components -= 1;
            }
        }
    }
    edges.sort_unstable();
    dsu = Dsu::new(count);
    let mut score = 0;
    for (distance, u, v) in edges {
        let (a, b) = (dsu.find(u), dsu.find(v));
        score -= people[a].min(jobs[a]) + people[b].min(jobs[b]);
        let population = people[a] + people[b];
        let capacity = jobs[a] + jobs[b];
        dsu.join(a, b);
        let root = dsu.find(a);
        people[root] = population;
        jobs[root] = capacity;
        score += population.min(capacity);
        if score == target {
            println!("{} {}", target, distance);
            return;
        }
    }
}
