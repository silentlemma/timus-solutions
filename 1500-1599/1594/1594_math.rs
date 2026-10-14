use std::io::{self, Read};

const MOD: u64 = 1_000_000_007;

fn power(mut b: u64, mut e: u64) -> u64 {
    let mut r = 1;
    b %= MOD;
    while e > 0 {
        if e & 1 == 1 {
            r = r * b % MOD;
        }
        b = b * b % MOD;
        e >>= 1;
    }
    r
}

/// Monic polynomial, lowest coefficient first, whose roots are
/// 4 cos^2(j pi / (m + 1)) for j = 1 .. ceil(m / 2).
fn roots_poly(m: usize) -> Vec<u64> {
    // S_k(x) = U_k(x / 2) grows by S_(k+1) = x S_k - S_(k-1) from S_0 = 1 and
    // S_1 = x, and its roots are 2 cos(j pi / (m + 1)) for j = 1 .. m
    let (mut prev, mut cur) = (vec![1u64], vec![0u64, 1]);
    for _ in 1..m {
        let mut next = vec![0u64];
        next.extend_from_slice(&cur);
        for (i, &c) in prev.iter().enumerate() {
            next[i] = (next[i] + MOD - c) % MOD;
        }
        prev = cur;
        cur = next;
    }
    // the roots come in pairs +-x, plus 0 when m is odd, so an extra factor x
    // when m is odd makes every power even, and x^2 -> y keeps one per pair
    if m % 2 == 1 {
        cur.insert(0, 0);
    }
    cur.into_iter().step_by(2).collect()
}

fn det(mut a: Vec<Vec<u64>>) -> u64 {
    let size = a.len();
    let mut result = 1;
    for col in 0..size {
        let pivot = match (col..size).find(|&r| a[r][col] != 0) {
            Some(r) => r,
            None => return 0,
        };
        if pivot != col {
            a.swap(pivot, col);
            result = (MOD - result) % MOD;
        }
        result = result * a[col][col] % MOD;
        let inv = power(a[col][col], MOD - 2);
        for r in col + 1..size {
            let f = a[r][col] * inv % MOD;
            if f == 0 {
                continue;
            }
            for c in col..size {
                a[r][c] = (a[r][c] + MOD - f * a[col][c] % MOD) % MOD;
            }
        }
    }
    result
}

/// Res(p, q) as the determinant of the Sylvester matrix.
fn resultant(p: &[u64], q: &[u64]) -> u64 {
    let (d, e) = (p.len() - 1, q.len() - 1);
    let size = d + e;
    let mut rows = vec![vec![0u64; size]; size];
    for i in 0..e {
        for k in 0..=d {
            rows[i][i + k] = p[d - k];
        }
    }
    for i in 0..d {
        for k in 0..=e {
            rows[e + i][i + k] = q[e - k];
        }
    }
    det(rows)
}

fn main() {
    let mut s = String::new();
    io::stdin().read_to_string(&mut s).unwrap();
    let v: Vec<usize> = s
        .split_ascii_whitespace()
        .map(|x| x.parse().unwrap())
        .collect();
    if v.len() < 2 {
        return;
    }
    // Kasteleyn: the number of tilings is the product of a_j + b_k over the
    // roots a_j of roots_poly(m) and b_k of roots_poly(n), which is the
    // resultant of the first with the monic polynomial whose roots are -b_k
    let p = roots_poly(v[0]);
    let mut q = roots_poly(v[1]);
    // (-1)^e q(-y) is monic with roots -b_k: coefficient i gets (-1)^(e - i)
    let e = q.len() - 1;
    for (i, c) in q.iter_mut().enumerate() {
        if (e - i) % 2 == 1 {
            *c = (MOD - *c) % MOD;
        }
    }
    println!("{}", resultant(&p, &q));
}
