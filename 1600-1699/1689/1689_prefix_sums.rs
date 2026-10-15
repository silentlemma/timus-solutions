use std::io::{self, Read};

fn main() {
    let mut text = String::new();
    io::stdin().read_to_string(&mut text).unwrap();
    let data: Vec<i64> = text.split_ascii_whitespace().map(|w| w.parse().unwrap()).collect();
    let mut head = data.iter().copied();
    let mut next = || head.next().unwrap();
    let (g, w, b, p, n) = (next(), next(), next(), next(), next() as usize);
    let last = g - b; // the barbell starts at s = 0 .. g - b
    let mut diff = vec![0i64; last as usize + 2];
    let mut add = |lo: i64, hi: i64, value: i64| {
        let (lo, hi) = (lo.max(0), hi.min(last));
        if lo <= hi {
            diff[lo as usize] += value;
            diff[hi as usize + 1] -= value;
        }
    };
    for &x in data.iter().rev().take(n).rev() {
        // a plate [a, a + p] hurts the worm [x, x + w] when they overlap by a
        // positive length, that is for whole a from x - p + 1 to x + w - 1.
        // The left plate starts at s, the right one at s + b - p
        let (lo1, hi1) = (x - p + 1, x + w - 1);
        let (lo2, hi2) = (x - b + 1, x + w - 1 - b + p);
        add(lo1, hi1, 1);
        add(lo2, hi2, 1);
        // a worm under both plates is hurt once
        add(lo1.max(lo2), hi1.min(hi2), -1);
    }
    let (mut best, mut best_hurt, mut hurt) = (0, i64::MAX, 0);
    for s in 0..=last as usize {
        hurt += diff[s];
        if hurt < best_hurt {
            best_hurt = hurt;
            best = s;
        }
    }
    println!("{}", best);
}
