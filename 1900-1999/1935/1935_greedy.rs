use std::io::{self, Read};

fn minimum_sheets(clearances: &[i32]) -> i32 {
    clearances.iter().sum::<i32>() + clearances.iter().max().unwrap()
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut values = input.split_whitespace();
    let count = values.next().unwrap().parse::<usize>().unwrap();
    let clearances: Vec<i32> = values
        .take(count)
        .map(|token| token.parse().unwrap())
        .collect();
    println!("{}", minimum_sheets(&clearances));
}
