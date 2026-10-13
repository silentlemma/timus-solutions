use std::io::{self, Read};

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let v: Vec<i32> = input
        .split_whitespace()
        .map(|x| x.parse().unwrap())
        .collect();
    let (harry, larry) = (v[0], v[1]);
    // the last can was shot by both, so each missed the other's count minus one
    println!("{} {}", larry - 1, harry - 1);
}
