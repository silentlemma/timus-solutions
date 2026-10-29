use std::io::{self, Read};

fn main() {
    let mut position = 0_i32;
    let mut steps = 0;
    // a name's only capital letter is its first one, and the first letters tell
    // the cabinets apart, so the input is scanned byte by byte for capitals
    for byte in io::stdin().lock().bytes() {
        let c = byte.unwrap();
        if !c.is_ascii_uppercase() {
            continue;
        }
        let target = match c {
            b'A' | b'P' | b'O' | b'R' => 0,
            b'B' | b'M' | b'S' => 1,
            _ => 2,
        };
        steps += (target - position).abs();
        position = target;
    }
    println!("{}", steps);
}
