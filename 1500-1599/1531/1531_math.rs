use std::io::{self, Read};

const BASE: u32 = 10;
const ODD: u32 = 3; // the factor of the power of two for odd n
const LESS: u32 = 4; // every count is that power times 1 or ODD, minus LESS

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let n: u32 = input.trim().parse().unwrap();
    if n == 1 {
        println!("1");
        return;
    }
    // the counts of polygons grow by 4, 4, 8, 8, 16, 16, ... from zone 3 on:
    // 2^(n / 2 + 2) - 4 for even n and 3 * 2^(n / 2 + 1) - 4 for odd n
    let mut digits: Vec<u32> = vec![if n % 2 == 0 { 1 } else { ODD }]; // the lowest first
    for _ in 0..n / 2 + 2 - n % 2 {
        let mut carry = 0;
        for d in digits.iter_mut() {
            let v = *d * 2 + carry;
            *d = v % BASE;
            carry = v / BASE;
        }
        if carry > 0 {
            digits.push(carry);
        }
    }
    // subtract LESS; the number is at least 8, so the borrow stops early
    let mut sub = LESS;
    for d in digits.iter_mut() {
        if *d >= sub {
            *d -= sub;
            break;
        }
        *d = *d + BASE - sub;
        sub = 1;
    }
    while digits.len() > 1 && digits[digits.len() - 1] == 0 {
        digits.pop();
    }
    let text: String = digits
        .iter()
        .rev()
        .map(|d| char::from(b'0' + *d as u8))
        .collect();
    println!("{}", text);
}
