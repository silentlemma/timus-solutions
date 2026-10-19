use std::io::{self, Read};

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let v: Vec<i64> = input.split_ascii_whitespace().map(|t| t.parse().unwrap()).collect();
    if v.is_empty() {
        return;
    }
    let n = v[0];
    // least squares line through the points (i, a_i), i = 0 .. n - 1:
    // the normal equations give the step and then the first term
    let sum_x = n * (n - 1) / 2;
    let (mut sum_xx, mut sum_a, mut sum_xa) = (0i64, 0i64, 0i64);
    for (i, &a) in v[1..=n as usize].iter().enumerate() {
        let i = i as i64;
        sum_xx += i * i;
        sum_a += a;
        sum_xa += i * a;
    }
    let step = (n * sum_xa - sum_x * sum_a) as f64 / (n * sum_xx - sum_x * sum_x) as f64;
    let first = (sum_a as f64 - step * sum_x as f64) / n as f64;
    println!("{:.9} {:.9}", first, step);
}
