use std::collections::HashSet;
use std::io::{self, Read};

const UNKNOWN: &str = "unknown";

// every block of size phrases is one language, and no language is used in
// two blocks
fn fits(phrases: &[&str], size: usize) -> bool {
    let mut used = HashSet::new();
    for block in phrases.chunks(size) {
        let known: HashSet<&str> = block.iter().copied().filter(|&p| p != UNKNOWN).collect();
        if known.len() > 1 {
            return false;
        }
        if let Some(&lang) = known.iter().next() {
            if !used.insert(lang) {
                return false;
            }
        }
    }
    true
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut words = input.split_ascii_whitespace();
    let n: usize = words.next().unwrap().parse().unwrap();
    let phrases: Vec<&str> = words.take(n).collect();
    let counts: Vec<String> =
        (1..=n).filter(|&k| n % k == 0 && fits(&phrases, n / k)).map(|k| k.to_string()).collect();
    if counts.is_empty() {
        println!("Igor is wrong.");
    } else {
        println!("{}", counts.join(" "));
    }
}
