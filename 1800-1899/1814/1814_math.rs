use std::io::{self, Read};

const MOD: u64 = 1_000_000_007;

// a 2 x 2 matrix rows first: a b / c d
#[derive(Clone, Copy)]
struct Matrix {
    a: u64,
    b: u64,
    c: u64,
    d: u64,
}

fn mul(x: &Matrix, y: &Matrix) -> Matrix {
    Matrix {
        a: (x.a * y.a + x.b * y.c) % MOD,
        b: (x.a * y.b + x.b * y.d) % MOD,
        c: (x.c * y.a + x.d * y.c) % MOD,
        d: (x.c * y.b + x.d * y.d) % MOD,
    }
}

// [p_k p_(k-1); q_k q_(k-1)] grows by the factor [a 1; 1 0]
fn term(a: u64) -> Matrix {
    Matrix { a: a % MOD, b: 1, c: 1, d: 0 }
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let v: Vec<u64> = input.split_ascii_whitespace().map(|t| t.parse().unwrap()).collect();
    let (x, k) = (v[0], v[1]);
    let mut a0 = (x as f64).sqrt() as u64;
    while a0 * a0 > x {
        a0 -= 1;
    }
    while (a0 + 1) * (a0 + 1) <= x {
        a0 += 1;
    }
    // the partial quotients of sqrt(x) repeat with a period that ends at
    // the first term equal to 2 a0
    let mut period: Vec<u64> = Vec::new();
    let (mut m, mut d, mut a) = (0u64, 1u64, a0);
    while a != 2 * a0 {
        m = d * a - m;
        d = (x - m * m) / d;
        a = (a0 + m) / d;
        period.push(a);
    }
    let identity = Matrix { a: 1, b: 0, c: 0, d: 1 };
    let cycle = period.iter().fold(identity, |acc, &t| mul(&acc, &term(t)));
    let (mut result, mut power) = (term(a0), cycle);
    let length = period.len() as u64;
    let mut full = k / length;
    while full > 0 {
        if full & 1 == 1 {
            result = mul(&result, &power);
        }
        power = mul(&power, &power);
        full >>= 1;
    }
    for &t in period.iter().take((k % length) as usize) {
        result = mul(&result, &term(t));
    }
    // convergents are always in lowest terms
    println!("{}/{}", result.a, result.c);
}
