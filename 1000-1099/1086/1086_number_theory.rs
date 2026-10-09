use std::io::{self, Read};

// the 15000th prime is 163841
const LIMIT: usize = 163842;

fn main() {
    let mut composite = vec![false; LIMIT];
    let mut primes = Vec::new();
    for p in 2..LIMIT {
        if composite[p] {
            continue;
        }
        primes.push(p);
        let mut q = p * p;
        while q < LIMIT {
            composite[q] = true;
            q += p;
        }
    }
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut it = input
        .split_ascii_whitespace()
        .map(|t| t.parse::<usize>().unwrap());
    let k = it.next().unwrap();
    let out: Vec<String> = it.take(k).map(|n| primes[n - 1].to_string()).collect();
    println!("{}", out.join("\n"));
}
