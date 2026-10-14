use std::io::{self, Read};

const LETTERS: u64 = 26;

/// A number in base 26, lowest digit first, without high zeros.
type Big = Vec<u64>;

fn trim(x: &mut Big) {
    while x.last() == Some(&0) {
        x.pop();
    }
}

fn mul_add(x: &Big, factor: u64, add: u64) -> Big {
    let mut r = Vec::new();
    let mut carry = add;
    for &d in x {
        carry += d * factor;
        r.push(carry % LETTERS);
        carry /= LETTERS;
    }
    while carry > 0 {
        r.push(carry % LETTERS);
        carry /= LETTERS;
    }
    trim(&mut r);
    r
}

/// The k-th password from 1: by length, then alphabetically, which is k
/// written in bijective base 26 with digits a to z.
fn word(mut k: Big) -> String {
    let mut out = Vec::new();
    while !k.is_empty() {
        // k - 1, then its lowest digit is the letter and the rest goes on
        let mut i = 0;
        while k[i] == 0 {
            k[i] = LETTERS - 1;
            i += 1;
        }
        k[i] -= 1;
        out.push(b'a' + k[0] as u8);
        k.remove(0);
        trim(&mut k);
    }
    out.reverse();
    String::from_utf8(out).unwrap()
}

fn main() {
    let mut s = String::new();
    io::stdin().read_to_string(&mut s).unwrap();
    let v: Vec<u64> = s
        .split_ascii_whitespace()
        .map(|x| x.parse().unwrap())
        .collect();
    let (n, m) = (v[0] as usize, v[1]);
    // 26 + 26^2 + ... + 26^n is 11...10 in base 26
    let mut total = vec![1; n + 1];
    total[0] = 0;
    let mut share = vec![0; total.len()];
    let mut rest = 0;
    for i in (0..total.len()).rev() {
        rest = rest * LETTERS + total[i];
        share[i] = rest / m;
        rest %= m;
    }
    trim(&mut share);
    let extra = rest;
    // the first extra processors take one password more
    let mut out = String::new();
    for i in 0..m {
        let start = mul_add(&share, i, i.min(extra) + 1);
        let end = mul_add(&share, i + 1, (i + 1).min(extra));
        out += &format!("{}-{}\n", word(start), word(end));
    }
    print!("{}", out);
}
