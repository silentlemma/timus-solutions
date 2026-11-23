#![no_main]

use std::io::{self, Read};

fn solve_entry() {
    let mut position = 0_i32;
    let mut steps = 0;
    // a name's only capital letter is its first one, and the first letters tell
    // the cabinets apart, so the input is scanned byte by byte for capitals
    let mut data = Vec::new();
    io::stdin().read_to_end(&mut data).unwrap();
    for c in data {
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

// Run the algorithm directly and flush Rust's global output before returning to C.
#[no_mangle]
pub extern "C" fn main() -> i32 {
    solve_entry();
    std::io::Write::flush(&mut std::io::stdout()).unwrap();
    0
}
