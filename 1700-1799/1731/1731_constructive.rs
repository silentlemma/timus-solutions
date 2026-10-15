use std::io::{self, Read};

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut it = input.split_ascii_whitespace().map(|w| w.parse::<usize>().unwrap());
    let (n, m) = (it.next().unwrap(), it.next().unwrap());
    // with first boxes 1..n and second boxes spaced n apart above them,
    // every sum a + b names its pair, so no two gifts can weigh the same
    let first: Vec<String> = (1..=n).map(|i| i.to_string()).collect();
    let second: Vec<String> = (0..m).map(|j| ((j + 1) * n + 1).to_string()).collect();
    println!("{}\n{}", first.join(" "), second.join(" "));
}
