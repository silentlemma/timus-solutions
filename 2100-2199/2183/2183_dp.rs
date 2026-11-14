use std::io::{self, BufRead};

fn number(input: &mut impl BufRead) -> i32 {
    let (mut value, mut sign, mut started) = (0, 1, false);
    loop {
        let buffer = input.fill_buf().unwrap();
        if buffer.is_empty() {
            return sign * value;
        }
        let mut consumed = 0;
        for &byte in buffer {
            consumed += 1;
            if byte.is_ascii_digit() {
                value = 10 * value + i32::from(byte - b'0');
                started = true;
            } else if started {
                input.consume(consumed);
                return sign * value;
            } else if byte == b'-' {
                sign = -1;
            }
        }
        input.consume(consumed);
    }
}

fn main() {
    let mut input = io::stdin().lock();
    let n = number(&mut input);
    let first = number(&mut input);
    let (mut untouched, mut ending, mut used) = (first, -first, -first);
    // Ending flips the last value. Used allows the flip to end anywhere.
    for _ in 1..n {
        let value = number(&mut input);
        ending = (-value).min(ending.max(untouched));
        used = ending.max(value.min(used));
        untouched = value.min(untouched);
    }
    println!("{used}");
}
