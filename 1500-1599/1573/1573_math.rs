use std::collections::HashMap;
use std::io::{self, Read};

fn main() {
    let mut text = String::new();
    io::stdin().read_to_string(&mut text).unwrap();
    let mut words = text.split_ascii_whitespace();
    let mut bags: HashMap<&str, u64> = HashMap::new();
    for color in ["Blue", "Red", "Yellow"] {
        bags.insert(color, words.next().unwrap().parse().unwrap());
    }
    let k: usize = words.next().unwrap().parse().unwrap();
    // one reagent from each needed bag, chosen independently
    let ways: u64 = words.take(k).map(|color| bags[color]).product();
    println!("{}", ways);
}
