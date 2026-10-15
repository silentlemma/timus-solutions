use std::collections::HashSet;
use std::io::{self, Read};

fn main() {
    let mut text = String::new();
    io::stdin().read_to_string(&mut text).unwrap();
    let mut lines = text.split('\n');
    let head: Vec<usize> = lines
        .next()
        .unwrap()
        .split_whitespace()
        .map(|w| w.parse().unwrap())
        .collect();
    let (n, q) = (head[1], head[2]);
    let mut taken = HashSet::new();
    for line in lines.take(n) {
        let team = line.trim();
        // the university is everything before " #k"; names differing only
        // in letter case are the same university
        let university = match team.rfind('#') {
            Some(hash) => team[..hash].trim(),
            None => team,
        }
        .to_lowercase();
        if taken.contains(&university) {
            continue;
        }
        if taken.len() == q {
            println!("{}", team);
            return;
        }
        taken.insert(university);
    }
}
