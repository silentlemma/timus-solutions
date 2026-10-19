use std::io::{self, Read, Write};

const MAX_TERM: usize = 300;
const BLOCK_SIZE: usize = 1 << 16;
const RING_SIZE: usize = MAX_TERM + 1;

fn primes_up_to(bound: usize) -> Vec<usize> {
    let mut composite = vec![false; bound + 1];
    let mut primes = Vec::new();
    for p in 2..=bound {
        if !composite[p] {
            primes.push(p);
            for multiple in (p * p..=bound).step_by(p) {
                composite[multiple] = true;
            }
        }
    }
    primes
}

fn divisor_block(left: usize, right: usize, primes: &[usize]) -> Vec<u16> {
    let size = right - left + 1;
    let mut remaining: Vec<usize> = (left..=right).collect();
    let mut counts = vec![1_u16; size];
    for &p in primes {
        if p * p > right {
            break;
        }
        for offset in ((p - left % p) % p..size).step_by(p) {
            let mut exponent = 0_u16;
            while remaining[offset] % p == 0 {
                remaining[offset] /= p;
                exponent += 1;
            }
            counts[offset] *= exponent + 1;
        }
    }
    for i in 0..size {
        if remaining[i] > 1 {
            counts[i] *= 2;
        }
    }
    counts
}

fn solve(n: usize) -> Vec<usize> {
    let limit = MAX_TERM * n;
    let mut root = 1;
    while (root + 1) * (root + 1) <= limit {
        root += 1;
    }
    let primes = primes_up_to(root);
    let mut history = Vec::<u16>::new();
    let mut depth = vec![0; RING_SIZE];
    for left in (1..=limit).step_by(BLOCK_SIZE) {
        let right = limit.min(left + BLOCK_SIZE - 1);
        let counts = divisor_block(left, right, &primes);
        for (offset, raw) in counts.into_iter().enumerate() {
            let mut total = left + offset;
            let term = raw as usize;
            history.push(raw);
            let mut current = usize::from(total <= MAX_TERM);
            if term <= MAX_TERM && total > term {
                let previous = depth[(total - term) % RING_SIZE];
                if previous > 0 {
                    current = current.max(previous + 1);
                }
            }
            depth[total % RING_SIZE] = current;
            if current >= n {
                let mut answer = vec![0; n];
                for i in (1..n).rev() {
                    answer[i] = history[total - 1] as usize;
                    total -= answer[i];
                }
                answer[0] = total;
                return answer;
            }
        }
    }
    Vec::new()
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let n = input.trim().parse().unwrap();
    let answer = solve(n);
    let mut out = io::BufWriter::new(io::stdout().lock());
    if answer.is_empty() {
        writeln!(&mut out, "Impossible").unwrap();
    } else {
        for (i, value) in answer.iter().enumerate() {
            if i > 0 {
                write!(&mut out, " ").unwrap();
            }
            write!(&mut out, "{}", value).unwrap();
        }
        writeln!(&mut out).unwrap();
    }
}
