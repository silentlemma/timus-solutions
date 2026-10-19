use std::io::{self, Read};

fn solve(x: u64, y: u64, total: u64) -> Option<(u64, u64)> {
    let a = x.min(total);
    let b = total - a;
    if b > y {
        None
    } else {
        Some((a, b))
    }
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut tokens = input.split_whitespace();
    let x: u64 = match tokens.next() {
        Some(word) => word.parse().unwrap(),
        None => return,
    };
    let y: u64 = tokens.next().unwrap().parse().unwrap();
    let total: u64 = tokens.next().unwrap().parse().unwrap();
    match solve(x, y, total) {
        Some((a, b)) => println!("{} {}", a, b),
        None => println!("Impossible"),
    }
}
