use std::io::{self, Read};

const LIMB: i64 = 1_000_000_000;
const DIGITS: usize = 9;

// 2 x - y for y <= 2 x, with base 10^9 limbs, the lowest first
fn twice_minus(x: &[i64], y: &[i64]) -> Vec<i64> {
    let mut out = vec![0; x.len() + 1];
    let mut carry = 0;
    for (i, slot) in out.iter_mut().enumerate() {
        let v = carry + 2 * x.get(i).copied().unwrap_or(0) - y.get(i).copied().unwrap_or(0);
        carry = if v < 0 { -1 } else { v / LIMB };
        *slot = if v < 0 { v + LIMB } else { v % LIMB };
    }
    while out.len() > 1 && out[out.len() - 1] == 0 {
        out.pop();
    }
    out
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let v: Vec<usize> = input
        .split_ascii_whitespace()
        .map(|t| t.parse().unwrap())
        .collect();
    let (n, k) = (v[0], v[1]);
    // count[i + 1]: lines of i words with no more than k lemons in a row,
    // with count[0] = 1 standing for length -1
    let mut count: Vec<Vec<i64>> = vec![vec![1], vec![1]];
    for i in 1..=n {
        // a valid line of i words is a valid line of i - 1 words plus a word,
        // except those ending in exactly k + 1 lemons after a banana
        let next = if i > k {
            twice_minus(&count[i], &count[i - k - 1])
        } else {
            twice_minus(&count[i], &[0])
        };
        count.push(next);
    }
    let answer = &count[n + 1];
    let mut out = answer[answer.len() - 1].to_string();
    for limb in answer.iter().rev().skip(1) {
        out += &format!("{:0width$}", limb, width = DIGITS);
    }
    println!("{}", out);
}
