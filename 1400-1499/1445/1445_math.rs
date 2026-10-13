use std::io::{self, Read};

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let sizes: Vec<i64> = input
        .split_whitespace()
        .skip(1)
        .map(|x| x.parse().unwrap())
        .collect();
    let biggest = *sizes.iter().max().unwrap();
    let total: i64 = sizes.iter().sum();
    // the biggest company needs gifts from outside it: prepared or from the others
    let best = (2 * biggest - total).max(1);
    // in the worst order the biggest company comes first, and that many always suffice
    println!("{} {}", best, biggest);
}
