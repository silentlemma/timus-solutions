use std::io::{self, Read};

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let text = input.split_ascii_whitespace().next().unwrap().as_bytes();
    let mut suffixes: Vec<&[u8]> = (0..text.len()).map(|i| &text[i..]).collect();
    suffixes.sort_unstable();
    let mut answer = text.len() * (text.len() + 1) / 2;
    // A suffix shares every previously seen prefix with its immediate
    // predecessor in lexicographic order, so only adjacent LCPs matter.
    for pair in suffixes.windows(2) {
        let common = pair[0]
            .iter()
            .zip(pair[1])
            .take_while(|(a, b)| a == b)
            .count();
        answer -= common;
    }
    println!("{}", answer);
}
