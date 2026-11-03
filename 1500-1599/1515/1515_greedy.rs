use std::io::{self, Read};

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut tokens = input.split_ascii_whitespace();
    let n: usize = tokens.next().unwrap().parse().unwrap();
    // every sum from 1 to reach is made of the notes taken so far; a note
    // no larger than reach + 1 extends that to reach + note
    let mut reach = 0;
    for _ in 0..n {
        let d: u64 = tokens.next().unwrap().parse().unwrap();
        if d > reach + 1 {
            break;
        }
        reach += d;
    }
    println!("{}", reach + 1);
}
