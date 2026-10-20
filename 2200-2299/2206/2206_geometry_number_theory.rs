use std::io::{self, Read};

const SCALE: i64 = 1000;

fn number(token: &str) -> i64 {
    token
        .bytes()
        .filter(|&c| c != b'.')
        .fold(0, |value, c| value * 10 + i64::from(c - b'0'))
}

fn main() {
    let mut data = String::new();
    io::stdin().read_to_string(&mut data).unwrap();
    let mut tokens = data.split_whitespace();
    let n = number(tokens.next().unwrap()) as usize;
    let points: Vec<(i64, i64)> = (0..n)
        .map(|_| {
            (
                number(tokens.next().unwrap()),
                number(tokens.next().unwrap()),
            )
        })
        .collect();
    let left = ((points.iter().map(|p| p.0).min().unwrap() + SCALE - 1) / SCALE) as usize;
    let right = (points.iter().map(|p| p.0).max().unwrap() / SCALE) as usize;
    if left > right {
        println!("0");
        return;
    }
    let mut lower = vec![0_i64; right + 1];
    let mut upper = vec![0_i64; right + 1];
    for i in 0..n {
        let (mut a, mut b) = (points[i], points[(i + 1) % n]);
        if a.0 == b.0 {
            continue;
        }
        let bottom = a.0 < b.0;
        if !bottom {
            std::mem::swap(&mut a, &mut b);
        }
        let begin = ((a.0 + SCALE - 1) / SCALE) as usize;
        let end = (b.0 / SCALE) as usize;
        let (dx, dy) = (b.0 - a.0, b.1 - a.1);
        let denominator = dx * SCALE;
        let mut numerator = a.1 * dx + (begin as i64 * SCALE - a.0) * dy;
        if bottom {
            numerator -= 1;
        }
        let target = if bottom { &mut lower } else { &mut upper };
        for value in target.iter_mut().take(end + 1).skip(begin) {
            *value = numerator / denominator;
            numerator += dy * SCALE;
        }
    }
    let limit = right.min(*upper.iter().max().unwrap() as usize);
    let mut mu = vec![1_i64; limit + 1];
    let mut composite = vec![false; limit + 1];
    for prime in 2..=limit {
        if composite[prime] {
            continue;
        }
        for multiple in (prime..=limit).step_by(prime) {
            composite[multiple] = true;
            mu[multiple] = -mu[multiple];
        }
        let square = prime * prime;
        for multiple in (square..=limit).step_by(square) {
            mu[multiple] = 0;
        }
    }
    let mut answer = 0_i64;
    for (divisor, &sign) in mu.iter().enumerate().skip(1) {
        if sign == 0 {
            continue;
        }
        let begin = ((left + divisor - 1) / divisor) * divisor;
        let mut subtotal = 0_i64;
        for column in (begin..=right).step_by(divisor) {
            subtotal += upper[column] / divisor as i64 - lower[column] / divisor as i64;
        }
        answer += sign * subtotal;
    }
    println!("{}", answer);
}
