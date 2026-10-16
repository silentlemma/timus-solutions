use std::io::{self, Read};

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut it = input.split_ascii_whitespace().map(|w| w.parse::<u64>().unwrap());
    let (n, p) = (it.next().unwrap(), it.next().unwrap());
    // the route is the capital, then the other n - 1 = m cities twice each
    // with no city twice in a row, then the capital; such words over m
    // pairs obey a(m) = m (2m - 1) a(m - 1) + m (m - 1) a(m - 2)
    let (mut before, mut current) = (1 % p, 0u64);
    for m in 2..n {
        let next = (m * (2 * m - 1) % p * current + m * (m - 1) % p * before) % p;
        before = current;
        current = next;
    }
    println!("{}", current % p);
}
