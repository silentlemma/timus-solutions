use std::collections::BTreeSet;
use std::io::{self, Read};

const LIMIT: usize = 100000;

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let n: usize = input.trim().parse().unwrap();
    // a palindrome of two or more letters has one of two or three letters
    // in its middle, so any three letters in a row must differ, and a name
    // is one order of a, b, c repeated
    let orders = ["abc", "acb", "bac", "bca", "cab", "cba"];
    let names: BTreeSet<String> = orders
        .iter()
        .map(|order| order.chars().cycle().take(n).collect())
        .collect();
    if names.len() * n > LIMIT {
        println!("TOO LONG");
        return;
    }
    let out: Vec<&str> = names.iter().map(|s| s.as_str()).collect();
    println!("{}", out.join("\n"));
}
