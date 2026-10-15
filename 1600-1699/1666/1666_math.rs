use std::io::{self, Read};

const QUARTIC: usize = 5; // coefficients of a degree-4 polynomial
const DISCRIMINANT: i64 = 4; // t^2 - at + e has discriminant a^2 - 4e

/// The positive and negative divisors of v != 0.
fn divisors(v: i64) -> Vec<i64> {
    let v = v.abs();
    let mut out = Vec::new();
    let mut d = 1;
    while d * d <= v {
        if v % d == 0 {
            out.extend([d, -d, v / d, -(v / d)]);
        }
        d += 1;
    }
    out
}

fn value(poly: &[i64], x: i64) -> i64 {
    poly.iter().fold(0, |acc, &c| acc * x + c)
}

/// An integer root of a monic polynomial: it divides the constant term.
fn root(poly: &[i64]) -> Option<i64> {
    let constant = *poly.last().unwrap();
    if constant == 0 {
        return Some(0);
    }
    divisors(constant).into_iter().find(|&d| value(poly, d) == 0)
}

fn exact_root(v: i64) -> i64 {
    let mut s = (v as f64).sqrt() as i64;
    while s * s > v {
        s -= 1;
    }
    while (s + 1) * (s + 1) <= v {
        s += 1;
    }
    s
}

/// (x^2 + px + q)(x^2 + rx + s) with qs = d, p + r = a, q + s + pr = b,
/// ps + qr = c.
fn quadratics(poly: &[i64]) -> Option<(Vec<i64>, Vec<i64>)> {
    let (a, b, c, d) = (poly[1], poly[2], poly[QUARTIC - 2], poly[QUARTIC - 1]);
    for q in divisors(d) {
        let s = d / q;
        let p;
        if q != s {
            if (c - a * q) % (s - q) != 0 {
                continue;
            }
            p = (c - a * q) / (s - q);
        } else {
            // then p and r are the roots of t^2 - at + (b - 2q)
            let disc = a * a - DISCRIMINANT * (b - 2 * q);
            if disc < 0 {
                continue;
            }
            let root = exact_root(disc);
            if root * root != disc || (a + root) % 2 != 0 {
                continue;
            }
            p = (a + root) / 2;
        }
        let r = a - p;
        if q + s + p * r == b && p * s + q * r == c {
            return Some((vec![1, p, q], vec![1, r, s]));
        }
    }
    None
}

fn show(poly: &[i64]) -> String {
    let deg = poly.len() - 1;
    let mut out = String::new();
    for (i, &c) in poly.iter().enumerate() {
        if c == 0 {
            continue;
        }
        let power = deg - i;
        if c < 0 {
            out.push('-');
        } else if !out.is_empty() {
            out.push('+');
        }
        if c.abs() != 1 || power == 0 {
            out.push_str(&c.abs().to_string());
        }
        if power > 0 {
            out.push('x');
        }
        if power > 1 {
            out.push_str(&power.to_string());
        }
    }
    format!("({})", out)
}

fn main() {
    let mut text = String::new();
    io::stdin().read_to_string(&mut text).unwrap();
    let mut poly = vec![1i64];
    poly.extend(text.split_ascii_whitespace().map(|w| w.parse::<i64>().unwrap()));
    let mut factors: Vec<Vec<i64>> = Vec::new();
    while poly.len() > 2 {
        let r = match root(&poly) {
            Some(r) => r,
            None => break,
        };
        factors.push(vec![1, -r]);
        let mut quotient = vec![1i64];
        for &coef in &poly[1..poly.len() - 1] {
            let last = *quotient.last().unwrap();
            quotient.push(coef + r * last);
        }
        poly = quotient;
    }
    if poly.len() == QUARTIC {
        match quadratics(&poly) {
            Some((first, second)) => {
                factors.push(first);
                factors.push(second);
            }
            None => {
                println!("Irreducible");
                return;
            }
        }
    } else if poly.len() > 1 {
        factors.push(poly);
    }
    let out: String = factors.iter().map(|f| show(f)).collect();
    println!("{}", out);
}
