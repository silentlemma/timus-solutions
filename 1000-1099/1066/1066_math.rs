use std::io::{self, Read};

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut it = input.split_ascii_whitespace();
    let n: i64 = it.next().unwrap().parse().unwrap();
    let a: f64 = it.next().unwrap().parse().unwrap();
    // with the second height x, lamp i hangs at a + (i-1)(x - a) + (i-1)(i-2)
    // and the last height grows with x, so x is the smallest value keeping every
    // lamp at height 0 or above
    let x = (1..n).fold(0.0f64, |x, k| x.max(a - a / k as f64 - (k - 1) as f64));
    let m = (n - 1) as f64;
    println!("{:.2}", a + m * (x - a) + m * (m - 1.0));
}
