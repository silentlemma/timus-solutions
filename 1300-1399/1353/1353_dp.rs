use std::io::{self, Read};

const DIGITS: usize = 9; // numbers below 10^9 have at most nine digits
const BASE: usize = 10;

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let target: usize = input.trim().parse().unwrap();
    // ways[s]: digit strings of the current length with digit sum s
    let mut ways: Vec<u64> = vec![1];
    for _ in 0..DIGITS {
        let mut next = vec![0u64; ways.len() + BASE - 1];
        for (s, &w) in ways.iter().enumerate() {
            for d in 0..BASE {
                next[s + d] += w;
            }
        }
        ways = next;
    }
    // 10^9 itself has digit sum 1; zero is not counted since S >= 1
    let extra = if target == 1 { 1 } else { 0 };
    println!("{}", ways[target] + extra);
}
