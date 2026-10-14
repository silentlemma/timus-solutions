use std::io::{self, BufRead};

fn main() {
    let stdin = io::stdin();
    let mut tokens = stdin
        .lock()
        .lines()
        .map(|line| line.unwrap())
        .flat_map(|line| {
            line.split_ascii_whitespace()
                .map(|t| t.parse::<u64>().unwrap())
                .collect::<Vec<_>>()
        });
    let n = tokens.next().unwrap() as usize;
    // Boyer-Moore vote: a value met more often than all the others together
    // survives pairing every note with a different one
    let (mut leader, mut lead) = (0u64, 0u32);
    for value in tokens.take(n) {
        if lead == 0 {
            leader = value;
            lead = 1;
        } else if value == leader {
            lead += 1;
        } else {
            lead -= 1;
        }
    }
    println!("{}", leader);
}
