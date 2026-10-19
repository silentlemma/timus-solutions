use std::io::{self, Read};

// contests played by players 0 to 13, counted from the story
const CONTESTS: [u32; 14] = [5, 21, 12, 2, 1, 4, 6, 1, 4, 4, 1, 0, 1, 1];

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let player: usize = input.trim().parse().unwrap();
    println!("{}", CONTESTS[player]);
}
