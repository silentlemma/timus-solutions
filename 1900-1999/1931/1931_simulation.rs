use std::io::{self, Read};

fn most_compared(values: &[i32]) -> usize {
    let mut champion_value = values[0];
    let (mut champion, mut best) = (0, 0);
    let (mut current_count, mut best_count) = (0, 0);
    for (index, &value) in values.iter().enumerate().skip(1) {
        current_count += 1;
        if current_count > best_count {
            best_count = current_count;
            best = champion;
        }
        if value < champion_value {
            champion_value = value;
            champion = index;
            current_count = 1;
        }
    }
    best + 1
}

fn main() {
    let mut text = String::new();
    io::stdin().read_to_string(&mut text).unwrap();
    let mut tokens = text.split_whitespace();
    let count = tokens.next().unwrap().parse::<usize>().unwrap();
    let values: Vec<i32> = (0..count)
        .map(|_| tokens.next().unwrap().parse().unwrap())
        .collect();
    println!("{}", most_compared(&values));
}
