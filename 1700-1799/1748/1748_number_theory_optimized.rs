use std::io::{self, BufWriter, Read, Write};

const PRIMES: [u64; 16] = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53];
const MOST: u32 = 64;

fn grow(
    records: &mut Vec<(u64, u32)>,
    limit: u64,
    index: usize,
    cap: u32,
    mut value: u64,
    divisors: u32,
) {
    let at = records.partition_point(|entry| entry.0 < value);
    if at == 0 || records[at - 1].1 < divisors {
        let mut end = at;
        // Keep only values that strictly improve the best earlier divisor count.
        while end < records.len() && records[end].1 <= divisors {
            end += 1;
        }
        records.drain(at..end);
        records.insert(at, (value, divisors));
    }
    if index == PRIMES.len() {
        return;
    }
    for exponent in 1..=cap {
        if value > limit / PRIMES[index] {
            break;
        }
        value *= PRIMES[index];
        grow(
            records,
            limit,
            index + 1,
            exponent,
            value,
            divisors * (exponent + 1),
        );
    }
}

fn main() {
    let mut raw = String::new();
    io::stdin().read_to_string(&mut raw).unwrap();
    let mut input = raw.split_ascii_whitespace();
    let tests: usize = input.next().unwrap().parse().unwrap();
    let queries: Vec<u64> = input
        .take(tests)
        .map(|token| token.parse().unwrap())
        .collect();
    let limit = *queries.iter().max().unwrap();
    let mut records = Vec::new();
    grow(&mut records, limit, 0, MOST, 1, 1);
    let stdout = io::stdout();
    let mut out = BufWriter::new(stdout.lock());
    for query in queries {
        let at = records.partition_point(|entry| entry.0 <= query) - 1;
        writeln!(out, "{} {}", records[at].0, records[at].1).unwrap();
    }
}
