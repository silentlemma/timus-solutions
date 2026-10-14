use std::collections::HashMap;
use std::io::{self, Read};

fn main() {
    let mut s = String::new();
    io::stdin().read_to_string(&mut s).unwrap();
    let words: Vec<&str> = s.split_ascii_whitespace().collect();
    let n: u32 = words[0].parse().unwrap();
    let mut count: HashMap<&str, u32> = HashMap::new();
    for &prefecture in words[1..].iter().skip(1).step_by(2) {
        *count.entry(prefecture).or_insert(0) += 1;
    }
    let largest = *count.values().max().unwrap();
    // c wrestlers of one prefecture can avoid each other in all rounds but
    // ceil(log2 c) of them, and dealing the wrestlers sorted by prefecture
    // round-robin into that many top-level groups achieves it for all at once
    let mut unsafe_rounds = 0;
    while 1 << unsafe_rounds < largest {
        unsafe_rounds += 1;
    }
    println!("{}", n - unsafe_rounds);
}
