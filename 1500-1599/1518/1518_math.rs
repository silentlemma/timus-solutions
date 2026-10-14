use std::io::{self, Read};

const HEADER: usize = 3; // N, X and Y come first

// p * q modulo the characteristic polynomial and y, where x^n is the sum of
// x^(n - j) over the steps
fn times(p: &[u64], q: &[u64], steps: &[usize], y: u64) -> Vec<u64> {
    let n = p.len();
    let mut prod = vec![0u64; 2 * n - 1];
    for i in 0..n {
        if p[i] == 0 {
            continue;
        }
        for j in 0..n {
            prod[i + j] = (prod[i + j] + p[i] * q[j]) % y;
        }
    }
    for d in (n..=2 * n - 2).rev() {
        if prod[d] == 0 {
            continue;
        }
        for &j in steps {
            prod[d - j] = (prod[d - j] + prod[d]) % y;
        }
    }
    prod.truncate(n);
    prod
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let v: Vec<u64> = input
        .split_ascii_whitespace()
        .map(|t| t.parse().unwrap())
        .collect();
    let (n, x, y) = (v[0] as usize, v[1], v[2]);
    let keys = &v[HEADER..HEADER + n];
    let shifts = &v[HEADER + n..HEADER + 2 * n];
    // K[i] = sum of K[i - j] * C[n + 1 - j] over j = 1 ... n
    let steps: Vec<usize> = (1..=n).filter(|&j| shifts[n - j] == 1).collect();
    // K[x] is the x - 1 st term counting from K[1], and the coefficients of
    // x^(x - 1) reduced modulo the characteristic polynomial weigh K[1 ... n]
    let mut result = vec![0u64; n];
    let mut base = vec![0u64; n];
    result[0] = 1;
    if n > 1 {
        base[1] = 1;
    } else {
        base[0] = shifts[0] % y;
    }
    let mut e = x - 1;
    while e > 0 {
        if e & 1 == 1 {
            result = times(&result, &base, &steps, y);
        }
        base = times(&base, &base, &steps, y);
        e >>= 1;
    }
    let answer = (0..n).fold(0, |acc, i| (acc + result[i] * (keys[i] % y)) % y);
    println!("{}", answer);
}
