use std::cmp::Reverse;
use std::collections::BinaryHeap;
use std::io::{self, Read, Write};

// the local search stops after this many improvements
const ROUNDS: usize = 20000;
// an exact split of two generals may use at most this many bits of tables
const SPLIT_BITS: i64 = 4000000;
const WORD: i64 = 64;
// a box is its value shifted by INDEX_BITS, plus its number
const INDEX_BITS: i64 = 14;
const INDEX_MASK: i64 = (1 << INDEX_BITS) - 1;

struct Generals {
    sums: Vec<i64>,
    boxes: Vec<Vec<i64>>, // sorted, per general
}

fn put(list: &mut Vec<i64>, b: i64) {
    let k = list.partition_point(|&x| x < b);
    list.insert(k, b);
}

impl Generals {
    // the move or swap of boxes from hi to lo that leaves the smallest gap
    // between the two, if it is smaller than now
    fn exchange(&mut self, hi: usize, lo: usize) -> bool {
        let d = self.sums[hi] - self.sums[lo];
        if d <= 1 {
            return false;
        }
        let (a, b) = (&self.boxes[hi], &self.boxes[lo]);
        let half = d / 2;
        let mut candidates: Vec<(i64, usize, Option<usize>)> = Vec::new();
        if a.len() > 1 {
            let k = a.partition_point(|&x| x < half << INDEX_BITS);
            for ia in [k.wrapping_sub(1), k] {
                if ia < a.len() {
                    candidates.push((a[ia] >> INDEX_BITS, ia, None));
                }
            }
        }
        for ia in 0..a.len() {
            let va = a[ia] >> INDEX_BITS;
            if ia > 0 && va == a[ia - 1] >> INDEX_BITS {
                continue;
            }
            let k = b.partition_point(|&x| x < (va - half) << INDEX_BITS);
            for ib in [k.wrapping_sub(1), k] {
                if ib < b.len() {
                    candidates.push((va - (b[ib] >> INDEX_BITS), ia, Some(ib)));
                }
            }
        }
        let mut best = d;
        let mut chosen = None;
        for (t, ia, ib) in candidates {
            if t > 0 && t < d && (d - 2 * t).abs() < best {
                best = (d - 2 * t).abs();
                chosen = Some((ia, ib));
            }
        }
        let Some((ia, ib)) = chosen else {
            return false;
        };
        let x = self.boxes[hi].remove(ia);
        self.sums[hi] -= x >> INDEX_BITS;
        self.sums[lo] += x >> INDEX_BITS;
        if let Some(ib) = ib {
            let y = self.boxes[lo].remove(ib);
            put(&mut self.boxes[hi], y);
            self.sums[hi] += y >> INDEX_BITS;
            self.sums[lo] -= y >> INDEX_BITS;
        }
        put(&mut self.boxes[lo], x);
        true
    }

