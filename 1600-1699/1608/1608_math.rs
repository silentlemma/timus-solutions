use std::io::{self, Read};

const DIGITS: u64 = 10;
const PAIR: u64 = DIGITS * (DIGITS - 1); // two free mirrored digits that differ

/// Lucky numbers of this length that start with these digits.
fn complete(prefix: &[u64], length: usize) -> u64 {
    let mut ways = 1;
    let fixed = prefix.len();
    for i in 0..(length + 1) / 2 {
        let j = length - 1 - i;
        if i == j {
            if i >= fixed {
                ways *= DIGITS;
            }
        } else if j < fixed {
            if prefix[i] == prefix[j] {
                return 0;
            }
        } else if i < fixed {
            ways *= DIGITS - 1; // the partner must differ from the fixed digit
        } else {
            ways *= PAIR;
        }
    }
    ways
}

/// Lucky tickets numbered 1 .. n.
fn lucky_up_to(n: u64) -> u64 {
    if n == 0 {
        return 0;
    }
    let digits: Vec<u64> = n.to_string().bytes().map(|c| (c - b'0') as u64).collect();
    let length = digits.len();
    let mut total = 0;
    // all shorter numbers, by their first digit
    for k in 1..length {
        for d in 1..DIGITS {
            total += complete(&[d], k);
        }
    }
    // same length: the first position where the number drops below n
    for k in 0..length {
        let mut prefix = digits[..k].to_vec();
        prefix.push(0);
        let start = if k == 0 { 1 } else { 0 };
        for d in start..digits[k] {
            prefix[k] = d;
            total += complete(&prefix, length);
        }
    }
    total + complete(&digits, length)
}

fn main() {
    let mut s = String::new();
    io::stdin().read_to_string(&mut s).unwrap();
    let v: Vec<u64> = s
        .split_ascii_whitespace()
        .map(|x| x.parse().unwrap())
        .collect();
    if let [a, b] = v[..] {
        println!("{}", lucky_up_to(b) - lucky_up_to(a - 1));
    }
}
