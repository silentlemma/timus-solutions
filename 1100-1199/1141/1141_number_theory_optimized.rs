use std::io::{self, BufWriter, Read, Write};

const FIRST_ODD_PRIME: usize = 3;

const MAX_FACTOR: usize = 178;

fn number(input: &mut impl Iterator<Item = u8>) -> i32 {
    let first = input.find(|byte| byte.is_ascii_digit()).unwrap();
    let mut value = i32::from(first - b'0');
    for byte in input.take_while(u8::is_ascii_digit) {
        value = value * 10 + i32::from(byte - b'0');
    }
    value
}

fn inverse(e: i32, phi: i32) -> i32 {
    let (mut a, mut b, mut x, mut y) = (e, phi, 1, 0);
    while b != 0 {
        let q = a / b;
        (a, b) = (b, a - q * b);
        (x, y) = (y, x - q * y);
    }
    x.rem_euclid(phi)
}

fn power(mut base: i32, mut exponent: i32, modulus: i32) -> i32 {
    let mut value = 1;
    base %= modulus;
    while exponent != 0 {
        if exponent & 1 != 0 {
            value = value * base % modulus;
        }
        base = base * base % modulus;
        exponent >>= 1;
    }
    value
}

fn main() {
    let mut composite = [false; MAX_FACTOR + 1];
    let mut primes = [0; MAX_FACTOR / 2];
    let mut count = 0;
    for p in (FIRST_ODD_PRIME..=MAX_FACTOR).step_by(2) {
        if composite[p] {
            continue;
        }
        primes[count] = p as i32;
        count += 1;
        for multiple in (p * p..=MAX_FACTOR).step_by(2 * p) {
            composite[multiple] = true;
        }
    }
    let stdin = io::stdin();
    let mut input = stdin.lock().bytes().map(Result::unwrap);
    let mut out = BufWriter::new(io::stdout().lock());
    for _ in 0..number(&mut input) {
        let (e, n, c) = (number(&mut input), number(&mut input), number(&mut input));
        let p = *primes[..count].iter().find(|&&p| n % p == 0).unwrap();
        let phi = (p - 1) * (n / p - 1);
        writeln!(out, "{}", power(c, inverse(e, phi), n)).unwrap();
    }
    out.flush().unwrap();
}
