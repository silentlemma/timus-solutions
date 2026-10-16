use std::io::{self, Read};

// the smallest number for each word, from the largest down
const FROM: [i32; 9] = [1000, 500, 250, 100, 50, 20, 10, 5, 1];
const WORDS: [&str; 9] = [
    "legion", "zounds", "swarm", "throng", "horde", "lots", "pack", "several", "few",
];

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let n: i32 = input.trim().parse().unwrap();
    let mut i = 0;
    while n < FROM[i] {
        i += 1;
    }
    println!("{}", WORDS[i]);
}
