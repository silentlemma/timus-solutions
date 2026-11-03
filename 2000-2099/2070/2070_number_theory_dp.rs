use std::io::{self, Read};

const FOURTH_ROOT_LIMIT: usize = 1000;
const FIRST_HIGHER_EXPONENT: usize = 4;

fn floor_sqrt(value: u64) -> usize {
    let mut root = (value as f64).sqrt() as u64;
    while (root + 1) * (root + 1) <= value {
        root += 1;
    }
    while root * root > value {
        root -= 1;
    }
    root as usize
}

fn prime_count(n: usize) -> usize {
    if n < 2 {
        return 0;
    }
    let root = floor_sqrt(n as u64);
    let mut small = vec![0; root + 1];
    let mut large = vec![0; root + 1];
    for i in 1..=root {
        small[i] = i - 1;
        large[i] = n / i - 1;
    }
    for prime in 2..=root {
        if small[prime] == small[prime - 1] {
            continue;
        }
        let (before, square) = (small[prime - 1], prime * prime);
        // g(v) counts survivors after smaller primes. Remove multiples
        // whose remaining factor is at least this prime.
        for i in 1..=root.min(n / square) {
            let reduced = n / i / prime;
            let count = if reduced <= root {
                small[reduced]
            } else {
                large[n / reduced]
            };
            large[i] -= count - before;
        }
        // Descending values preserve the previous-prime layer.
        for value in (square..=root).rev() {
            small[value] -= small[value / prime] - before;
        }
    }
    large[1]
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut numbers = input
        .split_ascii_whitespace()
        .map(|word| word.parse::<u64>().unwrap());
    let (left, right) = (numbers.next().unwrap(), numbers.next().unwrap());
    let mut bad = (prime_count(floor_sqrt(right)) - prime_count(floor_sqrt(left - 1))) as u64;
    let mut composite = [false; FOURTH_ROOT_LIMIT + 1];
    composite[0] = true;
    composite[1] = true;
    for p in 2..=floor_sqrt(FOURTH_ROOT_LIMIT as u64) {
        if !composite[p] {
            for multiple in (p * p..=FOURTH_ROOT_LIMIT).step_by(p) {
                composite[multiple] = true;
            }
        }
    }
    // k+1 prime and k>=2 implies even k. Beyond squares p^4<=R,
    // so a sieve to the fourth root supplies all remaining bases.
    for prime in 2..=FOURTH_ROOT_LIMIT {
        if composite[prime] {
            continue;
        }
        let square = (prime * prime) as u64;
        if square > right / square {
            break;
        }
        let (mut power, mut exponent) = (square * square, FIRST_HIGHER_EXPONENT);
        loop {
            if power >= left && !composite[exponent + 1] {
                bad += 1;
            }
            if power > right / square {
                break;
            }
            power *= square;
            exponent += 2;
        }
    }
    println!("{}", right - left + 1 - bad);
}
