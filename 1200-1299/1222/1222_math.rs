use std::io;

const THREE: u32 = 3;
const FOUR: u32 = 4;
const BASE: u32 = 10;

fn main() {
    let mut line = String::new();
    io::stdin().read_line(&mut line).unwrap();
    let n: u32 = line.trim().parse().unwrap();
    // threes are best: a 4 or more splits into parts with a larger product, and
    // three 2s lose to two 3s; a leftover 1 joins a 3 to make 2 + 2
    if n < FOUR {
        println!("{}", n);
        return;
    }
    let (mut threes, mut rest) = (n / THREE, n % THREE);
    if rest == 1 {
        threes -= 1;
        rest = FOUR;
    }
    let mut digits = vec![rest.max(1)]; // lowest first
    for _ in 0..threes {
        let mut carry = 0;
        for d in digits.iter_mut() {
            let v = *d * THREE + carry;
            *d = v % BASE;
            carry = v / BASE;
        }
        if carry > 0 {
            digits.push(carry);
        }
    }
    let text: String = digits
        .iter()
        .rev()
        .map(|&d| char::from_digit(d, BASE).unwrap())
        .collect();
    println!("{}", text);
}
