use std::io::{self, Read};

const PERCENT: i64 = 100;

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut it = input.split_whitespace().map(|t| t.parse::<i64>().unwrap());
    let mut next = || it.next().unwrap();
    // tuple fields are read from left to right
    let (b, c, d, k, p) = (next(), next(), next(), next(), next());
    // the usual insurance for the next k years; registering the accident costs
    // p percent of it on top, paying cash costs b on top
    let usual = k * c + d * k * (k + 1) / 2;
    // both sides times 100, so everything stays in integers
    let gap = usual * p - b * PERCENT;
    println!("{}", if gap > 0 { "Cash" } else { "Insurance" });
    let cents = gap.abs();
    println!("{}.{:02}", cents / PERCENT, cents % PERCENT);
}
