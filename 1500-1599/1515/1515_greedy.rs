use std::io::{self, Read};

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let v: Vec<u64> = input
        .split_ascii_whitespace()
        .map(|t| t.parse().unwrap())
        .collect();
    let n = v[0] as usize;
    let mut notes = v[1..=n].to_vec();
    notes.sort_unstable();
    // every sum from 1 to reach is made of the notes taken so far; a note
    // no larger than reach + 1 extends that to reach + note
    let mut reach = 0;
    for d in notes {
        if d > reach + 1 {
            break;
        }
        reach += d;
    }
    println!("{}", reach + 1);
}
