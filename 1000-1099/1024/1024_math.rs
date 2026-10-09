use std::io::{self, Read};

fn gcd(a: u64, b: u64) -> u64 {
    if b == 0 {
        a
    } else {
        gcd(b, a % b)
    }
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let v: Vec<usize> = input
        .split_ascii_whitespace()
        .map(|t| t.parse().unwrap())
        .collect();
    let n = v[0];
    // P^k is the identity exactly when k is a multiple of every cycle length:
    // the order is their least common multiple
    let mut seen = vec![false; n + 1];
    let mut order: u64 = 1;
    for i in 1..=n {
        let (mut length, mut j) = (0, i);
        while !seen[j] {
            seen[j] = true;
            j = v[j];
            length += 1;
        }
        if length > 0 {
            order = order / gcd(order, length) * length;
        }
    }
    println!("{}", order);
}
