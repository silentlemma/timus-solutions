use std::io;

const FIRST: u32 = 36;
const OTHER: u32 = 55;
const BASE: u32 = 10;

fn main() {
    let mut line = String::new();
    io::stdin().read_line(&mut line).unwrap();
    let k: usize = line.trim().parse().unwrap();
    // no position may carry: 36 pairs of leading digits with a sum of at
    // most 9, and 55 pairs of digits from 0 in every other position
    let mut digits = vec![FIRST % BASE, FIRST / BASE]; // lowest first
    for _ in 1..k {
        let mut carry = 0;
        for d in digits.iter_mut() {
            let v = *d * OTHER + carry;
            *d = v % BASE;
            carry = v / BASE;
        }
        while carry > 0 {
            digits.push(carry % BASE);
            carry /= BASE;
        }
    }
    let text: String = digits
        .iter()
        .rev()
        .map(|&d| char::from_digit(d, BASE).unwrap())
        .collect();
    println!("{}", text);
}
