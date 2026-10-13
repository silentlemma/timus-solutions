use std::io::{self, Read};

const QUARTERS: i64 = 4;

fn isqrt(n: i64) -> i64 {
    let mut s = (n as f64).sqrt() as i64;
    while s * s > n {
        s -= 1;
    }
    while (s + 1) * (s + 1) <= n {
        s += 1;
    }
    s
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let r: i64 = input.trim().parse().unwrap();
    // a tile shares more than one point with the disc exactly when its
    // corner nearest to the centre lies strictly inside: in one quarter,
    // tiles (i, j) with i^2 + j^2 < r^2, that is j <= isqrt(r^2 - i^2 - 1)
    let total: i64 = (0..r).map(|i| isqrt(r * r - i * i - 1) + 1).sum();
    println!("{}", QUARTERS * total);
}
