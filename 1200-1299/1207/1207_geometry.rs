use std::io::{self, Read};

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let v: Vec<i64> = input
        .split_ascii_whitespace()
        .map(|t| t.parse().unwrap())
        .collect();
    let n = v[0] as usize;
    let (x, y): (Vec<i64>, Vec<i64>) = (0..n).map(|i| (v[1 + 2 * i], v[2 + 2 * i])).unzip();
    // the lowest point (the leftmost of the lowest) sees all others within
    // half a turn, so they can be sorted by angle with cross products
    let pivot = (0..n).min_by_key(|&i| (y[i], x[i])).unwrap();
    let (px, py) = (x[pivot], y[pivot]);
    let mut others: Vec<usize> = (0..n).filter(|&i| i != pivot).collect();
    others.sort_by(|&i, &j| {
        let cross = (x[i] - px) * (y[j] - py) - (y[i] - py) * (x[j] - px);
        0.cmp(&cross)
    });
    // the middle one leaves (n - 2) / 2 points on each side of the line
    println!("{} {}", pivot + 1, others[(n - 2) / 2] + 1);
}
