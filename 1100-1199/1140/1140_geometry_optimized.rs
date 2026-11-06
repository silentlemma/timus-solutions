use std::io::{self, Read, Write};

const AXES: usize = 3;

fn number(input: &mut impl Iterator<Item = u8>) -> i32 {
    let first = input.find(|byte| !byte.is_ascii_whitespace()).unwrap();
    let mut value = match first {
        b'+' | b'-' => 0,
        digit => i32::from(digit - b'0'),
    };
    for byte in input.take_while(u8::is_ascii_digit) {
        value = value * 10 + i32::from(byte - b'0');
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
    let n = number(&mut input);
    let mut total = [0; AXES];
    for _ in 0..n {
        let direction = input.find(|byte| !byte.is_ascii_whitespace()).unwrap();
        total[usize::from(direction - b'X')] += number(&mut input);
    }
    let (a, b) = (total[0] + total[1], total[2] + total[1]);
    // Clamp zero to the interval between a and b to obtain their median with zero.
    let m = 0.clamp(a.min(b), a.max(b));
    let lengths = [m - a, -m, m - b];
    let mut out = io::stdout().lock();
    writeln!(out, "{}", lengths.iter().filter(|&&step| step != 0).count()).unwrap();
    for (direction, length) in ['X', 'Y', 'Z'].into_iter().zip(lengths) {
        if length != 0 {
            writeln!(out, "{} {}", direction, length).unwrap();
        }
    }
}
