use std::io::{self, Read};

const TOP: usize = 40;

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let v: Vec<usize> = input
        .split_ascii_whitespace()
        .map(|t| t.parse().unwrap())
        .collect();
    let (n, a, b) = (v[0], v[1], v[2]);
    // Pascal's triangle; the binomials stay below 2^32
    let mut c = [[0u64; TOP]; TOP];
    for i in 0..TOP {
        c[i][0] = 1;
        for j in 1..=i {
            c[i][j] = c[i - 1][j - 1] + c[i - 1][j];
        }
    }
    // up to a identical balls in n boxes: put the unused ones in an extra box,
    // then it is a stars-and-bars count C(a + n, n); the colours are
    // independent, and the product reaches 1.05 * 10^19, past signed 64 bits
    println!("{}", c[a + n][n] * c[b + n][n]);
}
