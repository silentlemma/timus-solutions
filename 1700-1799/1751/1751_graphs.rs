use std::io::{self, Read};

const NONE: usize = usize::MAX;
const WORD_BITS: usize = 64;

struct Tarjan<'a> {
    deps: &'a [Vec<usize>],
    index: Vec<usize>,
    low: Vec<usize>,
    on_stack: Vec<bool>,
    stack: Vec<usize>,
    group: Vec<usize>,
    groups: Vec<Vec<usize>>,
    counter: usize,
}

impl Tarjan<'_> {
    // hypotheses on one cycle of dependencies are all true or all false,
    // and Tarjan's method finds those groups, dependencies first
    fn visit(&mut self, v: usize) {
        self.index[v] = self.counter;
        self.low[v] = self.counter;
        self.counter += 1;
        self.stack.push(v);
        self.on_stack[v] = true;
        for &w in &self.deps[v] {
            if self.index[w] == NONE {
                self.visit(w);
                self.low[v] = self.low[v].min(self.low[w]);
            } else if self.on_stack[w] {
                self.low[v] = self.low[v].min(self.index[w]);
            }
        }
        if self.low[v] == self.index[v] {
            let mut members = Vec::new();
            loop {
                let w = self.stack.pop().unwrap();
                self.on_stack[w] = false;
                self.group[w] = self.groups.len();
                members.push(w);
                if w == v {
                    break;
                }
            }
            self.groups.push(members);
        }
    }
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut it = input.split_ascii_whitespace();
    let n: usize = it.next().unwrap().parse().unwrap();
    let (mut t, mut p, mut deps) = (Vec::new(), Vec::new(), Vec::new());
    for _ in 0..n {
        t.push(it.next().unwrap().parse::<f64>().unwrap());
        p.push(it.next().unwrap().parse::<f64>().unwrap());
        let k: usize = it.next().unwrap().parse().unwrap();
        deps.push((0..k).map(|_| it.next().unwrap().parse::<usize>().unwrap() - 1).collect());
    }
    let mut tarjan = Tarjan {
        deps: &deps,
        index: vec![NONE; n],
        low: vec![0; n],
        on_stack: vec![false; n],
        stack: Vec::new(),
        group: vec![NONE; n],
        groups: Vec::new(),
        counter: 0,
    };
    for v in 0..n {
        if tarjan.index[v] == NONE {
            tarjan.visit(v);
        }
    }
    let (group, mut groups) = (tarjan.group, tarjan.groups);
    // a group is worth checking only when every group it rests on is fully
    // admissible; inside it, checks stop at the first failure, so the order
    // by t / (1 - p) is the cheapest
    let count = groups.len();
    let (mut cost, mut sound) = (vec![0.0; count], vec![0.0; count]);
    let words = (count + WORD_BITS - 1) / WORD_BITS;
    let mut reach = vec![vec![0u64; words]; count];
    let has = |row: &[u64], h: usize| row[h / WORD_BITS] >> (h % WORD_BITS) & 1 == 1;
    for g in 0..count {
        groups[g].sort_by(|&a, &b| {
            (t[a] * (1.0 - p[b])).partial_cmp(&(t[b] * (1.0 - p[a]))).unwrap()
        });
        let (mut still, mut expected) = (1.0, 0.0);
        for &v in &groups[g] {
            expected += still * t[v];
            still *= p[v];
        }
        cost[g] = expected;
        sound[g] = still;
        for &v in &groups[g] {
            for &w in &deps[v] {
                let h = group[w];
                if h == g || has(&reach[g], h) {
                    continue;
                }
                for x in 0..words {
                    let bits = reach[h][x];
                    reach[g][x] |= bits;
                }
                reach[g][h / WORD_BITS] |= 1 << (h % WORD_BITS);
            }
        }
    }
    let answer: f64 = (0..count)
        .map(|g| {
            let chance: f64 =
                (0..count).filter(|&h| has(&reach[g], h)).map(|h| sound[h]).product();
            chance * cost[g]
        })
        .sum();
    println!("{:.3}", answer);
}
