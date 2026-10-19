use std::io::{self, Read};

const PRIME: usize = 11;
const DIGITS: usize = 10;

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let v: Vec<usize> = input.split_ascii_whitespace().map(|t| t.parse().unwrap()).collect();
    let n = v[0];
    let (a, b, c) = (&v[1..n + 1], &v[n + 1..2 * n + 1], &v[2 * n + 1..]);
    // chance[r]: probability that the product so far is r modulo 11
    let mut chance = vec![0.0f64; PRIME];
    chance[1] = 1.0;
    for i in 0..n {
        let mut next = vec![0.0f64; PRIME];
        for x in 0..DIGITS {
            let factor = (a[i] * x * x + b[i] * x + c[i]) % PRIME;
            for r in 0..PRIME {
                next[r * factor % PRIME] += chance[r] / DIGITS as f64;
            }
        }
        chance = next;
    }
    let mut p = vec![0.0f64; DIGITS];
    for r in 0..PRIME {
        p[r % DIGITS] += chance[r];
    }
    // only positive terms are ever added, so an impossible digit stays 0
    if p.iter().any(|&q| q == 0.0) {
        println!("-1");
        return;
    }
    // expected draws from the set of digits seen to all ten: a draw of a
    // missing digit moves on, others repeat; the chance to move on is summed
    // directly so that small probabilities keep their precision
    let full = (1usize << DIGITS) - 1;
    let mut expect = vec![0.0f64; full + 1];
    for mask in (0..full).rev() {
        let (mut moving, mut sum) = (0.0, 1.0);
        for d in 0..DIGITS {
            if mask >> d & 1 == 0 {
                moving += p[d];
                sum += p[d] * expect[mask | 1 << d];
            }
        }
        expect[mask] = sum / moving;
    }
    println!("{:.10}", expect[0]);
}
