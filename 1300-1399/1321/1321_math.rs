use std::io::{self, Read};

const ONE_DIGIT: u32 = 4; // floors 1 to 5 show every indicator lit and unlit

const SHORT: u32 = 5; // blocks of the second digit: 6 through 9, 0 to 2
const LONG: u32 = 7; // blocks of the second digit: 2 to 9, 0

const LOW_TOP: u32 = 3; // a leading digit up to this needs blank, 1, 2 on top
const WIDE: u32 = 3; // blocks of the leading digit otherwise: blank through 4
const RADIX: u32 = 10;

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let n: Vec<u32> = input
        .split_ascii_whitespace()
        .next()
        .unwrap()
        .chars()
        .map(|c| c.to_digit(RADIX).unwrap())
        .collect();
    if n.len() == 1 {
        println!("{}", ONE_DIGIT);
        return;
    }
    let (lead, zeros) = if n[0] == 1 {
        (if n[1] >= 2 { SHORT } else { LONG }, n.len() - 2)
    } else {
        (if n[0] <= LOW_TOP { 1 } else { WIDE }, n.len() - 1)
    };
    // lead * 10^zeros + 1, written out
    if zeros == 0 {
        println!("{}", lead + 1);
    } else {
        println!("{}{}1", lead, "0".repeat(zeros - 1));
    }
}