    // the most even split of the boxes of hi and lo found by subset sums, if
    // it narrows their gap and leaves each general a box
    fn split(&mut self, hi: usize, lo: usize) -> bool {
        let items: Vec<i64> = self.boxes[hi]
            .iter()
            .chain(&self.boxes[lo])
            .copied()
            .collect();
        let total = self.sums[hi] + self.sums[lo];
        let (count, words) = (items.len(), (total / WORD) as usize + 1);
        if (count as i64 + 1) * words as i64 * WORD > SPLIT_BITS {
            return false;
        }
        let mut reach = vec![vec![0u64; words]; count + 1];
        reach[0][0] = 1;
        for k in 0..count {
            let v = items[k] >> INDEX_BITS;
            let (shift, bits) = ((v / WORD) as usize, (v % WORD) as u32);
            for w in 0..words {
                let mut moved = 0u64;
                if w >= shift {
                    moved = reach[k][w - shift] << bits;
                    if bits > 0 && w > shift {
                        moved |= reach[k][w - shift - 1] >> (WORD as u32 - bits);
                    }
                }
                reach[k + 1][w] = reach[k][w] | moved;
            }
        }
        let has = |k: usize, t: i64| reach[k][(t / WORD) as usize] >> (t % WORD) & 1 == 1;
        let mut t = total / 2;
        while t > 0 && !has(count, t) {
            t -= 1;
        }
        if t == 0 || total - 2 * t >= self.sums[hi] - self.sums[lo] {
            return false;
        }
        let (mut small, mut big) = (Vec::new(), Vec::new());
        let mut rest = t;
        for k in (0..count).rev() {
            if !has(k, rest) {
                small.push(items[k]);
                rest -= items[k] >> INDEX_BITS;
            } else {
                big.push(items[k]);
            }
        }
        if small.is_empty() || big.is_empty() {
            return false;
        }
        small.sort();
        big.sort();
        self.boxes[hi] = big;
        self.boxes[lo] = small;
        self.sums[hi] = total - t;
        self.sums[lo] = t;
        true
    }
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut tok = input
        .split_ascii_whitespace()
        .map(|t| t.parse::<i64>().unwrap());
    let (n, m, limit) = (
        tok.next().unwrap() as usize,
        tok.next().unwrap() as usize,
        tok.next().unwrap(),
    );
    let value: Vec<i64> = tok.take(n).collect();
    // largest boxes first, each to the general with the least gold so far
    let mut order: Vec<usize> = (0..n).collect();
    order.sort_by(|&x, &y| value[y].cmp(&value[x]));
    let mut gen = Generals {
        sums: vec![0; m],
        boxes: vec![Vec::new(); m],
    };
    let mut poorest: BinaryHeap<Reverse<(i64, usize)>> = (0..m).map(|g| Reverse((0, g))).collect();
    for i in order {
        let Reverse((s, g)) = poorest.pop().unwrap();
        gen.boxes[g].push(value[i] << INDEX_BITS | i as i64);
        gen.sums[g] = s + value[i];
        poorest.push(Reverse((gen.sums[g], g)));
    }
    for list in gen.boxes.iter_mut() {
        list.sort();
    }
    // then even out the richest and the poorest general against the others
    for _ in 0..ROUNDS {
        let (mut hi, mut lo) = (0, 0);
        for g in 0..m {
            if gen.sums[g] > gen.sums[hi] {
                hi = g;
            }
            if gen.sums[g] < gen.sums[lo] {
                lo = g;
            }
        }
        if gen.sums[hi] - gen.sums[lo] <= limit {
            break;
        }
        if gen.exchange(hi, lo) {
            continue;
        }
        let mut up: Vec<usize> = (0..m).collect();
        up.sort_by_key(|&g| gen.sums[g]);
        let mut down: Vec<usize> = (0..m).collect();
        down.sort_by_key(|&g| Reverse(gen.sums[g]));
        let mut moved = false;
        for &g in &up {
            if !moved && g != hi {
                moved = gen.exchange(hi, g);
            }
        }
        for &g in &down {
            if !moved && g != lo {
                moved = gen.exchange(g, lo);
            }
        }
        moved = moved || gen.split(hi, lo);
        for &g in &up {
            if !moved && g != hi {
                moved = gen.split(hi, g);
            }
        }
        for &g in &down {
            if !moved && g != lo {
                moved = gen.split(g, lo);
            }
        }
        if !moved {
            break;
        }
    }
    let most = *gen.sums.iter().max().unwrap();
    let least = *gen.sums.iter().min().unwrap();
    let mut out = format!("{}\n", most - least);
    for list in &gen.boxes {
        let mut ids: Vec<i64> = list.iter().map(|&b| (b & INDEX_MASK) + 1).collect();
        ids.sort();
        let line: Vec<String> = ids.iter().map(|id| id.to_string()).collect();
        out.push_str(&line.join(" "));
        out.push('\n');
    }
    io::stdout().write_all(out.as_bytes()).unwrap();
}
