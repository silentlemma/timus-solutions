use std::io::{self, Read};

const BASE: usize = 10;
const LIMIT: usize = BASE * BASE - 1;
// the d-th character is digit d turned upside down, as in the statement, and
// ? marks a digit that reads as nothing
const TURN: &[u8] = b"01????9?86";

fn solve(count: usize) -> String {
    let mut run = 0;
    for value in 1..=LIMIT {
        if TURN[value / BASE] != b'?' && TURN[value % BASE] != b'?' {
            run += 1;
        } else {
            run = 0;
        }
        if run >= count {
            let mut answer = String::new();
            for offset in 0..count {
                let target = value - offset;
                if !answer.is_empty() {
                    answer.push(' ');
                }
                answer.push(TURN[target % BASE] as char);
                answer.push(TURN[target / BASE] as char);
            }
            return answer;
        }
    }
    "Glupenky Pierre".to_owned()
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    if let Some(word) = input.split_whitespace().next() {
        println!("{}", solve(word.parse().unwrap()));
    }
}
