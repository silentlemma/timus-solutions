use std::collections::HashMap;
use std::io::{self, Read};

const MEDALS: [&str; 3] = ["gold", "silver", "bronze"];
const PER_MEDAL: usize = 4;
const PRIZE: usize = 5;

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut words = input.split_ascii_whitespace();
    let mut medal: HashMap<&str, &str> = HashMap::new();
    for &kind in MEDALS.iter() {
        for _ in 0..PER_MEDAL {
            medal.insert(words.next().unwrap(), kind);
        }
    }
    let n: usize = words.next().unwrap().parse().unwrap();
    let mut scores = Vec::with_capacity(n);
    for _ in 0..n {
        let k: usize = words.next().unwrap().parse().unwrap();
        let mut right = 0;
        for _ in 0..k {
            let team = words.next().unwrap();
            words.next();
            let kind = words.next().unwrap();
            if medal.get(team) == Some(&kind) {
                right += 1;
            }
        }
        scores.push(right);
    }
    let best = *scores.iter().max().unwrap();
    println!("{}", PRIZE * scores.iter().filter(|&&s| s == best).count());
}
