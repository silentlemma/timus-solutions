use std::collections::HashSet;
use std::io::{self, Read};

fn main() {
    let mut text = String::new();
    io::stdin().read_to_string(&mut text).unwrap();
    let mut lines = text.split('\n');
    let n: usize = lines.next().unwrap().trim().parse().unwrap();
    // a name is the whole line, spaces included; only the line end goes
    let names: Vec<&str> = lines.take(n).map(|l| l.trim_end_matches('\r')).collect();
    let distinct: HashSet<&str> = names.iter().copied().collect();
    println!("{}", names.len() - distinct.len());
}
