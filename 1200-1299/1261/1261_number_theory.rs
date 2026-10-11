use std::io::{self, Read};

const BASE: u64 = 3;

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut n: u64 = input.trim().parse().unwrap();
    // balanced ternary: digits 1 go into the payment, digits -1 into the tip
    let (mut pay, mut tip, mut power) = (0u64, 0u64, 1u64);
    while n > 0 {
        if n % BASE == 1 {
            pay += power;
            n -= 1;
        } else if n % BASE == BASE - 1 {
            tip += power;
            n += 1;
        }
        n /= BASE;
        power *= BASE;
    }
    // no tip yet: add the smallest bill the payment lacks to both
    power = 1;
    while tip == 0 {
        if pay / power % BASE == 0 {
            pay += power;
            tip = power;
        }
        power *= BASE;
    }
    println!("{} {}", pay, tip);
}
