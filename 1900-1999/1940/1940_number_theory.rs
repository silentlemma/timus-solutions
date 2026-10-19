use std::collections::HashMap;
use std::io::{self, Read};

const MAX_MINUTES: usize = 300;
const MAX_DIVISOR: usize = MAX_MINUTES + 1;
const WHEEL_PRIMES: usize = 6;
const USED_BITS: u32 = 6;

struct Counter {
    primes: Vec<usize>,
    prime_counts: Vec<usize>,
    wheels: Vec<Vec<usize>>,
    memo: HashMap<u64, usize>,
    base: usize,
}

impl Counter {
    fn new() -> Self {
        let limit = MAX_DIVISOR * MAX_DIVISOR;
        let mut composite = vec![false; limit + 1];
        composite[0] = true;
        composite[1] = true;
        let mut divisor = 2;
        while divisor * divisor <= limit {
            if !composite[divisor] {
                for number in (divisor * divisor..=limit).step_by(divisor) {
                    composite[number] = true;
                }
            }
            divisor += 1;
        }
        let mut prime_counts = vec![0; limit + 1];
        let mut primes = Vec::new();
        for number in 1..=limit {
            prime_counts[number] = prime_counts[number - 1] + usize::from(!composite[number]);
            if number <= MAX_DIVISOR && !composite[number] {
                primes.push(number);
            }
        }
        let mut wheels = vec![vec![0, 1]];
        let mut period = 1;
        for used in 1..=WHEEL_PRIMES {
            period *= primes[used - 1];
            let mut blocked = vec![false; period + 1];
            for &prime in &primes[..used] {
                for number in (prime..=period).step_by(prime) {
                    blocked[number] = true;
                }
            }
            let mut prefix = vec![0; period + 1];
            for number in 1..=period {
                prefix[number] = prefix[number - 1] + usize::from(!blocked[number]);
            }
            wheels.push(prefix);
        }
        Self {
            primes,
            prime_counts,
            wheels,
            memo: HashMap::new(),
            base: 0,
        }
    }

    fn phi(&mut self, value: usize, remaining: usize) -> usize {
        if remaining == self.base {
            let prefix = &self.wheels[self.base];
            let period = prefix.len() - 1;
            return value / period * prefix[period] + prefix[value % period];
        }
        if value == 0 {
            return 0;
        }
        let last = self.primes[remaining - 1];
        if value < last {
            return 1;
        }
        if value < last * last {
            return 1 + self.prime_counts[value] - remaining;
        }
        let key = ((value as u64) << USED_BITS) | remaining as u64;
        if let Some(&cached) = self.memo.get(&key) {
            return cached;
        }
        let result = self.phi(value, remaining - 1) - self.phi(value / last, remaining - 1);
        self.memo.insert(key, result);
        result
    }

    fn count_years(&mut self, start: usize, duration: usize, minutes: usize) -> usize {
        let limit = minutes + 1;
        let used = self.prime_counts[limit];
        self.base = used.min(WHEEL_PRIMES);
        self.memo.clear();
        let finish = start + duration;
        let result = self.phi(finish, used) - self.phi(start, used);
        result + self.prime_counts[finish.min(limit)] - self.prime_counts[start.min(limit)]
    }
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut words = input.split_whitespace();
    let start = words.next().unwrap().parse().unwrap();
    let duration = words.next().unwrap().parse().unwrap();
    let minutes = words.next().unwrap().parse().unwrap();
    let mut counter = Counter::new();
    println!("{}", counter.count_years(start, duration, minutes));
}
