use std::io::{self, Read};

const SQUARE_FACTOR: i64 = 3;
const CONSTANT_FACTOR: i64 = 12;
const SEARCH_LIMIT: i64 = 2_000_000_000;

fn solve(a: i64, b: i64, c: i64) -> i64 {
    let scaled = SQUARE_FACTOR * b * b / a - CONSTANT_FACTOR * c;
    if scaled < 0 {
        return 1;
    }
    let threshold = scaled / a + 1;
    let (mut low, mut high) = (1, SEARCH_LIMIT);
    while low < high {
        let middle = low + (high - low) / 2;
        if middle * middle > threshold {
            high = middle;
        } else {
            low = middle + 1;
        }
    }
    low
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut words = input.split_whitespace();
    let cases: usize = words.next().unwrap().parse().unwrap();
    let mut output = String::new();
    for _ in 0..cases {
        let a = words.next().unwrap().parse().unwrap();
        let b = words.next().unwrap().parse().unwrap();
        let c = words.next().unwrap().parse().unwrap();
        output.push_str(&solve(a, b, c).to_string());
        output.push('\n');
    }
    print!("{}", output);
}
