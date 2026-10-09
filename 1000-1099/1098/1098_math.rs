use std::io::{self, Read};

const STEP: usize = 1999;

fn main() {
    let mut data = Vec::new();
    io::stdin().read_to_end(&mut data).unwrap();
    let text: Vec<u8> = data
        .into_iter()
        .filter(|&c| c != b'\r' && c != b'\n')
        .collect();
    // Josephus: with m characters left, the one that stays last sits at
    // (survivor of m - 1) + STEP, counted from where the first deletion was
    let survivor = (2..=text.len()).fold(0, |s, m| (s + STEP) % m);
    let answer = match text[survivor] {
        b'?' => "Yes",
        b' ' => "No",
        _ => "No comments",
    };
    println!("{}", answer);
}
