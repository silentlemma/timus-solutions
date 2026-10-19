use std::io::{self, Read};

const ALICE: i32 = 1;
const DRAW: i32 = 0;
const BOB: i32 = -1;

// the colour of a strip that shows a single colour on both sides, if any
fn winner(top: &[u8], bottom: &[u8]) -> Option<i32> {
    for (colour, result) in [(b'A', ALICE), (b'B', BOB)] {
        if top.iter().chain(bottom.iter()).all(|&c| c == colour) {
            return Some(result);
        }
    }
    None
}

// the result of optimal play from this strip with this player to move
fn play(top: &[u8], bottom: &[u8], alice: bool) -> i32 {
    let n = top.len();
    if n % 2 == 1 {
        return DRAW;
    }
    let half = n / 2;
    // folding brings the right half over or under the left one; the faces that
    // end up inside are hidden
    let upper: Vec<u8> = top[half..].iter().rev().copied().collect();
    let lower: Vec<u8> = bottom[half..].iter().rev().copied().collect();
    let folds = [(&top[..half], &upper[..]), (&lower[..], &bottom[..half])];
    let mut best: Option<i32> = None;
    for (new_top, new_bottom) in folds {
        let result =
            winner(new_top, new_bottom).unwrap_or_else(|| play(new_top, new_bottom, !alice));
        if best.map_or(true, |b| if alice { result > b } else { result < b }) {
            best = Some(result);
        }
        if best == Some(if alice { ALICE } else { BOB }) {
            break;
        }
    }
    best.unwrap()
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let words: Vec<&str> = input.split_whitespace().collect();
    let result = play(words[1].as_bytes(), words[2].as_bytes(), true);
    let name = match result {
        ALICE => "Alice",
        BOB => "Bob",
        _ => "Draw",
    };
    println!("{}", name);
}
