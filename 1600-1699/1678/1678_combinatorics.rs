use std::collections::{BTreeMap, HashMap};
use std::io::{self, Read};

const RANKS: &str = "23456789TJQKA";
const RANK_COUNT: usize = 13;
const HEADER_LINES: usize = 3; // sizes, own cards, shown cards

type Shape = Vec<usize>; // rank counts in decreasing order

struct Game {
    n: usize,
    m: usize,
    combos: Vec<Shape>,
    fact: Vec<f64>,
    best_cache: HashMap<Shape, i64>,
    rival_cache: HashMap<Shape, Vec<f64>>,
    own: Vec<usize>,
    shown: Vec<usize>,
    common: Vec<usize>,
    scale: f64,
    answer: f64,
}

fn sorted_down(mut a: Vec<usize>) -> Vec<usize> {
    a.sort_unstable_by(|x, y| y.cmp(x));
    a
}

// the partitions of total into at most parts positive parts, decreasing
fn partitions(total: usize, parts: usize) -> Vec<Shape> {
    fn build(rest: usize, top: usize, parts: usize, cur: &mut Shape, out: &mut Vec<Shape>) {
        if rest == 0 {
            out.push(cur.clone());
            return;
        }
        if cur.len() == parts {
            return;
        }
        for x in (1..=rest.min(top)).rev() {
            cur.push(x);
            build(rest - x, x, parts, cur, out);
            cur.pop();
        }
    }
    let mut out = Vec::new();
    build(total, total, parts, &mut Vec::new(), &mut out);
    out
}

impl Game {
    // the most valuable combination a hand with these sorted counts holds,
    // or -1: (v1, ..., vL) fits when the i-th largest count is at least the i-th v
    fn best(&mut self, hand: &Shape) -> i64 {
        if let Some(&v) = self.best_cache.get(hand) {
            return v;
        }
        let mut found = -1;
        for (c, need) in self.combos.iter().enumerate().rev() {
            if need.len() <= hand.len() && need.iter().zip(hand).all(|(v, h)| h >= v) {
                found = c as i64;
                break;
            }
        }
        self.best_cache.insert(hand.clone(), found);
        found
    }

    // the chance, for each combination, that a rival's best one is cheaper,
    // shifted by one place. Ranks with equal common counts are interchangeable,
    // so each group takes a partition of its share of the rival's cards
    fn rival(&mut self, common: &Shape) -> Vec<f64> {
        let mut groups: BTreeMap<usize, usize> = BTreeMap::new();
        for &v in common {
            *groups.entry(v).or_insert(0) += 1;
        }
        let m = self.m;
        let mut states: HashMap<(Shape, usize), f64> = HashMap::new();
        states.insert((Vec::new(), 0), 1.0);
        for (&v, &g) in &groups {
            let mut next: HashMap<(Shape, usize), f64> = HashMap::new();
            for ((shape, used), w) in &states {
                for s in 0..=m - used {
                    for p in partitions(s, g) {
                        let mut ways = self.fact[g] / self.fact[g - p.len()];
                        let mut mult: HashMap<usize, usize> = HashMap::new();
                        for &x in &p {
                            *mult.entry(x).or_insert(0) += 1;
                            ways /= self.fact[x];
                        }
                        for &c in mult.values() {
                            ways /= self.fact[c];
                        }
                        let mut merged = shape.clone();
                        merged.extend(p.iter().map(|x| v + x));
                        if v > 0 {
                            merged.extend(std::iter::repeat(v).take(g - p.len()));
                        }
                        let merged = sorted_down(merged);
                        *next.entry((merged, used + s)).or_insert(0.0) += w * ways;
                    }
                }
            }
            states = next;
        }
        let scale = self.fact[m] / (RANK_COUNT as f64).powi(m as i32);
        let count = self.combos.len();
        let mut dist = vec![0.0; count + 1];
        for ((shape, used), w) in &states {
            if *used == m {
                let b = self.best(shape);
                dist[(b + 1) as usize] += w * scale;
            }
        }
        let mut below = vec![0.0; count + 1];
        for c in 0..count {
            below[c + 1] = below[c] + dist[c];
        }
        below
    }

    // the hidden common cards: every way to spread them over the ranks
    fn spread(&mut self, r: usize, left: usize, weight: f64) {
        if r == RANK_COUNT - 1 {
            self.common[r] = self.shown[r] + left;
            let weight = weight / self.fact[left];
            let mine: Shape = (0..RANK_COUNT)
                .map(|i| self.common[i] + self.own[i])
                .filter(|&x| x > 0)
                .collect();
            let top = self.best(&sorted_down(mine));
            if top >= 0 {
                let sorted = sorted_down(self.common.clone());
                if !self.rival_cache.contains_key(&sorted) {
                    let below = self.rival(&sorted);
                    self.rival_cache.insert(sorted.clone(), below);
                }
                let beat = self.rival_cache[&sorted][(top + 1) as usize];
                self.answer += weight * self.scale * beat.powi(self.n as i32 - 1);
            }
            return;
        }
        for x in 0..=left {
            self.common[r] = self.shown[r] + x;
            self.spread(r + 1, left - x, weight / self.fact[x]);
        }
    }
}

fn main() {
    let mut text = String::new();
    io::stdin().read_to_string(&mut text).unwrap();
    let lines: Vec<&str> = text.split('\n').collect();
    let head: Vec<usize> = lines[0].split_whitespace().map(|w| w.parse().unwrap()).collect();
    let (n, m, k) = (head[0], head[1], head[2]);
    let count_ranks = |line: Option<&&str>| {
        let mut counts = vec![0; RANK_COUNT];
        for c in line.map_or("", |l| l).chars() {
            if let Some(i) = RANKS.find(c) {
                counts[i] += 1;
            }
        }
        counts
    };
    let own = count_ranks(lines.get(1));
    let shown = count_ranks(lines.get(2));
    let shown_count: usize = shown.iter().sum();
    let rest = lines[HEADER_LINES.min(lines.len())..].join(" ");
    let mut words = rest.split_whitespace().map(|w| w.parse::<usize>().unwrap());
    let count = words.next().unwrap();
    let mut combos = Vec::with_capacity(count);
    for _ in 0..count {
        let size = words.next().unwrap();
        let need: Shape = (0..size).map(|_| words.next().unwrap()).collect();
        combos.push(sorted_down(need));
    }
    let mut fact = vec![1.0f64; m + k + RANK_COUNT + 1];
    for i in 1..fact.len() {
        fact[i] = fact[i - 1] * i as f64;
    }
    let hidden = k - shown_count;
    let scale = fact[hidden] / (RANK_COUNT as f64).powi(hidden as i32);
    let mut game = Game {
        n,
        m,
        combos,
        fact,
        best_cache: HashMap::new(),
        rival_cache: HashMap::new(),
        own,
        shown,
        common: vec![0; RANK_COUNT],
        scale,
        answer: 0.0,
    };
    game.spread(0, hidden, 1.0);
    println!("{:.10}", game.answer);
}
