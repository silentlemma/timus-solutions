use std::io::{self, Read};

const FIELDS: usize = 4;

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let v: Vec<i64> = input
        .split_ascii_whitespace()
        .map(|t| t.parse().unwrap())
        .collect();
    let n = v[0] as usize;
    let rects: Vec<&[i64]> = v[1..1 + FIELDS * n].chunks(FIELDS).collect();
    // the rectangles form a chain from left to right, so the horizontal
    // part of the path is fixed; only the height at each border varies
    let (mut y, mut vertical) = (1i64, 0i64);
    for pair in rects.windows(2) {
        let (&[_, low1, _, high1], &[_, low2, _, high2]) = (pair[0], pair[1]) else {
            unreachable!()
        };
        let (lo, hi) = (low1.max(low2) + 1, high1.min(high2) - 1);
        if lo > hi {
            println!("-1");
            return;
        }
        // moving only when forced is optimal: clamp into the crossing
        let target = y.max(lo).min(hi);
        vertical += (target - y).abs();
        y = target;
    }
    let &[_, _, right, top] = rects[n - 1] else {
        unreachable!()
    };
    println!("{}", right - 2 + vertical + (top - 1 - y).abs());
}
