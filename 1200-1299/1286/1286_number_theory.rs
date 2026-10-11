use std::io::{self, Read};

fn gcd(a: i64, b: i64) -> i64 {
    if b == 0 {
        a.abs()
    } else {
        gcd(b, a % b)
    }
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut it = input
        .split_ascii_whitespace()
        .map(|t| t.parse::<i64>().unwrap());
    let mut next = || it.next().unwrap();
    let (p, q, x, y, x1, y1) = (next(), next(), next(), next(), next(), next());
    let (dx, dy, g) = (x1 - x, y1 - y, gcd(p, q));
    let ok = if g == 0 {
        dx == 0 && dy == 0
    } else if dx % g != 0 || dy % g != 0 {
        false
    } else {
        // with p/g and q/g coprime, the moves reach every point of the
        // lattice g Z^2, except that when both are odd every move keeps the
        // parity of (dx + dy) / g
        let both_odd = (p / g) % 2 != 0 && (q / g) % 2 != 0;
        !both_odd || (dx / g + dy / g) % 2 == 0
    };
    println!("{}", if ok { "YES" } else { "NO" });
}
