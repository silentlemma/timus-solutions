use std::io::{self, Read};

const STEP: usize = 1999;

fn main() {
    let mut data = Vec::new();
    io::stdin().read_to_end(&mut data).unwrap();
    let text: Vec<u8> = data
        .into_iter()
        .filter(|&c| c != b'\r' && c != b'\n')
        .collect();
    // Josephus: J(m) is zero-based from the original counting start.
    // After the first deletion, counting restarts STEP positions from that start.
    // Thus J(m) = (J(m - 1) + STEP) % m, with J(1) = 0.
    let survivor = (2..=text.len()).fold(0, |s, m| (s + STEP) % m);
    let answer = match text[survivor] {
        b'?' => "Yes",
        b' ' => "No",
        _ => "No comments",
    };
    println!("{}", answer);
}
