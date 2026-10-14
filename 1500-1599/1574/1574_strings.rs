use std::io::{self, Read};

fn main() {
    let mut text = String::new();
    io::stdin().read_to_string(&mut text).unwrap();
    let line = text.trim();
    // the balance after each prefix; a shift that starts right after a prefix
    // of the lowest balance never goes below zero, any other shift does
    let prefix: Vec<i64> = line
        .bytes()
        .scan(0i64, |b, c| {
            *b += if c == b'(' { 1 } else { -1 };
            Some(*b)
        })
        .collect();
    let lowest = *prefix.iter().min().unwrap();
    let count = prefix.iter().filter(|&&b| b == lowest).count();
    println!(
        "{}",
        if prefix[prefix.len() - 1] == 0 {
            count
        } else {
            0
        }
    );
}
