use std::io::{self, Read};

const SIZE: usize = 4;
const BASE: u64 = 10;

type Matrix = [[u64; SIZE]; SIZE];

fn multiply(a: &Matrix, b: &Matrix, m: u64) -> Matrix {
    let mut c = [[0u64; SIZE]; SIZE];
    for i in 0..SIZE {
        for k in 0..SIZE {
            for j in 0..SIZE {
                c[i][j] = (c[i][j] + a[i][k] * b[k][j]) % m;
            }
        }
    }
    c
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut it = input.split_ascii_whitespace();
    let digits = it.next().unwrap().as_bytes();
    let mut k: u64 = it.next().unwrap().parse().unwrap();
    let m: u64 = it.next().unwrap().parse().unwrap();
    // going left to right, E is the sum of the substrings ending at the
    // current digit: E' = 10 E + digit * (its position), and S adds up E,
    // so one copy of p acts linearly on (S, E, J, 1), J digits before it
    let (mut power, mut value, mut weighted) = (1 % m, 0u64, 0u64);
    let (mut sum_power, mut sum_value, mut sum_weighted) = (0u64, 0u64, 0u64);
    for (i, &ch) in digits.iter().enumerate() {
        let d = u64::from(ch - b'0');
        power = power * BASE % m;
        value = (value * BASE + d) % m;
        weighted = (weighted * BASE + d * (i as u64 + 1)) % m;
        sum_power = (sum_power + power) % m;
        sum_value = (sum_value + value) % m;
        sum_weighted = (sum_weighted + weighted) % m;
    }
    let mut block: Matrix = [
        [1 % m, sum_power, sum_value, sum_weighted],
        [0, power, value, weighted],
        [0, 0, 1 % m, digits.len() as u64 % m],
        [0, 0, 0, 1 % m],
    ];
    let mut result = [[0u64; SIZE]; SIZE];
    for (i, row) in result.iter_mut().enumerate() {
        row[i] = 1 % m;
    }
    while k > 0 {
        if k & 1 == 1 {
            result = multiply(&result, &block, m);
        }
        block = multiply(&block, &block, m);
        k >>= 1;
    }
    // starting from S = E = J = 0, the total is the constant column of S
    println!("{}", result[0][SIZE - 1]);
}
