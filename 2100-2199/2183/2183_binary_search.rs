use std::io::{self, Read};

const LIMIT: i64 = 1_000_000_000; // the largest absolute mood

fn possible(a: &[i64], smallest: i64, x: i64) -> bool {
    // Every mood below x must be flipped, so the shortest segment covers them
    // all, and every mood inside must become at least x.
    let first = a.iter().position(|&v| v < x);
    let last = a.iter().rposition(|&v| v < x);
    match (first, last) {
        (Some(l), Some(r)) => a[l..=r].iter().all(|&v| v <= -x),
        _ => smallest <= -x, // some single mood can still be flipped
    }
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut it = input.split_ascii_whitespace().map(|t| t.parse::<i64>().unwrap());
    let n = it.next().unwrap() as usize;
    let a: Vec<i64> = it.take(n).collect();
    let smallest = *a.iter().min().unwrap();
    let (mut lo, mut hi) = (-LIMIT, LIMIT);
    while lo < hi {
        let middle = lo + (hi - lo + 1) / 2;
        if possible(&a, smallest, middle) {
            lo = middle;
        } else {
            hi = middle - 1;
        }
    }
    println!("{}", lo);
}
