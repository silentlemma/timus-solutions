use std::collections::HashMap;
use std::io::{self, Read};

const INF: i32 = 1 << 30;
const WORD: usize = 64; // documents per word of a set

struct Solver {
    m: usize,
    week: i32,
    off: Vec<i32>,
    tail: Vec<i32>,
    topo: Vec<usize>,
    pre: Vec<Vec<usize>>,
    succ: Vec<Vec<usize>>,
    waiting: Vec<usize>,
    done: Vec<bool>,
    best_day: i32,
    best_plan: Vec<usize>,
    path: Vec<usize>,
    seen: HashMap<(u64, u64), i32>,
}

impl Solver {
    /// The first day from t on when the official of v receives.
    fn first_day(&self, t: i32, v: usize) -> i32 {
        t + (self.off[v] - t).rem_euclid(self.week)
    }

    /// No plan from day t on can fetch the last document earlier.
    fn lower_bound(&self, t: i32) -> i32 {
        let mut earliest = vec![0; self.m];
        let mut by_slot: Vec<Vec<(i32, i32)>> = vec![Vec::new(); self.week as usize];
        for &v in &self.topo {
            if self.done[v] {
                continue;
            }
            let mut base = t;
            for &p in &self.pre[v] {
                if !self.done[p] {
                    base = base.max(earliest[p] + 1);
                }
            }
            earliest[v] = self.first_day(base, v);
            by_slot[self.off[v] as usize].push((earliest[v], self.tail[v]));
        }
        // k documents of one reception day that cannot come before day r
        // take k such days from r on, and the last still has a tail ahead
        let mut bound = 0;
        for here in by_slot.iter_mut() {
            here.sort_unstable_by(|a, b| b.cmp(a));
            let mut shortest = INF;
            for (count, &(first, after)) in here.iter().enumerate() {
                shortest = shortest.min(after);
                bound = bound.max(first + count as i32 * self.week + shortest);
            }
        }
        bound
    }

    /// The first day with a document to fetch, and those documents.
    fn choices(&self, t: i32, wait: &[usize], taken: &[bool]) -> (i32, Vec<usize>) {
        let mut day = INF;
        let mut cands = Vec::new();
        for v in 0..self.m {
            if taken[v] || wait[v] != 0 {
                continue;
            }
            let d = self.first_day(t, v);
            if d < day {
                day = d;
                cands.clear();
            }
            if d == day {
                cands.push(v);
            }
        }
        cands.sort_by_key(|&v| (-self.tail[v], v));
        (day, cands)
    }

    /// Fetch the document with the longest chain behind it each time.
    fn greedy(&self, mut t: i32, count: usize) -> (i32, Vec<usize>) {
        let mut wait = self.waiting.clone();
        let mut taken = self.done.clone();
        let mut last = t - 1;
        let mut plan = Vec::with_capacity(count);
        for _ in 0..count {
            let (day, cands) = self.choices(t, &wait, &taken);
            let v = cands[0];
            taken[v] = true;
            plan.push(v);
            for &u in &self.succ[v] {
                wait[u] -= 1;
            }
            last = day;
            t = day + 1;
        }
        (last, plan)
    }

    fn search(&mut self, t: i32, mask: (u64, u64), count: usize) {
        if count == 0 {
            if t - 1 < self.best_day {
                self.best_day = t - 1;
                self.best_plan = self.path.clone();
            }
            return;
        }
        // the same documents in hand by an earlier day were already tried
        if let Some(&old) = self.seen.get(&mask) {
            if old <= t {
                return;
            }
        }
        self.seen.insert(mask, t);
        if self.lower_bound(t) >= self.best_day {
            return;
        }
        // fetching nothing on a day when something can be fetched never helps
        let (day, cands) = self.choices(t, &self.waiting, &self.done);
        for v in cands {
            self.done[v] = true;
            for i in 0..self.succ[v].len() {
                let u = self.succ[v][i];
                self.waiting[u] -= 1;
            }
            self.path.push(v);
            let (last, rest) = self.greedy(day + 1, count - 1);
            if last < self.best_day {
                self.best_day = last;
                self.best_plan = self.path.clone();
                self.best_plan.extend(rest);
            }
            if day < self.best_day {
                let mut next = mask;
                if v < WORD {
                    next.0 |= 1 << v;
                } else {
                    next.1 |= 1 << (v - WORD);
                }
                self.search(day + 1, next, count - 1);
            }
            self.path.pop();
            for i in 0..self.succ[v].len() {
                let u = self.succ[v][i];
                self.waiting[u] += 1;
            }
            self.done[v] = false;
        }
    }
}

