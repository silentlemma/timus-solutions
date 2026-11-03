use std::io::{self, Read};

const BASE: usize = 10;
const DIGITS: usize = 6;
const WORD_BITS: usize = 64;

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let text = input.trim().as_bytes();
    let mut first = 1;
    // Try lengths in order; the first absent value is the global answer.
    for length in 1..=DIGITS {
        let count = (BASE - 1) * first;
        let modulus = first * BASE;
        let mut value = 0;
        let mut seen = vec![0u64; (count + WORD_BITS - 1) / WORD_BITS];
        for (i, &digit) in text.iter().enumerate() {
            value = (value * BASE + usize::from(digit - b'0')) % modulus;
            if i + 1 >= length && value >= first {
                let offset = value - first;
                seen[offset / WORD_BITS] |= 1u64 << (offset % WORD_BITS);
            }
        }
        for offset in 0..count {
            if seen[offset / WORD_BITS] & (1u64 << (offset % WORD_BITS)) == 0 {
                println!("{}", first + offset);
                return;
            }
        }
        first *= BASE;
    }
}
