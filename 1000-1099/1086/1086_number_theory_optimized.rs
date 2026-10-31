use std::io::{self, BufWriter, Read, Write};

// sieving this range gives 15000 primes, enough for every statement query.
const LIMIT: usize = 163842;
const PRIME_COUNT: usize = 15000;
const FIRST_ODD_PRIME: usize = 3;

fn main() {
    // index i represents 2*i+1, so even composite numbers need no storage.
    let mut composite = vec![false; LIMIT / 2];
    let mut p = FIRST_ODD_PRIME;
    while p * p < LIMIT {
        if !composite[p / 2] {
            for i in (p * p / 2..LIMIT / 2).step_by(p) {
                composite[i] = true;
            }
        }
        p += 2;
    }
    // every computed prime is below LIMIT and fits u32.
    let mut primes = Vec::with_capacity(PRIME_COUNT);
    primes.push(2u32);
    for p in (FIRST_ODD_PRIME..LIMIT).step_by(2) {
        if !composite[p / 2] {
            primes.push(p as u32);
        }
    }
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut tokens = input
        .split_ascii_whitespace()
        .map(|s| s.parse::<usize>().unwrap());
    let queries = tokens.next().unwrap();
    let stdout = io::stdout();
    let mut output = BufWriter::new(stdout.lock());
    for n in tokens.take(queries) {
        writeln!(output, "{}", primes[n - 1]).unwrap();
    }
}