fn main() {
    let mut s = String::new();
    io::stdin().read_to_string(&mut s).unwrap();
    let mut it = s
        .split_ascii_whitespace()
        .map(|x| x.parse::<i32>().unwrap());
    let mut next = || it.next().unwrap();
    let n = next() as usize;
    let week = next();
    let day_of: Vec<i32> = (0..=n).map(|i| if i == 0 { 0 } else { next() }).collect();
    let listed = |next: &mut dyn FnMut() -> i32| -> Vec<usize> {
        let mut items = Vec::new();
        loop {
            let v = next();
            if v == 0 {
                return items;
            }
            items.push(v as usize);
        }
    };
    let mut needs = vec![Vec::new()];
    for _ in 0..n {
        needs.push(listed(&mut next));
    }
    let today = next();
    let mut held = vec![false; n + 1];
    for d in listed(&mut next) {
        held[d] = true;
    }
    // every document still to get: the wanted ones and, behind them, the
    // papers they need, stopping at papers already held
    let mut todo = vec![false; n + 1];
    let mut stack: Vec<usize> = listed(&mut next)
        .into_iter()
        .filter(|&d| !held[d])
        .collect();
    while let Some(doc) = stack.pop() {
        if todo[doc] {
            continue;
        }
        todo[doc] = true;
        stack.extend(needs[doc].iter().filter(|&&p| !held[p]));
    }
    let docs: Vec<usize> = (1..=n).filter(|&d| todo[d]).collect();
    let mut index = vec![0; n + 1];
    for (i, &d) in docs.iter().enumerate() {
        index[d] = i;
    }
    let m = docs.len();
    let mut pre = vec![Vec::new(); m];
    let mut succ = vec![Vec::new(); m];
    for (v, &d) in docs.iter().enumerate() {
        for &p in &needs[d] {
            if todo[p] {
                pre[v].push(index[p]);
                succ[index[p]].push(v);
            }
        }
    }
    // day t (today is day 0) belongs to an official when t = off mod week
    let off: Vec<i32> = docs
        .iter()
        .map(|&d| (day_of[d] - today).rem_euclid(week))
        .collect();
    // a cycle among them makes the set impossible to get
    let waiting: Vec<usize> = pre.iter().map(|p| p.len()).collect();
    let mut left = waiting.clone();
    let mut topo: Vec<usize> = (0..m).filter(|&v| left[v] == 0).collect();
    let mut i = 0;
    while i < topo.len() {
        for &u in &succ[topo[i]] {
            left[u] -= 1;
            if left[u] == 0 {
                topo.push(u);
            }
        }
        i += 1;
    }
    if topo.len() < m {
        println!("No Solution");
        return;
    }
    if m == 0 {
        print!("0\n\n");
        return;
    }
    // tail[v]: days that must pass after v is fetched, along its longest chain
    let mut tail = vec![0; m];
    for &v in topo.iter().rev() {
        for &u in &succ[v] {
            let mut gap = (off[u] - off[v]).rem_euclid(week);
            if gap == 0 {
                gap = week;
            }
            tail[v] = tail[v].max(gap + tail[u]);
        }
    }
    let mut solver = Solver {
        m,
        week,
        off,
        tail,
        topo,
        pre,
        succ,
        waiting,
        done: vec![false; m],
        best_day: 0,
        best_plan: Vec::new(),
        path: Vec::new(),
        seen: HashMap::new(),
    };
    let (day, plan) = solver.greedy(0, m);
    solver.best_day = day;
    solver.best_plan = plan;
    solver.search(0, (0, 0), m);
    let words: Vec<String> = solver
        .best_plan
        .iter()
        .map(|&v| docs[v].to_string())
        .collect();
    println!("{}", solver.best_day);
    println!("{}", words.join(" "));
}
