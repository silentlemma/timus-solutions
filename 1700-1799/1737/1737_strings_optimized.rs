use std::io::{self, BufWriter, Read, Write};

const LIMIT: usize = 100000;
const LETTERS: &[u8] = b"abc";
const PERIOD: usize = LETTERS.len();
const BLOCK_REPEATS: usize = 1024;
const BLOCK_SIZE: usize = PERIOD * BLOCK_REPEATS;
const BUFFER_SIZE: usize = 4096;

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let n: usize = input.trim().parse().unwrap();
    let stdout = io::stdout();
    let mut out = BufWriter::with_capacity(BUFFER_SIZE, stdout.lock());
    if n == 1 {
        for &letter in LETTERS {
            out.write_all(&[letter, b'\n']).unwrap();
        }
        return;
    }
    if PERIOD * (PERIOD - 1) * n > LIMIT {
        out.write_all(b"TOO LONG\n").unwrap();
        return;
    }
    let mut block = [0u8; BLOCK_SIZE];
    for first in 0..PERIOD {
        for second in 0..PERIOD {
            if first == second {
                continue;
            }
            let mut third = 0;
            while third == first || third == second {
                third += 1;
            }
            let pattern = [LETTERS[first], LETTERS[second], LETTERS[third]];
            for (i, ch) in block.iter_mut().enumerate() {
                *ch = pattern[i % PERIOD];
            }
            let mut left = n;
            while left > 0 {
                let take = left.min(BLOCK_SIZE);
                out.write_all(&block[..take]).unwrap();
                left -= take;
            }
            out.write_all(b"\n").unwrap();
        }
    }
}
