use std::io::{self, Read};

const POSITIONS: usize = 32;

// how many numbers in [0, n] are sums of exactly k different powers of b,
// that is, have only digits 0 and 1 in base b with k ones
fn count_upto(mut n: i64, k: usize, b: i64, binom: &[Vec<i64>]) -> i64 {
    let mut digits = Vec::new();
    while n > 0 {
        digits.push(n % b);
        n /= b;
    }
    // a digit above 1 lets every smaller number with 0/1 digits through: it
    // and all digits after it may as well be 1
    if let Some(i) = (0..digits.len()).rev().find(|&i| digits[i] > 1) {
        for d in digits.iter_mut().take(i + 1) {
            *d = 1;
        }
    }
    // count 0/1 strings with k ones not above the digits, from the top
    let mut total = 0;
    let mut ones = 0;
    for i in (0..digits.len()).rev() {
        if ones > k {
            break;
        }
        if digits[i] == 1 {
            if k - ones <= i {
                total += binom[i][k - ones];
            }
            ones += 1;
        }
    }
    total + if ones == k { 1 } else { 0 }
}

fn main() {
    let mut binom = vec![vec![0i64; POSITIONS + 1]; POSITIONS + 1];
    for i in 0..=POSITIONS {
        binom[i][0] = 1;
        for j in 1..=i {
            binom[i][j] = binom[i - 1][j - 1] + if j < i { binom[i - 1][j] } else { 0 };
        }
    }
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let v: Vec<i64> = input
        .split_ascii_whitespace()
        .map(|t| t.parse().unwrap())
        .collect();
    let (x, y) = (v[0], v[1]);
    let (k, b) = (v[2] as usize, v[v.len() - 1]);
    println!(
        "{}",
        count_upto(y, k, b, &binom) - count_upto(x - 1, k, b, &binom)
    );
}
