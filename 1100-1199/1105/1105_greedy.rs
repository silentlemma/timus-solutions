use std::fmt::Write;
use std::io::{self, Read};

const SHIFTS: usize = 3;
const EPS: f64 = 1e-9;

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut tok = input.split_ascii_whitespace();
    let mut num = || -> f64 { tok.next().unwrap().parse().unwrap() };
    let (t0, t1) = (num(), num());
    let n = num() as usize;
    let (mut lo, mut hi) = (vec![0.0; n], vec![0.0; n]);
    for i in 0..n {
        lo[i] = num();
        hi[i] = num();
    }
    // greedy cover: each step takes the observer reaching furthest among those
    // already present, so only neighbouring observers of the chain overlap
    let mut order: Vec<usize> = (0..n).collect();
    order.sort_by(|&a, &b| lo[a].partial_cmp(&lo[b]).unwrap());
    let mut chain = Vec::new();
    let (mut cur, mut i) = (t0, 0);
    while cur < t1 && i < n {
        let mut best: Option<usize> = None;
        while i < n && lo[order[i]] <= cur {
            if best.map_or(true, |b| hi[order[i]] > hi[b]) {
                best = Some(order[i]);
            }
            i += 1;
        }
        match best {
            Some(b) if hi[b] > cur => {
                chain.push(b);
                cur = hi[b];
            }
            _ => cur = if i < n { lo[order[i]] } else { t1 },
        }
    }
    // dropping every third observer of the chain leaves each piece of time
    // alone in two of the three shifts, so the best shift keeps 2/3 of it
    let m = chain.len();
    let alone = |shift: usize| -> f64 {
        let mut total = 0.0;
        for k in (0..m).filter(|k| k % SHIFTS != shift) {
            total += hi[chain[k]] - lo[chain[k]];
            if k + 1 < m && (k + 1) % SHIFTS != shift {
                total -= 2.0 * (hi[chain[k]] - lo[chain[k + 1]]).max(0.0);
            }
        }
        total
    };
    let best_shift = (0..SHIFTS)
        .max_by(|&a, &b| alone(a).partial_cmp(&alone(b)).unwrap())
        .unwrap();
    if alone(best_shift) < (t1 - t0) * 2.0 / SHIFTS as f64 - EPS {
        println!("0");
        return;
    }
    let painted: Vec<usize> = (0..m)
        .filter(|k| k % SHIFTS != best_shift)
        .map(|k| chain[k] + 1)
        .collect();
    let mut out = String::new();
    writeln!(out, "{}", painted.len()).unwrap();
    for p in painted {
        writeln!(out, "{}", p).unwrap();
    }
    print!("{}", out);
}
