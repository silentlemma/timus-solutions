use std::io::{self, Read};

// x^n mod m by repeated squaring
fn power(mut x: u64, mut n: u64, m: u64) -> u64 {
    let mut result = 1 % m;
    x %= m;
    while n > 0 {
        if n & 1 == 1 {
            result = result * x % m;
        }
        x = x * x % m;
        n >>= 1;
    }
    result
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let v: Vec<u64> = input
        .split_ascii_whitespace()
        .map(|t| t.parse().unwrap())
        .collect();
    let (n, m, y) = (v[0], v[1], v[2]);
    // only M candidates; a Y of M or more is never a remainder
    let roots: Vec<String> = (0..m)
        .filter(|&x| power(x, n, m) == y)
        .map(|x| x.to_string())
        .collect();
    if roots.is_empty() {
        println!("-1");
    } else {
        println!("{}", roots.join(" "));
    }
}
