use std::io::{self, Read};

fn gcd(mut a: i64, mut b: i64) -> i64 {
    while b != 0 {
        (a, b) = (b, a % b);
    }
    a
}

fn inverse(value: i64, modulus: i64) -> i64 {
    if modulus == 1 {
        return 0;
    }
    let (mut old_r, mut r) = (value, modulus);
    let (mut old_coefficient, mut coefficient) = (1, 0);
    while r != 0 {
        let quotient = old_r / r;
        (old_r, r) = (r, old_r - quotient * r);
        (old_coefficient, coefficient) = (coefficient, old_coefficient - quotient * coefficient);
    }
    old_coefficient.rem_euclid(modulus)
}

fn visits(a: i64, b: i64, x: i64, y: i64, n: i64) -> i64 {
    if x <= a || y <= b {
        return n;
    }
    let (bread_divisor, sausage_divisor) = (gcd(x, a), gcd(y, b));
    let (bread_period, bread_count) = (x / bread_divisor, a / bread_divisor);
    let (sausage_period, sausage_count) = (y / sausage_divisor, b / sausage_divisor);
    let common_divisor = gcd(bread_period, sausage_period);
    let modulus = sausage_period / common_divisor;
    let coefficient = inverse(bread_period / common_divisor, modulus);
    let period = bread_period * modulus;
    let mut answer = (n * a + x - 1) / x + (n * b + y - 1) / y;

    // Each ingredient has a few purchase residues in its repeating period.
    for i in 0..bread_count {
        let bread_residue = i * bread_period / bread_count;
        for j in 0..sausage_count {
            let sausage_residue = j * sausage_period / sausage_count;
            let difference = sausage_residue - bread_residue;
            if difference % common_divisor != 0 {
                continue;
            }
            // CRT gives the first simultaneous purchase for this residue pair.
            let step = (difference / common_divisor * coefficient).rem_euclid(modulus);
            let first = bread_residue + bread_period * step;
            if first < n {
                answer -= 1 + (n - 1 - first) / period;
            }
        }
    }
    answer
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut numbers = input.split_whitespace().map(|value| value.parse().unwrap());
    let a = numbers.next().unwrap();
    let b = numbers.next().unwrap();
    let x = numbers.next().unwrap();
    let y = numbers.next().unwrap();
    let n = numbers.next().unwrap();
    println!("{}", visits(a, b, x, y, n));
}
