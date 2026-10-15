use std::io::{self, Read};

const NEG: i64 = -(1 << 62);
const KINDS: usize = 3; // a count of teams: none, one, two or more

// every node of the tree over f keeps its total, its count of teams (capped
// at 2), its best prefix and suffix with exactly 0, 1 or 2+ teams, and its
// best range with at least two teams
struct Tree {
    size: usize,
    total: Vec<i64>,
    best: Vec<i64>,
    kind: Vec<usize>,
    pre: [Vec<i64>; KINDS],
    suf: [Vec<i64>; KINDS],
}

impl Tree {
    fn new(leaves: usize) -> Tree {
        let mut size = 1;
        while size < leaves {
            size *= 2;
        }
        let w = 2 * size;
        Tree {
            size,
            total: vec![0; w],
            best: vec![NEG; w],
            kind: vec![0; w],
            pre: [vec![0; w], vec![NEG; w], vec![NEG; w]],
            suf: [vec![0; w], vec![NEG; w], vec![NEG; w]],
        }
    }

    fn reset(&mut self) {
        let w = 2 * self.size;
        *self = Tree::new(w / 2);
    }

    fn pull(&mut self, v: usize) {
        let (a, b) = (2 * v, 2 * v + 1);
        self.total[v] = self.total[a] + self.total[b];
        self.kind[v] = (self.kind[a] + self.kind[b]).min(2);
        for k in 0..KINDS {
            self.pre[k][v] = self.pre[k][a];
            self.suf[k][v] = self.suf[k][b];
        }
        for j in 0..KINDS {
            // prefixes: inside the left child, or all of it and more
            if self.pre[j][b] != NEG {
                let k = (self.kind[a] + j).min(2);
                self.pre[k][v] = self.pre[k][v].max(self.total[a] + self.pre[j][b]);
            }
            if self.suf[j][a] != NEG {
                let k = (self.kind[b] + j).min(2);
                self.suf[k][v] = self.suf[k][v].max(self.suf[j][a] + self.total[b]);
            }
        }
        // ranges: inside a child, or across with two or more teams
        let mut top = self.best[a].max(self.best[b]);
        for i in 0..KINDS {
            for j in 2usize.saturating_sub(i)..KINDS {
                if self.suf[i][a] != NEG && self.pre[j][b] != NEG {
                    top = top.max(self.suf[i][a] + self.pre[j][b]);
                }
            }
        }
        self.best[v] = top;
    }

    fn add(&mut self, fi: usize, s: i64) {
        let mut v = self.size + fi;
        self.total[v] += s;
        self.kind[v] = (self.kind[v] + 1).min(2);
        for k in 0..KINDS {
            let value = if k == self.kind[v] { self.total[v] } else { NEG };
            self.pre[k][v] = value;
            self.suf[k][v] = value;
        }
        self.best[v] = if self.kind[v] == 2 { self.total[v] } else { NEG };
        v /= 2;
        while v > 0 {
            self.pull(v);
            v /= 2;
        }
    }
}

fn distinct(values: &[i64]) -> Vec<i64> {
    let mut sorted = values.to_vec();
    sorted.sort();
    sorted.dedup();
    sorted
}

fn main() {
    let mut text = String::new();
    io::stdin().read_to_string(&mut text).unwrap();
    let mut words = text.split_ascii_whitespace().map(|w| w.parse::<i64>().unwrap());
    let n = words.next().unwrap() as usize;
    let mut teams = Vec::with_capacity(n);
    for _ in 0..n {
        let (a, f, s) = (words.next().unwrap(), words.next().unwrap(), words.next().unwrap());
        teams.push((a, f, s));
    }
    let ages = distinct(&teams.iter().map(|t| t.0).collect::<Vec<_>>());
    let fs = distinct(&teams.iter().map(|t| t.1).collect::<Vec<_>>());
    let mut by_age: Vec<Vec<(usize, i64)>> = vec![Vec::new(); ages.len()];
    for &(a, f, s) in &teams {
        let ai = ages.binary_search(&a).unwrap();
        by_age[ai].push((fs.binary_search(&f).unwrap(), s));
    }
    let mut tree = Tree::new(fs.len());
    let mut answer = NEG;
    let (mut best_left, mut best_right) = (0, 0);
    for left in 0..ages.len() {
        tree.reset();
        for right in left..ages.len() {
            for &(fi, s) in &by_age[right] {
                tree.add(fi, s);
            }
            if tree.best[1] > answer {
                answer = tree.best[1];
                best_left = left;
                best_right = right;
            }
        }
    }
    // the range of f values with the largest total holding at least two
    // teams: for each right end the best left end has the least prefix sum
    // among those leaving at least two teams inside
    let nf = fs.len();
    let mut prefix = vec![0i64; nf + 1];
    let mut inside = vec![0usize; nf + 1];
    for r in best_left..=best_right {
        for &(fi, s) in &by_age[r] {
            prefix[fi + 1] += s;
            inside[fi + 1] += 1;
        }
    }
    for i in 0..nf {
        prefix[i + 1] += prefix[i];
        inside[i + 1] += inside[i];
    }
    let (mut top, mut low) = (NEG, NEG);
    let (mut lo, mut hi, mut low_at, mut t) = (0, 0, 0, 0);
    for r in 1..=nf {
        while t < r && inside[t] + 2 <= inside[r] {
            if low == NEG || prefix[t] < low {
                low = prefix[t];
                low_at = t;
            }
            t += 1;
        }
        if low != NEG && prefix[r] - low > top {
            top = prefix[r] - low;
            lo = low_at;
            hi = r - 1;
        }
    }
    println!("{} {}", ages[best_left], ages[best_right]);
    println!("{} {}", fs[lo], fs[hi]);
}
