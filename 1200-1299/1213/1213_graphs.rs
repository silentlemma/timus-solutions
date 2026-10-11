use std::collections::HashSet;
use std::io::{self, Read};

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut it = input.split_ascii_whitespace();
    let mut names: HashSet<&str> = HashSet::new();
    names.insert(it.next().unwrap());
    for line in it.take_while(|&t| t != "#") {
        names.extend(line.splitn(2, '-'));
    }
    // every other compartment must be emptied through one opened partition,
    // and the partitions of a tree towards the airlock are enough
    println!("{}", names.len() - 1);
}
