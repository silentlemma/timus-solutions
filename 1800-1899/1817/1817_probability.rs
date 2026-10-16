use std::io::{self, Read};

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let n: usize = input.trim().parse().unwrap();
    let mut out = String::new();
    for k in 0..n {
        // kids take the first free horse at or after a random one: linear
        // probing on a circle of n slots with k taken. By Knuth's analysis
        // the wait is (Q - 1)/2 with Q = sum (j + 1) k!/(k - j)! / n^j
        let (mut q, mut term) = (0.0f64, 1.0f64);
        for j in 0..=k {
            q += (j + 1) as f64 * term;
            term *= (k - j) as f64 / n as f64;
        }
        out.push_str(&format!("{:.9}\n", (q - 1.0) / 2.0));
    }
    print!("{}", out);
}
