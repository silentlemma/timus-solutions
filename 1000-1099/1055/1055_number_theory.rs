use std::io::{self, Read};

// the exponent of the prime p in x! (Legendre's formula)
fn exponent(mut x: usize, p: usize) -> usize {
    let mut e = 0;
    while x > 0 {
        x /= p;
        e += x;
    }
    e
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let v: Vec<usize> = input
        .split_ascii_whitespace()
        .map(|t| t.parse().unwrap())
        .collect();
    let (n, m) = (v[0], v[1]);
    let mut composite = vec![false; n + 1];
    let mut count = 0;
    for p in 2..=n {
        if composite[p] {
            continue;
        }
        let mut q = p * p;
        while q <= n {
            composite[q] = true;
            q += p;
        }
        if exponent(n, p) > exponent(m, p) + exponent(n - m, p) {
            count += 1;
        }
    }
    println!("{}", count);
}
