use std::io::{self, Read};

const HEAD: &str = "aabab";
const BLOCK: &str = "bbaaba"; // each block forces two more palindromes

// the end after the blocks for each remainder of n mod 6
const TAILS: [&str; 6] = ["b", "bb", "bbaaababb", "bbaa", "bbaab", ""];

// short lengths where the pattern is not yet the best, found by search
const SPECIAL: [(usize, &str); 3] = [(2, "ab"), (8, "aababbaa"), (11, "aababbaabab")];

fn main() {
    let mut text = String::new();
    io::stdin().read_to_string(&mut text).unwrap();
    let n: usize = text.trim().parse().unwrap();
    let word = if let Some(&(_, w)) = SPECIAL.iter().find(|&&(len, _)| len == n) {
        w.to_string()
    } else if n <= HEAD.len() {
        HEAD[..n].to_string()
    } else {
        let tail = TAILS[n % BLOCK.len()];
        HEAD.to_string() + &BLOCK.repeat((n - HEAD.len() - tail.len()) / BLOCK.len()) + tail
    };
    println!("{}", word);
}
