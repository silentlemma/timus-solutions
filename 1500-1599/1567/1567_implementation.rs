use std::io::{self, BufRead};

/// The characters of each key in the order of presses; the space has a key
/// of its own.
const KEYS: [&str; 11] = [
    "abc", "def", "ghi", "jkl", "mno", "pqr", "stu", "vwx", "yz", ".,!", " ",
];

fn main() {
    // the whole first line, spaces included; anything else costs nothing
    let mut line = String::new();
    io::stdin().lock().read_line(&mut line).unwrap();
    let total: usize = line
        .chars()
        .map(|c| {
            KEYS.iter()
                .filter_map(|key| key.find(c))
                .map(|at| at + 1)
                .sum::<usize>()
        })
        .sum();
    println!("{}", total);
}
