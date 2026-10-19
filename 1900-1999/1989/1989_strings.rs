use std::io::{self, Read, Write};

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut tokens = input.split_ascii_whitespace();
    let mut word = tokens.next().unwrap().as_bytes().to_vec();
    let size = word.len();
    let mut reverse: Vec<u8> = word.iter().rev().copied().collect();
    let operations: usize = tokens.next().unwrap().parse().unwrap();
    let mut answer = String::new();
    for _ in 0..operations {
        let operation = tokens.next().unwrap();
        let left: usize = tokens.next().unwrap().parse::<usize>().unwrap() - 1;
        let right = tokens.next().unwrap();
        if operation == "change" {
            let value = right.as_bytes()[0];
            word[left] = value;
            reverse[size - 1 - left] = value;
        } else {
            let end: usize = right.parse().unwrap();
            let half = (end - left) / 2;
            answer.push_str(
                if word[left..left + half] == reverse[size - end..size - end + half] {
                    "Yes\n"
                } else {
                    "No\n"
                },
            );
        }
    }
    io::stdout().write_all(answer.as_bytes()).unwrap();
}
