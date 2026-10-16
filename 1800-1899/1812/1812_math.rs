use std::io::{self, Read};

fn gcd(a: i64, b: i64) -> i64 {
    if b == 0 {
        a
    } else {
        gcd(b, a % b)
    }
}

fn isqrt(v: i64) -> i64 {
    let mut r = (v as f64).sqrt() as i64;
    while r * r > v {
        r -= 1;
    }
    while (r + 1) * (r + 1) <= v {
        r += 1;
    }
    r
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let v: Vec<i64> = input.split_ascii_whitespace().map(|x| x.parse().unwrap()).collect();
    let [r1, r2, n, i] = v[..] else {
        return;
    };
    let pos = i - 1;
    if pos == 0 {
        println!("{}/1", r1);
        return;
    }
    if pos == 1 << n {
        println!("{}/1", r2);
        return;
    }
    // between touching neighbours 1/sqrt(r) adds up, so circle pos has
    // 1/sqrt(r) = a/sqrt(r1) + b/sqrt(r2), with a and b from Stern's sequence
    // found as alpha f(x) + beta f(x + 1) while x is halved level by level
    let (mut alpha, mut beta, mut x) = (1i64, 0i64, pos);
    for _ in 0..n {
        if x % 2 == 0 {
            alpha += beta;
        } else {
            beta += alpha;
        }
        x /= 2;
    }
    // with both a and b positive the radius is rational exactly when
    // r1 = g p^2 and r2 = g q^2 for g = gcd(r1, r2)
    let g = gcd(r1, r2);
    let (p, q) = (isqrt(r1 / g), isqrt(r2 / g));
    if p * p * g != r1 || q * q * g != r2 {
        println!("Irrational");
        return;
    }
    // r = 1 / ((a q + b p) / (p q sqrt(g)))^2
    let d = alpha * q + beta * p;
    let (num, den) = (g * p * p * q * q, d * d);
    let common = gcd(num, den);
    println!("{}/{}", num / common, den / common);
}
