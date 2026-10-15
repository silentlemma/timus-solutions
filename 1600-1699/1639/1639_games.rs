use std::io::{self, Read};

fn main() {
    let mut text = String::new();
    io::stdin().read_to_string(&mut text).unwrap();
    let mut nums = text.split_ascii_whitespace().map(|w| w.parse::<u32>().unwrap());
    let (m, n) = (nums.next().unwrap(), nums.next().unwrap());
    // every break adds one piece, so the game always lasts m * n - 1 moves
    println!("{}", if (m * n - 1) % 2 == 1 { "[:=[first]" } else { "[second]=:]" });
}
