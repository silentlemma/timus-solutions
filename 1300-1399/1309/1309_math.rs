use std::io::{self, Read};

const MOD: i64 = 9973;
const COEF_X: i64 = 3;
const COEF_Y: i64 = 7;

// g(x, y) = y (x^5 - x + 7) + (x^3 + 3x - x^5) is the map y -> a y + b
// modulo 9973, and it depends only on x mod 9973
fn step(x: i64) -> (i64, i64) {
    let x3 = x * x % MOD * x % MOD;
    let x5 = x3 * x % MOD * x % MOD;
    (
        (x5 - x + COEF_Y).rem_euclid(MOD),
        (x3 + COEF_X * x - x5).rem_euclid(MOD),
    )
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let n: i64 = input.trim().parse().unwrap();
    let (whole, rest) = (n / MOD, n % MOD);
    // x = 1 .. 9973 compose into one map, the same for every full period
    let (mut big_a, mut big_b) = (1i64, 0i64);
    for x in 1..=MOD {
        let (a, b) = step(x);
        big_b = (a * big_b + b) % MOD;
        big_a = a * big_a % MOD;
    }
    let mut y = 0i64;
    for _ in 0..whole {
        y = (big_a * y + big_b) % MOD;
    }
    for x in 1..=rest {
        let (a, b) = step(x);
        y = (a * y + b) % MOD;
    }
    println!("{}", y);
}
