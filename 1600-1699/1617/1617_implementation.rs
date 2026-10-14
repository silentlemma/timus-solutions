use std::io::{self, Read};

const PAIRS_PER_CAR: usize = 4;
const LARGEST: usize = 700; // the widest diameter in millimetres

fn main() {
    let mut text = String::new();
    io::stdin().read_to_string(&mut text).unwrap();
    let mut words = text.split_ascii_whitespace().map(|w| w.parse::<usize>().unwrap());
    let n = words.next().unwrap();
    let mut count = [0usize; LARGEST + 1];
    for d in words.take(n) {
        count[d] += 1;
    }
    // each diameter equips as many cars as it has full sets of four pairs
    let cars: usize = count.iter().map(|c| c / PAIRS_PER_CAR).sum();
    println!("{}", cars);
}
