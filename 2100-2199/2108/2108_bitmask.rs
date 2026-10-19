use std::io::{self, Read};

const WORD_BITS: usize = 64;

fn read_set(token: &str, masks: &mut [u64], offset: usize) {
    for (bit, digit) in token.bytes().enumerate() {
        if digit == b'1' {
            masks[offset + bit / WORD_BITS] |= 1_u64 << (bit % WORD_BITS);
        }
    }
}

fn main() {
    let mut data = String::new();
    io::stdin().read_to_string(&mut data).unwrap();
    let mut tokens = data.split_whitespace();
    let n: usize = tokens.next().unwrap().parse().unwrap();
    let m: usize = tokens.next().unwrap().parse().unwrap();
    let words = (n + WORD_BITS - 1) / WORD_BITS;
    let mut required = vec![0_u64; m * words];
    let mut added = vec![0_u64; m * words];
    let mut owned = vec![0_u64; words];
    for rule in 0..m {
        read_set(tokens.next().unwrap(), &mut required, rule * words);
        read_set(tokens.next().unwrap(), &mut added, rule * words);
    }
    read_set(tokens.next().unwrap(), &mut owned, 0);

    let mut fired = vec![false; m];
    let mut changed = true;
    while changed {
        changed = false;
        for rule in 0..m {
            if fired[rule] {
                continue;
            }
            let offset = rule * words;
            let mut ready = true;
            for word in 0..words {
                if required[offset + word] & !owned[word] != 0 {
                    ready = false;
                    break;
                }
            }
            if !ready {
                continue;
            }
            fired[rule] = true;
            for word in 0..words {
                let merged = owned[word] | added[offset + word];
                changed |= merged != owned[word];
                owned[word] = merged;
            }
        }
    }

    let answer: String = (0..n)
        .map(|bit| {
            if (owned[bit / WORD_BITS] >> (bit % WORD_BITS)) & 1 != 0 {
                '1'
            } else {
                '0'
            }
        })
        .collect();
    println!("{}", answer);
}
