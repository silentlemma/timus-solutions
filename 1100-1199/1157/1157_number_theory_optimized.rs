use std::io::{self, Read};

const LIMIT: usize = 10000;

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut tokens = input.split_whitespace();
    let before: u8 = tokens.next().unwrap().parse().unwrap();
    let after: u8 = tokens.next().unwrap().parse().unwrap();
    let added: usize = tokens.next().unwrap().parse().unwrap();
    let mut shapes = [0_u8; LIMIT + 1];
    // Count each unordered divisor pair at its smaller side.
    let mut side = 1;
    while side * side <= LIMIT {
        for tiles in (side * side..=LIMIT).step_by(side) {
            shapes[tiles] += 1;
        }
        side += 1;
    }
    let answer = (added + 1..=LIMIT)
        .find(|&tiles| shapes[tiles] == after && shapes[tiles - added] == before)
        .unwrap_or(0);
    println!("{}", answer);
}
