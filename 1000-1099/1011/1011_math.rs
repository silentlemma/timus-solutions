use std::io::{self, Read};

const HUNDREDTHS: i64 = 100;
const WHOLE: i64 = 100 * HUNDREDTHS;

// A percentage with at most two decimals, in hundredths of a percent.
fn hundredths(s: &str) -> i64 {
    let (integer, fraction) = s.split_once('.').unwrap_or((s, ""));
    let integer: i64 = if integer.is_empty() {
        0
    } else {
        integer.parse().unwrap()
    };
    let fraction: String = fraction.chars().chain("00".chars()).take(2).collect();
    integer * HUNDREDTHS + fraction.parse::<i64>().unwrap()
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let v: Vec<i64> = input.split_ascii_whitespace().map(hundredths).collect();
    let (p, q) = (v[0], v[1]);
    // the fewest conductors above p are p*n/WHOLE + 1, and n is the answer
    // as soon as their share is below q
    let mut n = 1;
    while (p * n / WHOLE + 1) * WHOLE >= q * n {
        n += 1;
    }
    println!("{}", n);
}
