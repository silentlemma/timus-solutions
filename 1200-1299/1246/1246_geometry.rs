use std::io::{self, Read};

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let v: Vec<i64> = input
        .split_ascii_whitespace()
        .map(|t| t.parse().unwrap())
        .collect();
    let n = v[0] as usize;
    let p: Vec<(i64, i64)> = v[1..1 + 2 * n].chunks(2).map(|c| (c[0], c[1])).collect();
    // twice the signed area by the shoelace formula: positive when the
    // runner goes counterclockwise, and the rope winds the same way
    let twice: i64 = (0..n)
        .map(|i| {
            let (a, b) = (p[i], p[(i + 1) % n]);
            a.0 * b.1 - b.0 * a.1
        })
        .sum();
    println!("{}", if twice > 0 { "ccw" } else { "cw" });
}
