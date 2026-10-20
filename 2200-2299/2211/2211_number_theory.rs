use std::io::{self, Read};

const MIN_SUM_FACTOR: u64 = 3;
const QUADRATIC_FACTOR: u64 = 4;
const AREA_MULTIPLE: u64 = 6;

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let area: u64 = input.trim().parse().unwrap();
    if area % AREA_MULTIPLE != 0 {
        println!("0");
        return;
    }
    let mut divisors = vec![1_u64];
    let mut remaining = area;
    let mut prime = 2;
    while prime * prime <= remaining {
        let mut exponent = 0;
        while remaining % prime == 0 {
            remaining /= prime;
            exponent += 2;
        }
        let size = divisors.len();
        let mut power = 1;
        for _ in 0..exponent {
            power *= prime;
            for i in 0..size {
                divisors.push(divisors[i] * power);
            }
        }
        prime += if prime == 2 { 1 } else { 2 };
    }
    if remaining > 1 {
        let size = divisors.len();
        for i in 0..size {
            divisors.push(divisors[i] * remaining);
            divisors.push(divisors[i] * remaining * remaining);
        }
    }
    divisors.sort_unstable();
    let square = area * area;
    let mut answer = 0_u64;
    // Heron's variables satisfy x <= y <= z and xyz(x + y + z) = area squared.
    for (i, &x) in divisors.iter().enumerate() {
        if x > square / x / x / x / MIN_SUM_FACTOR {
            break;
        }
        remaining = square / x;
        let mut left = i;
        let mut right = divisors.len();
        while left < right {
            let middle = (left + right) / 2;
            let y = divisors[middle];
            if y <= remaining / y / (x + 2 * y) {
                left = middle + 1;
            } else {
                right = middle;
            }
        }
        for &y in &divisors[i..left] {
            if remaining % y != 0 {
                continue;
            }
            let total = x + y;
            let discriminant = total * total + QUADRATIC_FACTOR * (remaining / y);
            let mut root = (discriminant as f64).sqrt() as u64;
            while root * root > discriminant {
                root -= 1;
            }
            while (root + 1) * (root + 1) <= discriminant {
                root += 1;
            }
            if root * root == discriminant && (root - total) % 2 == 0 {
                answer += 1;
            }
        }
    }
    println!("{}", answer);
}
