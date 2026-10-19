use std::io::{self, Read};

const WINDOW_SIZE: usize = 3;

fn maximum_window(values: &[i32]) -> (i32, usize) {
    let mut current: i32 = values[..WINDOW_SIZE].iter().sum();
    let mut best = current;
    let mut position = WINDOW_SIZE / 2 + 1;
    for start in 1..=values.len() - WINDOW_SIZE {
        current += values[start + WINDOW_SIZE - 1] - values[start - 1];
        if current > best {
            best = current;
            position = start + WINDOW_SIZE / 2 + 1;
        }
    }
    (best, position)
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut tokens = input.split_whitespace();
    let count = tokens.next().unwrap().parse::<usize>().unwrap();
    let values: Vec<i32> = tokens
        .take(count)
        .map(|token| token.parse().unwrap())
        .collect();
    let (best, position) = maximum_window(&values);
    println!("{} {}", best, position);
}
