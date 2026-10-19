use std::fmt::Write as FmtWrite;
use std::io::{self, Read};

const MODULUS: i64 = 614_889_782_588_491_410;

fn process_queries(number: &str, queries: &[(i64, i64, i64)]) -> Vec<i64> {
    let mut digits = number.as_bytes().to_vec();
    let mut weights = vec![1_i64; digits.len()];
    for index in 1..weights.len() {
        weights[index] = weights[index - 1] * 10 % MODULUS;
    }
    let mut remainder = 0_i64;
    for &digit in &digits {
        remainder = (remainder * 10 + i64::from(digit - b'0')) % MODULUS;
    }
    let mut answers = Vec::new();
    for &(kind, first, second) in queries {
        if kind == 0 {
            answers.push(remainder % first);
        } else {
            let place = first as usize;
            let index = digits.len() - place;
            let difference = second - i64::from(digits[index] - b'0');
            digits[index] = b'0' + second as u8;
            remainder = (remainder + difference * weights[place - 1]).rem_euclid(MODULUS);
        }
    }
    answers
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut tokens = input.split_whitespace();
    let number = tokens.next().unwrap();
    let count = tokens.next().unwrap().parse::<usize>().unwrap();
    let queries: Vec<(i64, i64, i64)> = (0..count)
        .map(|_| {
            let kind = tokens.next().unwrap().parse().unwrap();
            let first = tokens.next().unwrap().parse().unwrap();
            let second = if kind == 1 {
                tokens.next().unwrap().parse().unwrap()
            } else {
                0
            };
            (kind, first, second)
        })
        .collect();
    let mut output = String::new();
    for answer in process_queries(number, &queries) {
        writeln!(output, "{}", answer).unwrap();
    }
    print!("{}", output);
}
