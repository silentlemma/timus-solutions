use std::io::{self, BufRead};

// below this many bits the string is short enough to search directly
const SMALL_BITS: usize = 6;
// the palindrome is made of the numbers 2^(k-1) + 5, 2^(k-1) + 6 and the
// start of 2^(k-1) + 7, three numbers of k bits less two
const NUMBERS: usize = 3;
const TAIL: usize = 3;

fn longest(n: u32) -> usize {
    let s: Vec<u8> = (1..=n).flat_map(|i| format!("{:b}", i).into_bytes()).collect();
    let mut best = 0;
    for centre in 0..2 * s.len() - 1 {
        let (mut lo, mut hi) = (centre as i64 / 2, (centre as i64 + 1) / 2);
        while lo >= 0 && (hi as usize) < s.len() && s[lo as usize] == s[hi as usize] {
            lo -= 1;
            hi += 1;
        }
        best = best.max((hi - lo - 1) as usize);
    }
    best
}

fn main() {
    // the number can have a million digits, so it is read as a stream: its
    // length, its value while short, the first one after the leading one and
    // the last three digits are all that matter
    let stdin = io::stdin();
    let mut reader = stdin.lock();
    let (mut k, mut value, mut first_one, mut last) = (0usize, 0u32, None, 0u32);
    loop {
        let chunk = reader.fill_buf().unwrap();
        if chunk.is_empty() {
            break;
        }
        for &c in chunk {
            if c != b'0' && c != b'1' {
                continue;
            }
            let bit = (c - b'0') as u32;
            if bit == 1 && k > 0 && first_one.is_none() {
                first_one = Some(k);
            }
            if k < SMALL_BITS {
                value = value * 2 + bit;
            }
            last = (last * 2 + bit) & ((1 << TAIL) - 1);
            k += 1;
        }
        let used = chunk.len();
        reader.consume(used);
    }
    if k < SMALL_BITS {
        println!("{}", longest(value));
        return;
    }
    // n reaches 2^(k-1) + 7 when a one follows the leading one before the
    // last three bits, or when those bits are all ones
    let reached = first_one.map_or(false, |i| i < k - TAIL) || last == (1 << TAIL) - 1;
    let bits = if reached { k } else { k - 1 };
    println!("{}", NUMBERS * bits - 2);
}
