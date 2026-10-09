use std::io::{self, Read};

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let n: usize = input.trim().parse().unwrap();
    // on sorted numbers every partition peels off just the first one
    let parts: Vec<String> = (1..=n).map(|i| i.to_string()).collect();
    println!("{}", parts.join(" "));
}
