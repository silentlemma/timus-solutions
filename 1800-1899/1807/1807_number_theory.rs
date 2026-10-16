use std::io::{self, Read};

// the best split of a prime p < 31623 never uses a prime above 700
const BOUND: usize = 1000;

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let n: u64 = input.trim().parse().unwrap();
    let p = (2..).take_while(|d| d * d <= n).find(|d| n % d == 0).unwrap_or(n);
    // the largest gcd is n / p: the pockets hold n/p times parts adding up
    // to p, and the lcm is n/p times the lcm of the parts. Parts that are
    // powers of distinct primes, padded with ones, give the best lcm
    let unit = n / p;
    let limit = p as usize;
    let mut groups: Vec<Vec<usize>> = Vec::new();
    let mut composite = vec![false; BOUND];
    for q in 2..BOUND.min(limit) {
        if composite[q] {
            continue;
        }
        for m in (q * q..BOUND).step_by(q) {
            composite[m] = true;
        }
        let mut powers = Vec::new();
        let mut w = q;
        while w < limit {
            powers.push(w);
            w *= q;
        }
        groups.push(powers);
    }
    // best[s]: the largest log of an lcm of parts with weight at most s
    let mut best = vec![0.0f64; limit + 1];
    let mut choices: Vec<Vec<u8>> = Vec::new();
    for powers in groups.iter() {
        let mut next = best.clone();
        let mut choice = vec![0u8; limit + 1];
        for (e, &w) in powers.iter().enumerate() {
            let value = (w as f64).ln();
            for s in w..=limit {
                let candidate = best[s - w] + value;
                if candidate > next[s] {
                    next[s] = candidate;
                    choice[s] = (e + 1) as u8;
                }
            }
        }
        best = next;
        choices.push(choice);
    }
    let mut parts: Vec<u64> = Vec::new();
    let (mut s, mut used) = (limit, 0);
    for (powers, choice) in groups.iter().zip(choices.iter()).rev() {
        let e = choice[s] as usize;
        if e > 0 {
            let w = powers[e - 1];
            parts.push(w as u64);
            s -= w;
            used += w;
        }
    }
    parts.extend(std::iter::repeat(1).take(limit - used));
    let line: Vec<String> = parts.iter().map(|x| (x * unit).to_string()).collect();
    println!("{}", line.join(" "));
}
