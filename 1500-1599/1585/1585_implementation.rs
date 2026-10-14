use std::collections::HashMap;
use std::io::{self, Read};

fn main() {
    let mut text = String::new();
    io::stdin().read_to_string(&mut text).unwrap();
    let mut words = text.split_ascii_whitespace();
    let n: usize = words.next().unwrap().parse().unwrap();
    // every record is two words, the kind and "Penguin"
    let mut seen: HashMap<&str, usize> = HashMap::new();
    for _ in 0..n {
        *seen.entry(words.next().unwrap()).or_default() += 1;
        words.next();
    }
    let best = seen.iter().max_by_key(|&(_, &c)| c).unwrap().0;
    println!("{} Penguin", best);
}
