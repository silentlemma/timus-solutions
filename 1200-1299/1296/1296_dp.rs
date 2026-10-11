use std::io::{self, Read};

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut it = input
        .split_ascii_whitespace()
        .map(|t| t.parse::<i64>().unwrap());
    let n = it.next().unwrap() as usize;
    // best is the largest segment sum so far (the empty segment gives 0), and
    // ending is the largest sum of a segment that ends at the current number
    let (mut best, mut ending) = (0i64, 0i64);
    for p in it.take(n) {
        ending += p;
        ending = ending.max(0);
        best = best.max(ending);
    }
    println!("{}", best);
}
