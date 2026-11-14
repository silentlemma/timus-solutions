use std::io::{self, Read, Write};

const ALPHABET: usize = 26;

fn fill(pattern: &mut [u8], limit: usize) -> bool {
    let mut fixed = [false; ALPHABET];
    let mut holes = [0; 2];
    for (i, &letter) in pattern.iter().enumerate() {
        if letter == b'?' {
            holes[i % 2] += 1;
        } else {
            fixed[usize::from(letter - b'a')] = true;
        }
    }
    let mut missing = [0; ALPHABET];
    let mut absent = 0;
    for (i, &used) in fixed.iter().enumerate() {
        if !used {
            missing[absent] = i;
            absent += 1;
        }
    }
    let needed = limit.saturating_sub(ALPHABET - absent);
    if needed > holes[0] + holes[1] {
        return false;
    }
    let mut low = [0; ALPHABET + 1];
    let mut high = [0; ALPHABET + 1];
    for i in 0..absent {
        low[i + 1] = low[i] + missing[i];
        high[i + 1] = high[i] + ALPHABET - 1 - missing[absent - 1 - i];
    }
    let positive = (needed.saturating_sub(holes[1])..=needed.min(holes[0]))
        .min_by_key(|&count| high[count] + low[needed - count])
        .unwrap();
    let mut remaining = [positive, needed - positive];
    let (mut left, mut right) = (0, absent);
    for (i, letter) in pattern.iter_mut().enumerate() {
        if *letter != b'?' {
            continue;
        }
        let parity = i % 2;
        *letter = if remaining[parity] == 0 {
            if parity == 0 {
                b'z'
            } else {
                b'a'
            }
        } else {
            remaining[parity] -= 1;
            if parity == 0 {
                right -= 1;
                b'a' + missing[right] as u8
            } else {
                let value = b'a' + missing[left] as u8;
                left += 1;
                value
            }
        };
    }
    true
}

fn main() {
    let mut input = Vec::new();
    io::stdin().read_to_end(&mut input).unwrap();
    let start = input.iter().position(|c| !c.is_ascii_whitespace()).unwrap();
    let mut parts = input[start..].split_mut(u8::is_ascii_whitespace);
    let pattern = parts.next().unwrap();
    let token = parts.find(|field| !field.is_empty()).unwrap();
    let limit = std::str::from_utf8(token).unwrap().parse().unwrap();
    let mut output = io::stdout().lock();
    if fill(pattern, limit) {
        output.write_all(pattern).unwrap();
        output.write_all(b"\n").unwrap();
    } else {
        output.write_all(b"-1\n").unwrap();
    }
}
