use std::cmp::Ordering;
use std::io::{self, Read};

// 8 S + 1 = (2 N + 1)^2 for S = N (N + 1) / 2
const EIGHT: u32 = 8;
const BASE: u32 = 10;
// the long-hand root takes the digits in pairs; each step multiplies the
// root so far by twice the base
const PAIR: u32 = BASE * BASE;
const TWICE: u32 = 2 * BASE;

// decimal digits, lowest first, no leading zeros
type Big = Vec<u32>;

fn trim(a: &mut Big) {
    while a.last() == Some(&0) {
        a.pop();
    }
}

fn mul_small(a: &Big, k: u32) -> Big {
    let mut r = Vec::with_capacity(a.len() + 2);
    let mut carry = 0;
    for &d in a {
        let v = d * k + carry;
        r.push(v % BASE);
        carry = v / BASE;
    }
    while carry > 0 {
        r.push(carry % BASE);
        carry /= BASE;
    }
    trim(&mut r);
    r
}

fn add_small(mut a: Big, mut k: u32) -> Big {
    let mut i = 0;
    while k > 0 {
        if i == a.len() {
            a.push(0);
        }
        let v = a[i] + k;
        a[i] = v % BASE;
        k = v / BASE;
        i += 1;
    }
    a
}

fn compare(a: &Big, b: &Big) -> Ordering {
    a.len()
        .cmp(&b.len())
        .then_with(|| a.iter().rev().cmp(b.iter().rev()))
}

fn subtract(mut a: Big, b: &Big) -> Big {
    let mut borrow = 0;
    for i in 0..a.len() {
        let take = borrow + if i < b.len() { b[i] } else { 0 };
        if a[i] < take {
            a[i] = a[i] + BASE - take;
            borrow = 1;
        } else {
            a[i] -= take;
            borrow = 0;
        }
    }
    trim(&mut a);
    a
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut total: Big = input
        .trim()
        .bytes()
        .rev()
        .map(|c| (c - b'0') as u32)
        .collect();
    trim(&mut total);
    let d = add_small(mul_small(&total, EIGHT), 1);
    let mut digits: Vec<u32> = d.iter().rev().copied().collect();
    if digits.len() % 2 == 1 {
        digits.insert(0, 0);
    }
    // the long-hand square root: bring down two digits, then take the largest
    // x with (20 root + x) x not above the remainder
    let (mut root, mut rest): (Big, Big) = (Vec::new(), Vec::new());
    for pair in digits.chunks(2) {
        rest = add_small(mul_small(&rest, PAIR), pair[0] * BASE + pair[1]);
        let twice = mul_small(&root, TWICE);
        let mut x = BASE - 1;
        while x > 0 {
            let take = mul_small(&add_small(twice.clone(), x), x);
            if compare(&take, &rest) != Ordering::Greater {
                rest = subtract(rest, &take);
                break;
            }
            x -= 1;
        }
        root = add_small(mul_small(&root, BASE), x);
    }
    // N = (root - 1) / 2, halved digit by digit from the top
    let root = subtract(root, &vec![1]);
    let mut out = String::new();
    let mut carry = 0;
    for &digit in root.iter().rev() {
        let v = carry * BASE + digit;
        if !out.is_empty() || v / 2 > 0 {
            out.push(char::from_digit(v / 2, BASE).unwrap());
        }
        carry = v % 2;
    }
    println!("{}", if out.is_empty() { "0" } else { &out });
}
