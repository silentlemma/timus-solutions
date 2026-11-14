use std::io::{self, BufRead};

const SCALE: u32 = 1000;

fn token(input: &mut impl BufRead, mut digit: impl FnMut(u8)) {
    let mut started = false;
    loop {
        let bytes = input.fill_buf().unwrap();
        if bytes.is_empty() {
            return;
        }
        let mut consumed = 0;
        for &byte in bytes {
            consumed += 1;
            if !byte.is_ascii_whitespace() {
                started = true;
                digit(byte);
            } else if started {
                input.consume(consumed);
                return;
            }
        }
        input.consume(consumed);
    }
}

fn residue(input: &mut impl BufRead) -> u32 {
    let (mut value, mut place) = (0, SCALE);
    let mut negative = false;
    token(input, |byte| match byte {
        b'-' => negative = true,
        b'.' => place = SCALE / 10,
        b'0'..=b'9' if place < SCALE => {
            value += u32::from(byte - b'0') * place;
            place /= 10;
        }
        _ => (),
    });
    if negative && value != 0 {
        SCALE - value
    } else {
        value
    }
}

fn norm(key: u32) -> u32 {
    let (x, y) = (key / SCALE, key % SCALE);
    let (dx, dy) = (x.min(SCALE - x), y.min(SCALE - y));
    dx * dx + dy * dy
}

fn main() {
    let stdin = io::stdin();
    let mut input = stdin.lock();
    let mut size = 0;
    token(&mut input, |byte| {
        if byte.is_ascii_digit() {
            size = size * 10 + usize::from(byte - b'0');
        }
    });
    let mut keys = Vec::with_capacity(size);
    for _ in 0..size {
        let x = residue(&mut input);
        let y = residue(&mut input);
        keys.push(x * SCALE + y);
    }
    keys.sort_unstable();
    let (mut best_count, mut best_norm) = (0, 0);
    let mut first = 0;
    while first < size {
        let key = keys[first];
        let mut end = first + 1;
        while end < size && keys[end] == key {
            end += 1;
        }
        let count = end - first;
        if count >= best_count {
            let distance = norm(key);
            if count > best_count || distance < best_norm {
                best_count = count;
                best_norm = distance;
            }
        }
        first = end;
    }
    println!(
        "{} {:.9}",
        best_count,
        f64::from(best_norm).sqrt() / f64::from(SCALE)
    );
}
