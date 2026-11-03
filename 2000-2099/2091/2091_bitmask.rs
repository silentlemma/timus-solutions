use std::io::{self, Read};

const WORD_BITS: usize = 64;
const GROUPS: usize = 4;

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut tokens = input.split_ascii_whitespace();
    let n: usize = tokens.next().unwrap().parse().unwrap();
    let m: usize = tokens.next().unwrap().parse().unwrap();
    let mut low = vec![0u64; m];
    let mut high = vec![0u64; m];
    let mut counts = vec![0usize; m];
    for r in 0..n {
        for c in 0..m {
            if tokens.next().unwrap() == "1" {
                counts[c] += 1;
                if r < WORD_BITS {
                    low[c] |= 1u64 << r;
                } else {
                    high[c] |= 1u64 << (r - WORD_BITS);
                }
            }
        }
    }
    let (mut best, mut first, mut second) = (n + 1, 0, 1);
    for a in 0..m {
        for b in a + 1..m {
            // Both is the intersection; other groups follow by subtraction.
            let both = ((low[a] & low[b]).count_ones() + (high[a] & high[b]).count_ones()) as usize;
            let score = both
                .max(counts[a] - both)
                .max(counts[b] - both)
                .max(n + both - counts[a] - counts[b]);
            if score < best {
                best = score;
                first = a;
                second = b;
            }
            if best == (n + GROUPS - 1) / GROUPS {
                println!("{}\n{} {}", best, first + 1, second + 1);
                return;
            }
        }
    }
    println!("{}\n{} {}", best, first + 1, second + 1);
}
