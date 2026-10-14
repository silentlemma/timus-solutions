use std::io::{self, Read};

/// Non-negative big numbers as base-10^9 digits, lowest first.
type Big = Vec<u64>;
const BASE: u64 = 1_000_000_000;

fn trim(a: &mut Big) {
    while a.len() > 1 && *a.last().unwrap() == 0 {
        a.pop();
    }
}

fn mul_small(a: &mut Big, s: u64) {
    let mut carry = 0;
    for d in a.iter_mut() {
        let cur = *d * s + carry;
        *d = cur % BASE;
        carry = cur / BASE;
    }
    while carry > 0 {
        a.push(carry % BASE);
        carry /= BASE;
    }
    trim(a);
}

/// The quotient of a by s, and the remainder.
fn div_small(a: &Big, s: u64) -> (Big, u64) {
    let mut q = a.clone();
    let mut rem = 0;
    for d in q.iter_mut().rev() {
        let cur = rem * BASE + *d;
        *d = cur / s;
        rem = cur % s;
    }
    trim(&mut q);
    (q, rem)
}

fn add_to(a: &mut Big, b: &Big) {
    let mut carry = 0;
    let mut i = 0;
    while i < b.len() || carry > 0 {
        if i == a.len() {
            a.push(0);
        }
        let cur = a[i] + carry + b.get(i).copied().unwrap_or(0);
        a[i] = cur % BASE;
        carry = cur / BASE;
        i += 1;
    }
}

/// a - b for a >= b.
fn sub_from(a: &mut Big, b: &Big) {
    let mut borrow = 0;
    for i in 0..a.len() {
        let take = b.get(i).copied().unwrap_or(0) + borrow;
        if a[i] >= take {
            a[i] -= take;
            borrow = 0;
        } else {
            a[i] = a[i] + BASE - take;
            borrow = 1;
        }
    }
    trim(a);
}

fn show(a: &Big) -> String {
    let mut s = a.last().unwrap().to_string();
    for d in a.iter().rev().skip(1) {
        s.push_str(&format!("{:09}", d));
    }
    s
}

fn main() {
    let mut text = String::new();
    io::stdin().read_to_string(&mut text).unwrap();
    let v: Vec<i64> = text.split_ascii_whitespace().map(|w| w.parse().unwrap()).collect();
    let (n, m, k) = (v[0], v[1], v[2]);
    // each flip moves the expectation to E (1 - 2/n) + 1, so after k flips
    // E = n/2 + (m - n/2) ((n - 2)/n)^k = (n^(k+1) + (2m - n)(n - 2)^k) / (2 n^k)
    let mut num: Big = vec![1];
    for _ in 0..=k {
        mul_small(&mut num, n as u64);
    }
    let (first, ratio) = (2 * m - n, n - 2);
    let mut tail: Big = vec![first.unsigned_abs()];
    for _ in 0..k {
        mul_small(&mut tail, ratio.unsigned_abs());
    }
    if (first < 0) != (ratio < 0 && k % 2 == 1) {
        sub_from(&mut num, &tail); // the expectation is never negative
    } else {
        add_to(&mut num, &tail);
    }
    if num == vec![0] {
        println!("0/1");
        return;
    }
    // the denominator 2 n^k as primes and powers; only these can divide num
    let mut den: Vec<(u64, i64)> = Vec::new();
    let mut rest = 2 * n;
    let mut p = 2;
    while p * p <= rest {
        if rest % p == 0 {
            let mut e = 0;
            while rest % p == 0 {
                rest /= p;
                e += 1;
            }
            den.push((p as u64, e));
        }
        p += 1;
    }
    if rest > 1 {
        den.push((rest as u64, 1));
    }
    for (p, e) in den.iter_mut() {
        let two = (*p == 2) as i64;
        *e = (*e - two) * k + two; // the exponent in 2 n^k
        while *e > 0 {
            let (q, rem) = div_small(&num, *p);
            if rem != 0 {
                break;
            }
            num = q;
            *e -= 1;
        }
    }
    let mut rest_den: Big = vec![1];
    for &(p, e) in &den {
        for _ in 0..e {
            mul_small(&mut rest_den, p);
        }
    }
    println!("{}/{}", show(&num), show(&rest_den));
}
