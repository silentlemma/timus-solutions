use std::io::{self, Read};

type Matrix = [[u64; 2]; 2];

fn multiply(x: &Matrix, y: &Matrix, m: u64) -> Matrix {
    let mut r = [[0; 2]; 2];
    for i in 0..2 {
        for j in 0..2 {
            let s = x[i][0] as u128 * y[0][j] as u128 + x[i][1] as u128 * y[1][j] as u128;
            r[i][j] = (s % m as u128) as u64;
        }
    }
    r
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let v: Vec<u64> = input
        .split_ascii_whitespace()
        .map(|t| t.parse().unwrap())
        .collect();
    let (n, k, m) = (v[0], v[1], v[2]);
    let d = (k - 1) % m;
    // (zero, other) -> (other, (zero + other)(K - 1)) is the matrix step,
    // after the first digit the pair is (0, K - 1)
    let mut step: Matrix = [[0, 1 % m], [d, d]];
    let mut power: Matrix = [[1 % m, 0], [0, 1 % m]];
    let mut e = n - 1;
    while e > 0 {
        if e & 1 == 1 {
            power = multiply(&power, &step, m);
        }
        step = multiply(&step, &step, m);
        e >>= 1;
    }
    let sum = power[0][1] as u128 + power[1][1] as u128;
    println!("{}", sum * d as u128 % m as u128);
}
