use std::io::{self, BufRead};

// the numbers are parsed by hand straight from the input buffer, without
// reading the whole input into a String
fn next_int(input: &mut impl BufRead) -> i64 {
    let mut value = 0;
    let mut sign = 1;
    let mut started = false;
    loop {
        let buffer = input.fill_buf().unwrap();
        if buffer.is_empty() {
            return value * sign;
        }
        let mut consumed = 0;
        let mut finished = false;
        for &c in buffer {
            consumed += 1;
            if c == b'-' {
                sign = -1;
                started = true;
            } else if c.is_ascii_digit() {
                value = value * 10 + i64::from(c - b'0');
                started = true;
            } else if started {
                finished = true;
                break;
            }
        }
        input.consume(consumed);
        if finished {
            return value * sign;
        }
    }
}

const TIME: usize = 30000;

fn main() {
    let stdin = io::stdin();
    let mut input = stdin.lock();
    let n = next_int(&mut input);
    // the latest start among the talks that end at each minute; times are at
    // most 30 000, so a u16 holds them
    let mut latest = vec![0u16; TIME + 1];
    for _ in 0..n {
        let start = next_int(&mut input) as u16;
        let end = next_int(&mut input) as usize;
        latest[end] = latest[end].max(start);
    }
    // take the talk that ends first among those starting after the last one
    let (mut count, mut last) = (0, 0);
    for (end, &start) in latest.iter().enumerate() {
        if usize::from(start) > last {
            count += 1;
            last = end;
        }
    }
    println!("{}", count);
}
