use std::io::{self, Read};

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut it = input.split_ascii_whitespace().map(|t| t.parse::<i64>().unwrap());
    let n = it.next().unwrap() as usize;
    // every move adds two heaps, and the game ends when all heaps are ones
    let moves: i64 = it.take(n).map(|a| (a - 1) / 2).sum();
    println!("{}", if moves % 2 == 1 { "Daenerys" } else { "Stannis" });
}
