use std::io::{self, Read};

const PRIME: i64 = 1000000007; // independence is decided exactly, modulo this prime
const ZERO_BAND: f64 = 5e-6; // values that print as 0.00000, kept without a minus

fn power(mut base: i64, mut exp: i64) -> i64 {
    let mut result = 1;
    base %= PRIME;
    while exp > 0 {
        if exp & 1 == 1 {
            result = result * base % PRIME;
        }
        base = base * base % PRIME;
        exp >>= 1;
    }
    result
}

/// Indices of a maximal linearly independent subset, found by Gaussian
/// elimination modulo PRIME, so no rounding decides the rank.
fn independent(vectors: &[Vec<i64>]) -> Vec<usize> {
    let mut basis: Vec<(usize, Vec<i64>)> = Vec::new();
    let mut chosen = Vec::new();
    for (k, vec) in vectors.iter().enumerate() {
        let mut row: Vec<i64> = vec.iter().map(|x| x.rem_euclid(PRIME)).collect();
        for (pivot, base) in &basis {
            let f = row[*pivot];
            if f != 0 {
                for (x, y) in row.iter_mut().zip(base) {
                    *x = (*x - f * y).rem_euclid(PRIME);
                }
            }
        }
        if let Some(pivot) = row.iter().position(|&x| x != 0) {
            let inv = power(row[pivot], PRIME - 2);
            for x in row.iter_mut() {
                *x = *x * inv % PRIME;
            }
            basis.push((pivot, row));
            chosen.push(k);
        }
    }
    chosen
}

fn dot(u: &[f64], v: &[f64]) -> f64 {
    u.iter().zip(v).map(|(a, b)| a * b).sum()
}

/// Q and R (by columns) of independent columns: Gram-Schmidt with every
/// projection done twice, which keeps Q orthonormal to rounding error.
fn qr(columns: &[Vec<f64>]) -> (Vec<Vec<f64>>, Vec<Vec<f64>>) {
    let mut q: Vec<Vec<f64>> = Vec::new();
    let mut r = Vec::new();
    for col in columns {
        let mut v = col.clone();
        let mut coef = vec![0.0; q.len()];
        for _ in 0..2 {
            for (k, u) in q.iter().enumerate() {
                let c = dot(u, &v);
                coef[k] += c;
                for (x, y) in v.iter_mut().zip(u) {
                    *x -= c * y;
                }
            }
        }
        let norm = dot(&v, &v).sqrt();
        for x in v.iter_mut() {
            *x /= norm;
        }
        q.push(v);
        coef.push(norm);
        r.push(coef);
    }
    (q, r)
}

fn main() {
    let mut text = String::new();
    io::stdin().read_to_string(&mut text).unwrap();
    let v: Vec<i64> = text.split_ascii_whitespace().map(|w| w.parse().unwrap()).collect();
    let (n, m) = (v[0] as usize, v[1] as usize);
    // engine i pushes along row i; the thrust is the sum of X_i times row i.
    // The shortest best X lies in the span of the columns c_j = (row i at j)_i
    let cols: Vec<Vec<i64>> = (0..n).map(|j| (0..m).map(|i| v[2 + i * n + j]).collect()).collect();
    let real: Vec<Vec<f64>> = cols.iter().map(|c| c.iter().map(|&x| x as f64).collect()).collect();
    let b: Vec<f64> = v[2 + m * n..2 + m * n + n].iter().map(|&x| x as f64).collect();
    let picked: Vec<Vec<f64>> = independent(&cols).into_iter().map(|j| real[j].clone()).collect();
    let (basis, _) = qr(&picked);
    // with X = sum of w_k basis[k], the thrust is K w for K[j][k] = c_j . q_k,
    // and K has full column rank: least squares by QR of K
    let k_cols: Vec<Vec<f64>> =
        basis.iter().map(|u| real.iter().map(|c| dot(c, u)).collect()).collect();
    let (q2, upper) = qr(&k_cols);
    let size = basis.len();
    let mut w = vec![0.0; size];
    for i in (0..size).rev() {
        let mut s = dot(&q2[i], &b);
        for k in i + 1..size {
            s -= upper[k][i] * w[k];
        }
        w[i] = s / upper[i][i];
    }
    let words: Vec<String> = (0..m)
        .map(|i| {
            let x: f64 = (0..size).map(|k| w[k] * basis[k][i]).sum();
            format!("{:.5}", if x.abs() < ZERO_BAND { 0.0 } else { x })
        })
        .collect();
    println!("{}", words.join(" "));
}
