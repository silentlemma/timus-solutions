use std::io::{self, Read};

const LIMIT: usize = 3162;
const PERSISTENT: u8 = 3;
const DECIMAL: usize = 10;

fn number(input: &mut impl Iterator<Item = u8>) -> usize {
    let mut value = 0;
    let mut started = false;
    for byte in input {
        if byte.is_ascii_digit() {
            value = value * DECIMAL + usize::from(byte - b'0');
            started = true;
        } else if started {
            break;
        }
    }
    value
}

fn count_small(occurrences: &mut [u8], prime: usize, best: &mut u8) -> bool {
    occurrences[prime] += 1;
    *best = (*best).max(occurrences[prime]);
    *best == PERSISTENT
}

fn main() {
    let stdin = io::stdin();
    let mut input = stdin.lock().bytes().map_while(Result::ok);
    let size = number(&mut input);
    let mut composite = [false; LIMIT + 1];
    let mut primes = Vec::new();
    for prime in 2..=LIMIT {
        if !composite[prime] {
            primes.push(prime);
            for multiple in (prime * prime..=LIMIT).step_by(prime) {
                composite[multiple] = true;
            }
        }
    }
    let mut occurrences = [0u8; LIMIT + 1];
    let mut large = Vec::with_capacity(size);
    let mut best = 0;
    for _ in 0..size {
        let mut value = number(&mut input);
        for &prime in &primes {
            if prime * prime > value {
                break;
            }
            if value % prime == 0 {
                if count_small(&mut occurrences, prime, &mut best) {
                    println!("infinity");
                    return;
                }
                while value % prime == 0 {
                    value /= prime;
                }
            }
        }
        if value > LIMIT {
            large.push(value as u32);
        } else if value > 1 && count_small(&mut occurrences, value, &mut best) {
            println!("infinity");
            return;
        }
    }
    large.sort_unstable();
    let (mut previous, mut count) = (0, 0);
    for prime in large {
        count = if prime == previous { count + 1 } else { 1 };
        previous = prime;
        best = best.max(count);
        if best == PERSISTENT {
            println!("infinity");
            return;
        }
    }
    println!("{best}");
}
