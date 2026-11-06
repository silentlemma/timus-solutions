use std::io::{self, BufRead};

fn main() -> io::Result<()> {
    let stdin = io::stdin();
    let mut input = stdin.lock();
    let (mut kept, mut dropped, mut letters) = (0, 0, 0);
    loop {
        let block = input.fill_buf()?;
        if block.is_empty() {
            break;
        }
        for &byte in block {
            if byte.is_ascii_alphabetic() {
                letters += 1;
            } else if letters != 0 {
                (kept, dropped) = (dropped + letters, kept.max(dropped));
                letters = 0;
            }
        }
        let count = block.len();
        input.consume(count);
    }
    println!("{}", kept.max(dropped + letters));
    Ok(())
}
