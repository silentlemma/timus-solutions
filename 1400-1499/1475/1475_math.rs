use std::cmp::Ordering;
use std::io::{self, Read, Write};

/// Non-negative integers as 32-bit limbs, the lowest first, without leading zeros.
type Big = Vec<u32>;

const LIMB: u32 = 32;
const BASE: u64 = 10;
const CHUNK: u64 = 1_000_000_000;
const SPEED: u64 = 4; // bounces k come at 4 h sin(a) k (k + 1) down the slope

fn trim(a: &mut Big) {
    while a.last() == Some(&0) {
        a.pop();
    }
}

fn parse(s: &str) -> Big {
    let mut a = Big::new();
    for d in s.bytes() {
        let mut carry = (d - b'0') as u64;
        for x in a.iter_mut() {
            let v = *x as u64 * BASE + carry;
            *x = v as u32;
            carry = v >> LIMB;
        }
        if carry > 0 {
            a.push(carry as u32);
        }
    }
    a
}

fn mul(a: &Big, b: &Big) -> Big {
    let mut r = vec![0u32; a.len() + b.len()];
    for (i, &x) in a.iter().enumerate() {
        let mut carry = 0u64;
        for (j, &y) in b.iter().enumerate() {
            let v = x as u64 * y as u64 + r[i + j] as u64 + carry;
            r[i + j] = v as u32;
            carry = v >> LIMB;
        }
        r[i + b.len()] = carry as u32;
    }
    trim(&mut r);
    r
}

fn add(a: &Big, b: &Big) -> Big {
    let n = a.len().max(b.len());
    let mut r = vec![0u32; n + 1];
    let mut carry = 0u64;
    for i in 0..n {
        let v = carry + *a.get(i).unwrap_or(&0) as u64 + *b.get(i).unwrap_or(&0) as u64;
        r[i] = v as u32;
        carry = v >> LIMB;
    }
    r[n] = carry as u32;
    trim(&mut r);
    r
}

fn compare(a: &Big, b: &Big) -> Ordering {
    a.len()
        .cmp(&b.len())
        .then_with(|| a.iter().rev().cmp(b.iter().rev()))
}

fn bits(a: &Big) -> usize {
    match a.last() {
        None => 0,
        Some(&x) => (a.len() - 1) * LIMB as usize + (LIMB - x.leading_zeros()) as usize,
    }
}

fn text(mut a: Big) -> String {
    let mut chunks = Vec::new();
    while !a.is_empty() {
        let mut rem = 0u64;
        for x in a.iter_mut().rev() {
            let cur = (rem << LIMB) | *x as u64;
            *x = (cur / CHUNK) as u32;
            rem = cur % CHUNK;
        }
        trim(&mut a);
        chunks.push(rem);
    }
    let mut s = chunks.pop().unwrap_or(0).to_string();
    for c in chunks.iter().rev() {
        s.push_str(&format!("{:09}", c));
    }
    s
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut it = input.split_ascii_whitespace();
    let t: usize = it.next().unwrap().parse().unwrap();
    let one: Big = vec![1];
    let mut out = String::new();
    for _ in 0..t {
        let height = parse(it.next().unwrap());
        let run = parse(it.next().unwrap());
        let drop: u64 = it.next().unwrap().parse().unwrap();
        // the largest k with SPEED * drop * height * k (k + 1) <= run^2 + height^2,
        // set bit by bit from the highest one k can have
        let x = add(&mul(&run, &run), &mul(&height, &height));
        let y = mul(&height, &vec![(SPEED * drop) as u32]);
        let mut k = Big::new();
        let top = (bits(&x) as i64 - bits(&y) as i64).max(0) as usize / 2 + 1;
        for b in (0..=top).rev() {
            let mut c = k.clone();
            let limb = b / LIMB as usize;
            if c.len() <= limb {
                c.resize(limb + 1, 0);
            }
            c[limb] |= 1 << (b % LIMB as usize);
            if compare(&mul(&mul(&c, &add(&c, &one)), &y), &x) != Ordering::Greater {
                k = c;
            }
        }
        out.push_str(&text(add(&k, &one)));
        out.push('\n');
    }
    io::stdout().write_all(out.as_bytes()).unwrap();
}
