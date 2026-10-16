use std::io::{self, Read};

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let n: u64 = input.trim().parse().unwrap();
    let mut primes: Vec<u64> = Vec::new();
    let mut exps: Vec<usize> = Vec::new();
    let mut rest = n;
    let mut p = 2;
    while p * p <= rest {
        if rest % p == 0 {
            let mut e = 0;
            while rest % p == 0 {
                rest /= p;
                e += 1;
            }
            primes.push(p);
            exps.push(e);
        }
        p += 1;
    }
    if rest > 1 {
        primes.push(rest);
        exps.push(1);
    }
    // a divisor is its exponent vector, numbered in mixed radix: every
    // proper divisor of a divisor gets a smaller number
    let mut radix = vec![1usize];
    for &e in exps.iter() {
        radix.push(radix.last().unwrap() * (e + 1));
    }
    let count = *radix.last().unwrap();
    let mut expected = vec![0.0f64; count];
    for index in 0..count {
        let mut total = 0;
        let mut parts: Vec<(usize, f64)> = vec![(0, 1.0)];
        for (i, &q) in primes.iter().enumerate() {
            let top = index / radix[i] % (exps[i] + 1);
            total += top;
            // gcd(m, r) for a uniform r splits over the primes: the exponent
            // of p in it is b < top with chance (1 - 1/p) / p^b, or top with
            // chance 1/p^top
            let q = q as f64;
            let mut next = Vec::with_capacity(parts.len() * (top + 1));
            for &(offset, chance) in parts.iter() {
                let mut scale = 1.0;
                for b in 0..=top {
                    let factor = if b < top { (1.0 - 1.0 / q) / scale } else { 1.0 / scale };
                    next.push((offset + b * radix[i], chance * factor));
                    scale *= q;
                }
            }
            parts = next;
        }
        if total <= 1 {
            continue; // 1 or a prime: no gcd is taken
        }
        let stay = parts[0].1 + parts[parts.len() - 1].1;
        let mut sum = 1.0;
        for &(offset, chance) in parts[1..parts.len() - 1].iter() {
            sum += chance * (expected[offset] + expected[index - offset]);
        }
        expected[index] = sum / (1.0 - stay);
    }
    println!("{:.10}", expected[count - 1]);
}
