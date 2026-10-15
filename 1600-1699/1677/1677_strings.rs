use std::fmt::Write as _;
use std::io::{self, Read};

const LIMB: u64 = 1_000_000_000; // the big number is kept in base 10^9

/// total = total * mul + add, on limbs stored lowest first.
fn times_plus(total: &mut Vec<u64>, mul: u64, add: u64) {
    let mut carry = add;
    for limb in total.iter_mut() {
        let cur = *limb * mul + carry;
        *limb = cur % LIMB;
        carry = cur / LIMB;
    }
    while carry > 0 {
        total.push(carry % LIMB);
        carry /= LIMB;
    }
}

fn main() {
    let mut text = String::new();
    io::stdin().read_to_string(&mut text).unwrap();
    let mut it = text.split_ascii_whitespace();
    let n: u64 = it.next().unwrap().parse().unwrap();
    let word = it.next().unwrap().as_bytes();
    let size = word.len();
    // prefix function: pi[i] is the longest border of word[..=i]
    let mut pi = vec![0usize; size];
    for i in 1..size {
        let mut j = pi[i - 1];
        while j > 0 && word[i] != word[j] {
            j = pi[j - 1];
        }
        if word[i] == word[j] {
            j += 1;
        }
        pi[i] = j;
    }
    // the expected time is the sum of n^k over the lengths k of the word's
    // borders, the whole word included: a number whose base-n digits are 0
    // and 1, built by Horner's rule from the top digit down
    let mut border = vec![0u64; size + 1];
    let mut k = size;
    while k > 0 {
        border[k] = 1;
        k = pi[k - 1];
    }
    let mut total = vec![0u64];
    for k in (1..=size).rev() {
        times_plus(&mut total, n, border[k]);
    }
    times_plus(&mut total, n, 0);
    let mut out = total.last().unwrap().to_string();
    for limb in total.iter().rev().skip(1) {
        write!(out, "{:09}", limb).unwrap();
    }
    println!("{}", out);
}
