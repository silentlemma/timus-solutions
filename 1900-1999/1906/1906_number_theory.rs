use std::io::{self, Read};

const MAX_VALUE: i128 = 1_000_000_000;

fn gcd(mut a: i128, mut b: i128) -> i128 {
    while b != 0 {
        let remainder = a % b;
        a = b;
        b = remainder;
    }
    a.abs()
}

fn extended_gcd(mut a: i128, mut b: i128) -> (i128, i128, i128) {
    let (mut x, mut next_x, mut y, mut next_y) = (1, 0, 0, 1);
    while b != 0 {
        let quotient = a / b;
        (a, b) = (b, a - quotient * b);
        (x, next_x) = (next_x, x - quotient * next_x);
        (y, next_y) = (next_y, y - quotient * next_y);
    }
    (a, x, y)
}

fn largest_modulus(d: i128, e: i128, constraint: i128) -> i128 {
    if e % gcd(d, constraint) == 0 {
        return constraint;
    }
    let common = gcd(constraint, e);
    let mut remaining = constraint / common;
    let forbidden = d / gcd(d, e);
    loop {
        let divisor = gcd(remaining, forbidden);
        if divisor == 1 {
            return common * remaining;
        }
        remaining /= divisor;
    }
}

fn witness(length: usize, d: i128, e: i128, constraint: i128) -> (usize, i128, i128) {
    let modulus = if constraint == 0 {
        d * MAX_VALUE + 1
    } else {
        largest_modulus(d, e, constraint)
    };
    let common = gcd(d, modulus);
    let reduced = modulus / common;
    let multiplier = if reduced == 1 {
        0
    } else {
        let (_, inverse, _) = extended_gcd(d / common, reduced);
        (e / common * inverse).rem_euclid(reduced)
    };
    (length, modulus, multiplier)
}

fn solve(values: &[i128]) -> (usize, i128, i128) {
    let n = values.len();
    if values[0] == 0 {
        return (values.iter().take_while(|&&x| x == 0).count(), 1, 0);
    }
    if n == 1 {
        return (1, values[0] + 1, 0);
    }
    let (mut d, mut e, mut constraint) = (values[0], values[1], 0);
    let mut largest = values[0].max(values[1]);
    let mut length = 2;
    for index in 1..n - 1 {
        let (a, b) = (values[index], values[index + 1]);
        if a == 0 {
            if b != 0 {
                break;
            }
            length = index + 2;
            continue;
        }
        let divisor = gcd(d, a);
        let mut next_e = e;
        if divisor != d {
            let (_, x, y) = extended_gcd(d, a);
            next_e = x * e + y * b;
        }
        let determinant = d / divisor * b - a / divisor * e;
        let next_constraint = gcd(constraint, determinant);
        if next_constraint != 0 {
            next_e = next_e.rem_euclid(next_constraint);
        }
        let next_largest = largest.max(b);
        if next_constraint != 0 && largest_modulus(divisor, next_e, next_constraint) <= next_largest
        {
            break;
        }
        (d, e, constraint) = (divisor, next_e, next_constraint);
        largest = next_largest;
        length = index + 2;
    }
    witness(length, d, e, constraint)
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut tokens = input.split_whitespace().map(|x| x.parse::<i128>().unwrap());
    let count = tokens.next().unwrap() as usize;
    let values: Vec<_> = (0..count).map(|_| tokens.next().unwrap()).collect();
    let (length, modulus, multiplier) = solve(&values);
    println!("{} {} {}", length, modulus, multiplier);
}
