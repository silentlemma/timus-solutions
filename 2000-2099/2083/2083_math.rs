use std::collections::HashMap;
use std::io::{self, Read, Write};

const SHORT: usize = 32; // cycles up to this length are summed directly
const MODS: [u64; 3] = [998244353, 167772161, 469762049]; // NTT primes, root 3
const ROOT: u64 = 3;
const SPAN: usize = 3; // a product of L and 2L numbers has fewer than 3L

fn power(mut b: u64, mut e: u64, m: u64) -> u64 {
    let mut r = 1;
    b %= m;
    while e > 0 {
        if e & 1 == 1 {
            r = r * b % m;
        }
        b = b * b % m;
        e >>= 1;
    }
    r
}

fn ntt(a: &mut [u64], invert: bool, m: u64) {
    let n = a.len();
    let mut j = 0;
    for i in 1..n {
        let mut bit = n >> 1;
        while j & bit != 0 {
            j ^= bit;
            bit >>= 1;
        }
        j ^= bit;
        if i < j {
            a.swap(i, j);
        }
    }
    let mut len = 2;
    while len <= n {
        let mut w = power(ROOT, (m - 1) / len as u64, m);
        if invert {
            w = power(w, m - 2, m);
        }
        let half = len / 2;
        for i in (0..n).step_by(len) {
            let mut wn = 1;
            for k in 0..half {
                let (u, v) = (a[i + k], a[i + k + half] * wn % m);
                a[i + k] = (u + v) % m;
                a[i + k + half] = (u + m - v) % m;
                wn = wn * w % m;
            }
        }
        len <<= 1;
    }
    if invert {
        let inv = power(n as u64, m - 2, m);
        for x in a.iter_mut() {
            *x = *x * inv % m;
        }
    }
}

// out[s] = sum over r of fold[r] * cycle[(s + r) mod L]; every sum is below 2^63
fn cyclic(fold: &[u64], cycle: &[u64]) -> Vec<u64> {
    let size = cycle.len();
    if size <= SHORT {
        return (0..size)
            .map(|s| (0..size).map(|r| fold[r] * cycle[(s + r) % size]).sum())
            .collect();
    }
    // reversed fold times the cycle written twice, modulo three primes,
    // put together by Garner's method; wrapping 64-bit arithmetic is exact here
    let mut n = 1;
    while n < SPAN * size {
        n <<= 1;
    }
    let residue: Vec<Vec<u64>> = MODS
        .iter()
        .map(|&m| {
            let mut a = vec![0u64; n];
            let mut b = vec![0u64; n];
            for r in 0..size {
                a[size - 1 - r] = fold[r] % m;
            }
            for i in 0..2 * size {
                b[i] = cycle[i % size] % m;
            }
            ntt(&mut a, false, m);
            ntt(&mut b, false, m);
            for i in 0..n {
                a[i] = a[i] * b[i] % m;
            }
            ntt(&mut a, true, m);
            a
        })
        .collect();
    let (m0, m1, m2) = (MODS[0], MODS[1], MODS[2]);
    let (inv01, inv012) = (power(m0 % m1, m1 - 2, m1), power(m0 * m1 % m2, m2 - 2, m2));
    (0..size)
        .map(|s| {
            let i = s + size - 1;
            let x0 = residue[0][i];
            let x1 = (residue[1][i] + m1 - x0 % m1) % m1 * inv01 % m1;
            let low = (x0 + x1 * m0) % m2;
            let x2 = (residue[2][i] + m2 - low) % m2 * inv012 % m2;
            x0.wrapping_add(x1 * m0).wrapping_add(x2.wrapping_mul(m0 * m1))
        })
        .collect()
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let v: Vec<u64> = input.split_ascii_whitespace().map(|t| t.parse().unwrap()).collect();
    let (m, n) = (v[0] as usize, v[1] as usize);
    let p: Vec<usize> = v[2..2 + n].iter().map(|&x| x as usize - 1).collect();
    let mut by_year = vec![0u64; m + 1]; // by_year[t] = q_t
    by_year[1..].copy_from_slice(&v[2 + n..2 + n + m]);
    // the year t row is p applied t times, so the answer at j is the sum of
    // q_t p^t(j); along a cycle of p this is a cyclic correlation
    let mut answer = vec![0u64; n];
    let mut seen = vec![false; n];
    let mut folds: HashMap<usize, Vec<u64>> = HashMap::new(); // cycle length -> remainder sums
    for start in 0..n {
        if seen[start] {
            continue;
        }
        let mut cycle = Vec::new();
        let mut j = start;
        while !seen[j] {
            seen[j] = true;
            cycle.push(j);
            j = p[j];
        }
        let size = cycle.len();
        let fold = folds.entry(size).or_insert_with(|| {
            let mut f = vec![0u64; size];
            for t in 1..=m {
                f[t % size] += by_year[t];
            }
            f
        });
        let values: Vec<u64> = cycle.iter().map(|&c| c as u64 + 1).collect();
        for (s, value) in cyclic(fold, &values).into_iter().enumerate() {
            answer[cycle[s]] = value;
        }
    }
    let text: Vec<String> = answer.iter().map(|x| x.to_string()).collect();
    io::stdout().write_all((text.join(" ") + "\n").as_bytes()).unwrap();
}
