use std::collections::HashSet;
use std::io::{self, Read};

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut words = input.split_ascii_whitespace();
    let read_set = |words: &mut std::str::SplitAsciiWhitespace| -> HashSet<String> {
        let count: usize = words.next().unwrap().parse().unwrap();
        (0..count)
            .map(|_| words.next().unwrap().to_string())
            .collect()
    };
    let menu = read_set(&mut words);
    let k: usize = words.next().unwrap().parse().unwrap();
    let blocks: Vec<HashSet<String>> = (0..=k).map(|_| read_set(&mut words)).collect();
    let m: usize = words.next().unwrap().parse().unwrap();
    // the first student was fine, so the meal is m products of the rest
    let safe: Vec<&String> = menu.iter().filter(|p| !blocks[0].contains(*p)).collect();
    for danger in &blocks[1..] {
        let risky = safe.iter().filter(|p| danger.contains(**p)).count();
        if m == 0 || risky == 0 {
            println!("YES");
        } else if safe.len() - risky < m {
            println!("NO"); // every possible meal holds a dangerous product
        } else {
            println!("MAYBE");
        }
    }
}
