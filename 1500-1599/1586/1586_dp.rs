use std::io::{self, Read};

const MOD: u64 = 1_000_000_009;
const LOW: usize = 100; // the three-digit numbers
const HIGH: usize = 1000;
const PAIRS: usize = 100; // the last two digits
const BASE: usize = 10;
const WINDOW: usize = 3; // neighbouring digits that form a prime

fn main() {
    let mut text = String::new();
    io::stdin().read_to_string(&mut text).unwrap();
    let n: usize = text.trim().parse().unwrap();
    let primes: Vec<usize> = (LOW..HIGH)
        .filter(|&p| (2..).take_while(|d| d * d <= p).all(|d| p % d != 0))
        .collect();
    // ways[t]: numbers of the length so far that end in the two digits t and
    // whose every three neighbouring digits form a three-digit prime
    let mut ways = vec![0u64; PAIRS];
    for &p in &primes {
        ways[p % PAIRS] += 1;
    }
    for _ in WINDOW..n {
        let mut next = vec![0u64; PAIRS];
        // a prime abc extends a number ending in ab to one ending in bc
        for &p in &primes {
            next[p % PAIRS] = (next[p % PAIRS] + ways[p / BASE]) % MOD;
        }
        ways = next;
    }
    println!("{}", ways.iter().sum::<u64>() % MOD);
}
