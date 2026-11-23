use std::io::{self, Read};

const PARAMS: usize = 3;
const MAJORITY: usize = 2;

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut it = input.split_ascii_whitespace();
    let n: usize = parse_integer(it.next().unwrap());
    let mut names = Vec::new();
    let mut stats = Vec::new();
    for _ in 0..n {
        names.push(it.next().unwrap());
        let row: Vec<i32> = (0..PARAMS)
            .map(|_| parse_integer(it.next().unwrap()))
            .collect();
        stats.push(row);
    }
    // reach[i][j]: i beats j, directly or through a chain of wins
    let mut reach = vec![vec![false; n]; n];
    for i in 0..n {
        for j in 0..n {
            let better = (0..PARAMS).filter(|&p| stats[i][p] > stats[j][p]).count();
            reach[i][j] = i != j && better >= MAJORITY;
        }
    }
    for k in 0..n {
        let row = reach[k].clone();
        for i in 0..n {
            if reach[i][k] {
                for j in 0..n {
                    reach[i][j] |= row[j];
                }
            }
        }
    }
    let mut out = String::new();
    // a Jedi can win when every other one can be beaten along such a chain
    for i in 0..n {
        if (0..n).all(|j| i == j || reach[i][j]) {
            out += names[i];
            out.push('\n');
        }
    }
    print!("{}", out);
}

// Input bounds guarantee that each decimal token fits its destination integer.
// Accumulate negative values directly so the minimum signed integer also fits.
fn parse_integer<T>(word: &str) -> T
where
    T: From<u8> + std::ops::Add<Output = T> + std::ops::Sub<Output = T> + std::ops::Mul<Output = T>,
{
    let digits = word.as_bytes();
    let negative = digits[0] == b'-';
    let start = usize::from(negative || digits[0] == b'+');
    let mut value = T::from(0);
    for &byte in &digits[start..] {
        let digit = T::from(byte - b'0');
        let scaled = value * T::from(10);
        value = if negative {
            scaled - digit
        } else {
            scaled + digit
        };
    }
    value
}
