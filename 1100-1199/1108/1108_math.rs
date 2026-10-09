use std::fmt::Write;
use std::io::{self, Read};

// a big number as base 10^9 digits, least significant first
const BASE: u64 = 1_000_000_000;

fn next_term(a: &[u64]) -> Vec<u64> {
    let mut less = a.to_vec();
    // a is at least 2 and odd from the second term on
    less[0] -= 1;
    let mut res = vec![0u64; a.len() * 2 + 1];
    for (i, &x) in a.iter().enumerate() {
        let mut carry = 0;
        let mut j = 0;
        while j < less.len() || carry > 0 {
            let prod = if j < less.len() { x * less[j] } else { 0 };
            let cur = res[i + j] + carry + prod;
            res[i + j] = cur % BASE;
            carry = cur / BASE;
            j += 1;
        }
    }
    // the product is even, so its lowest digit is below BASE - 1
    res[0] += 1;
    while res.len() > 1 && *res.last().unwrap() == 0 {
        res.pop();
    }
    res
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let n: usize = input.trim().parse().unwrap();
    let mut a = vec![2u64];
    let mut out = String::new();
    for _ in 0..n {
        write!(out, "{}", a.last().unwrap()).unwrap();
        for d in a.iter().rev().skip(1) {
            write!(out, "{:09}", d).unwrap();
        }
        out.push('\n');
        // after the shares 1/a(1) .. 1/a(k) the remainder is 1/(a(k+1) - 1), and the
        // largest share that still leaves something is 1/a(k+1)
        a = next_term(&a);
    }
    print!("{}", out);
}
