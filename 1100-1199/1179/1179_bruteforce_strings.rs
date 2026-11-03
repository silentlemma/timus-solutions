use std::io::{self, Read};

const WALL: u8 = 36;
const SMALLEST: u8 = 2;

fn digit(c: u8) -> u8 {
    match c {
        b'0'..=b'9' => c - b'0',
        b'A'..=b'Z' => c - b'A' + 10,
        _ => WALL,
    }
}
fn main() {
    let mut text = Vec::new();
    io::stdin().read_to_end(&mut text).unwrap();
    let (mut best_base, mut best) = (SMALLEST, 0);
    for base in SMALLEST..=WALL {
        let (mut inside, mut count) = (false, 0);
        for &c in &text {
            let current = digit(c) < base;
            if current && !inside {
                count += 1;
            }
            inside = current;
        }
        if base == SMALLEST || count > best {
            best_base = base;
            best = count;
        }
    }
    println!("{} {}", best_base, best);
}
