use std::io::{self, Read};

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let n: u64 = input.trim().parse().unwrap();
    // each number of dots v sits on n + 2 ends: on the tiles v-w for every w,
    // and twice on the double v-v; so the dots add up to (n + 2) * (0 + ... + n)
    println!("{}", (n + 2) * n * (n + 1) / 2);
}
