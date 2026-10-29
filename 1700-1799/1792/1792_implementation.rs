use std::io::{self, Read};

const DISKS: usize = 4;

// petal j lies in every disk except disk j
fn valid(word: &[u32]) -> bool {
    let total: u32 = word[..DISKS].iter().sum();
    word[DISKS..]
        .iter()
        .enumerate()
        .all(|(j, &p)| (total - word[j]) % 2 == p)
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let word: Vec<u32> = input
        .split_ascii_whitespace()
        .map(|x| x.parse().unwrap())
        .collect();
    // try the word as it is, then each single change
    let mut candidates = vec![word.clone()];
    for k in 0..word.len() {
        let mut changed = word.clone();
        changed[k] ^= 1;
        candidates.push(changed);
    }
    let fixed = candidates.into_iter().find(|c| valid(c)).unwrap();
    let line: Vec<String> = fixed.iter().map(|b| b.to_string()).collect();
    println!("{}", line.join(" "));
}
