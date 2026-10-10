use std::io::{self, Read};

fn gcd(a: i64, b: i64) -> i64 {
    if b == 0 {
        a
    } else {
        gcd(b, a % b)
    }
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut tok = input
        .split_ascii_whitespace()
        .map(|t| t.parse::<i64>().unwrap());
    let (n, m) = (tok.next().unwrap(), tok.next().unwrap());
    // an a by b grid: the diagonal crosses a + b - 2 inner lines, two at once
    // at each of the gcd(a, b) - 1 inner corners; it starts in one block and
    // every crossing enters a new one
    let (a, b) = (n - 1, m - 1);
    println!("{}", a + b - gcd(a, b));
}
