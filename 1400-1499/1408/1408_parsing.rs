use std::collections::HashMap;
use std::io::{self, Read};

const LETTERS: usize = 26;

type Powers = [i64; LETTERS];

/// The number of digits starting at pos and the position after it.
fn number(s: &[u8], mut pos: usize) -> (i64, usize) {
    let mut value = 0i64;
    while pos < s.len() && s[pos].is_ascii_digit() {
        value = value * 10 + (s[pos] - b'0') as i64;
        pos += 1;
    }
    (value, pos)
}

/// A polynomial as a map from the powers of a .. z to coefficients.
fn parse(line: &str) -> HashMap<Powers, i64> {
    // spaces may stand anywhere
    let s: Vec<u8> = line.bytes().filter(|c| !c.is_ascii_whitespace()).collect();
    let mut poly = HashMap::new();
    let (mut pos, mut sign) = (0usize, 1i64);
    while pos < s.len() {
        if s[pos] == b'+' || s[pos] == b'-' {
            sign = if s[pos] == b'-' { -1 } else { 1 };
            pos += 1;
        }
        let mut coef = 1i64;
        let mut powers = [0i64; LETTERS];
        loop {
            if s[pos].is_ascii_digit() {
                let (value, next) = number(&s, pos);
                coef *= value;
                pos = next;
            } else {
                let var = (s[pos] - b'a') as usize;
                pos += 1;
                let mut power = 1;
                if pos < s.len() && s[pos] == b'^' {
                    let (value, next) = number(&s, pos + 1);
                    power = value;
                    pos = next;
                }
                powers[var] += power;
            }
            if pos < s.len() && s[pos] == b'*' {
                pos += 1;
            } else {
                break;
            }
        }
        *poly.entry(powers).or_insert(0) += sign * coef;
    }
    poly
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut lines = input.split('\n');
    let first = parse(lines.next().unwrap_or(""));
    let second = parse(lines.next().unwrap_or(""));
    let mut product: HashMap<Powers, i64> = HashMap::new();
    for (p, x) in &first {
        for (q, y) in &second {
            let mut r = [0i64; LETTERS];
            for v in 0..LETTERS {
                r[v] = p[v] + q[v];
            }
            *product.entry(r).or_insert(0) += x * y;
        }
    }
    let mut terms: Vec<(Powers, i64)> = product.into_iter().filter(|t| t.1 != 0).collect();
    // by total degree, then by the powers of a, b, ... from the largest
    terms.sort_by(|l, r| {
        let (sl, sr): (i64, i64) = (l.0.iter().sum(), r.0.iter().sum());
        sr.cmp(&sl).then_with(|| r.0.cmp(&l.0))
    });
    let mut out = String::new();
    for (k, (p, coef)) in terms.iter().enumerate() {
        let mut factors: Vec<String> = Vec::new();
        for (v, &e) in p.iter().enumerate() {
            let name = (b'a' + v as u8) as char;
            if e == 1 {
                factors.push(name.to_string());
            } else if e > 1 {
                factors.push(format!("{}^{}", name, e));
            }
        }
        if coef.abs() != 1 || factors.is_empty() {
            factors.insert(0, coef.abs().to_string());
        }
        let body = factors.join("*");
        let sign = match (k == 0, *coef < 0) {
            (true, true) => "-",
            (true, false) => "",
            (false, true) => " - ",
            (false, false) => " + ",
        };
        out.push_str(sign);
        out.push_str(&body);
    }
    println!("{}", if out.is_empty() { "0" } else { &out });
}
