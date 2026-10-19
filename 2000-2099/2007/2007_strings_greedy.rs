use std::io::{self, Read};

const ALPHABET: usize = 26;
const FIRST: u8 = b'a';

fn solve(source: &str, modifiers: &str) -> String {
    let data = source.as_bytes();
    let size = data.len();
    let mut positions = vec![Vec::new(); ALPHABET];
    for (at, &ch) in data.iter().enumerate() {
        positions[(ch - FIRST) as usize].push(at);
    }
    let mut frequency = [0; ALPHABET];
    let mut counts = [0; ALPHABET];
    for ch in modifiers.bytes() {
        counts[(ch - FIRST) as usize] += 1;
    }
    let mut head = [0; ALPHABET];
    let mut cut = counts;
    let mut next_position = [0; ALPHABET];
    let mut next_cut = [0; ALPHABET];
    let mut delta = [0; ALPHABET];
    let (mut bad, mut available, mut present) = (0u32, 0u32, 0u32);
    for c in 0..ALPHABET {
        frequency[c] = positions[c].len();
        positions[c].push(size);
        next_position[c] = positions[c][0];
        next_cut[c] = if cut[c] < frequency[c] {
            positions[c][cut[c]]
        } else {
            size
        };
        delta[c] = counts[c] as i32 - frequency[c] as i32;
        if delta[c] < 0 || delta[c] & 1 != 0 {
            bad |= 1 << c;
        }
        if counts[c] > 0 {
            available |= 1 << c;
        }
        if frequency[c] > 0 {
            present |= 1 << c;
        }
    }
    let (mut at, mut original, mut dirty) = (0, ALPHABET, true);
    let mut answer = Vec::with_capacity(source.len() + modifiers.len());
    while bad != 0 {
        if dirty {
            if at == size {
                original = ALPHABET;
            } else if counts[(data[at] - FIRST) as usize] == 0 {
                original = (data[at] - FIRST) as usize;
            } else {
                let limit = *next_cut.iter().min().unwrap();
                let mut candidates = present;
                while candidates != 0 {
                    let c = candidates.trailing_zeros() as usize;
                    if next_position[c] <= limit {
                        original = c;
                        break;
                    }
                    candidates &= candidates - 1;
                }
            }
            dirty = false;
        }
        let modifier = if available != 0 {
            available.trailing_zeros() as usize
        } else {
            ALPHABET
        };
        let c;
        if original <= modifier {
            c = original;
            let to = next_position[c];
            while at < to {
                let removed = (data[at] - FIRST) as usize;
                at += 1;
                counts[removed] -= 1;
                head[removed] += 1;
                next_position[removed] = positions[removed][head[removed]];
                if counts[removed] == 0 {
                    available &= !(1 << removed);
                }
                if head[removed] == frequency[removed] {
                    present &= !(1 << removed);
                }
            }
            head[c] += 1;
            next_position[c] = positions[c][head[c]];
            at += 1;
            if head[c] == frequency[c] {
                present &= !(1 << c);
            }
            cut[c] += 1;
            delta[c] += 1;
            dirty = true;
        } else {
            c = modifier;
            counts[c] -= 1;
            if counts[c] == 0 {
                available &= !(1 << c);
            }
            cut[c] -= 1;
            delta[c] -= 1;
        }
        next_cut[c] = if cut[c] < frequency[c] {
            positions[c][cut[c]]
        } else {
            size
        };
        if delta[c] < 0 || delta[c] & 1 != 0 {
            bad |= 1 << c;
        } else {
            bad &= !(1 << c);
        }
        answer.push(FIRST + c as u8);
    }
    String::from_utf8(answer).unwrap()
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut tokens = input.split_whitespace();
    let source = tokens.next().unwrap();
    let modifiers = tokens.next().unwrap();
    println!("{}", solve(source, modifiers));
}
