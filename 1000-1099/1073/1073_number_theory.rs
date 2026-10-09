use std::io::{self, Read};

// Lagrange: every number is a sum of four squares, and Legendre: exactly the
// numbers 4^a (8b + 7) need all four
const MOST: u32 = 4;
const POWER: u32 = 4;
const MODULUS: u32 = 8;
const REST: u32 = 7;

fn is_square(v: u32) -> bool {
    let r = (v as f64).sqrt().round() as u32;
    r * r == v
}

fn count(mut n: u32) -> u32 {
    if is_square(n) {
        return 1;
    }
    if (1..)
        .take_while(|a| a * a < n)
        .any(|a| is_square(n - a * a))
    {
        return 2;
    }
    while n % POWER == 0 {
        n /= POWER;
    }
    if n % MODULUS == REST {
        MOST
    } else {
        MOST - 1
    }
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    println!("{}", count(input.trim().parse().unwrap()));
}
