use std::io::{self, Read};

fn main() {
    let mut data = Vec::new();
    io::stdin().read_to_end(&mut data).unwrap();
    // best sums with the last word kept and dropped; neighbours may not both stay
    let (mut kept, mut dropped) = (0u64, 0u64);
    for word in data.split(|c| !c.is_ascii_alphabetic()) {
        if !word.is_empty() {
            let next = dropped + word.len() as u64;
            dropped = dropped.max(kept);
            kept = next;
        }
    }
    println!("{}", kept.max(dropped));
}
