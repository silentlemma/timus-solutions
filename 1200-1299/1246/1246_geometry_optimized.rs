use std::io::{self, Read};

fn next_number(input: &mut impl Iterator<Item = u8>) -> i64 {
    let first = input.find(|byte| !byte.is_ascii_whitespace()).unwrap();
    let mut value = match first {
        b'+' | b'-' => 0,
        digit => i64::from(digit - b'0'),
    };
    for byte in input {
        if byte.is_ascii_whitespace() {
            break;
        }
        value = 10 * value + i64::from(byte - b'0');
    }
    if first == b'-' {
        -value
    } else {
        value
    }
}

fn main() {
    let stdin = io::stdin();
    let mut input = stdin.lock().bytes().map(Result::unwrap);
    let count = next_number(&mut input);
    let first = (next_number(&mut input), next_number(&mut input));
    let mut previous = first;
    let mut twice_area = 0;
    // Each edge contributes once, including the closing edge to the first point.
    for _ in 1..count {
        let point = (next_number(&mut input), next_number(&mut input));
        twice_area += previous.0 * point.1 - previous.1 * point.0;
        previous = point;
    }
    twice_area += previous.0 * first.1 - previous.1 * first.0;
    println!("{}", if twice_area > 0 { "ccw" } else { "cw" });
}
