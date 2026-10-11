use std::io::{self, Read};

// "-7 3/4", "-7/11" or "11" as a numerator and denominator
fn parse(line: &str) -> (i64, i64) {
    let line = line.trim();
    let sign = if line.starts_with('-') { -1 } else { 1 };
    let (mut whole, mut num, mut den) = (0i64, 0i64, 1i64);
    for token in line.trim_start_matches('-').split_whitespace() {
        if let Some((n, d)) = token.split_once('/') {
            num = n.parse().unwrap();
            den = d.parse().unwrap();
        } else {
            whole = token.parse().unwrap();
        }
    }
    (sign * (whole * den + num), den)
}

fn gcd(a: i64, b: i64) -> i64 {
    if b == 0 {
        a
    } else {
        gcd(b, a % b)
    }
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let lines: Vec<&str> = input.lines().collect();
    let (an, ad) = parse(lines[0]);
    let (bn, bd) = parse(lines[2]);
    let (mut num, mut den) = match lines[1].trim() {
        "+" => (an * bd + bn * ad, ad * bd),
        "-" => (an * bd - bn * ad, ad * bd),
        "*" => (an * bn, ad * bd),
        _ => (an * bd, ad * bn),
    };
    if den < 0 {
        num = -num;
        den = -den;
    }
    let sign = if num < 0 { "-" } else { "" };
    num = num.abs();
    let g = gcd(num, den);
    let (num, den) = (num / g, den / g);
    let (whole, rest) = (num / den, num % den);
    if rest == 0 {
        println!("{}{}", sign, whole);
    } else if whole == 0 {
        println!("{}{}/{}", sign, rest, den);
    } else {
        println!("{}{} {}/{}", sign, whole, rest, den);
    }
}
