use std::io::{self, Read};

fn gcd(mut a: u64, mut b: u64) -> u64 {
    while b != 0 {
        let t = a % b;
        a = b;
        b = t;
    }
    a
}

fn main() {
    let mut text = String::new();
    io::stdin().read_to_string(&mut text).unwrap();
    let n: u64 = text.trim().parse().unwrap();
    // the chance that the row ends with two cards: (n^2 + 3n - 2) / (2n (2n - 1))
    let num = n * (n + 2) + n - 2;
    let den = 2 * n * (2 * n - 1);
    let g = gcd(num, den);
    println!("{}/{}", num / g, den / g);
}
