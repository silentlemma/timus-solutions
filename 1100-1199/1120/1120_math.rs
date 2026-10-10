use std::io::{self, Read};

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let s: i64 = input.trim().parse().unwrap();
    // s = n*a + n(n-1)/2 with a >= 1 needs n(n+1)/2 <= s; try the longest first
    let mut n = (2.0 * s as f64).sqrt() as i64;
    while n * (n + 1) / 2 > s {
        n -= 1;
    }
    while (s - n * (n - 1) / 2) % n != 0 {
        n -= 1;
    }
    println!("{} {}", (s - n * (n - 1) / 2) / n, n);
}
