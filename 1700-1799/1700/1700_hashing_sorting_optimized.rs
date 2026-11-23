#![no_main]

use std::collections::HashMap;
use std::io::{self, Read, Write};

fn solve_entry() {
    let mut text = String::new();
    io::stdin().read_to_string(&mut text).unwrap();
    let mut lines = text.lines();
    let n: usize = parse_integer(lines.next().unwrap().trim());
    let mut known: HashMap<&str, Vec<u32>> = HashMap::with_capacity(n);
    let mut identifiers = HashMap::new();
    let mut vocabulary = Vec::new();
    for _ in 0..n {
        let line = lines.next().unwrap();
        let colon = line.find(':').unwrap();
        let mut words = Vec::new();
        for word in line[colon + 1..].split_whitespace() {
            let id = *identifiers.entry(word).or_insert_with(|| {
                vocabulary.push(word);
                (vocabulary.len() - 1) as u32
            });
            words.push(id);
        }
        known.insert(&line[..colon], words);
    }
    drop(identifiers);

    // Lexicographic IDs make each intersection and its output integer-only.
    let mut order: Vec<usize> = (0..vocabulary.len()).collect();
    order.sort_unstable_by_key(|&id| vocabulary[id]);
    let mut rank = vec![0_u32; vocabulary.len()];
    let mut sorted = Vec::with_capacity(vocabulary.len());
    for (new_id, old_id) in order.into_iter().enumerate() {
        rank[old_id] = new_id as u32;
        sorted.push(vocabulary[old_id]);
    }
    vocabulary = sorted;
    for words in known.values_mut() {
        for id in words.iter_mut() {
            *id = rank[*id as usize];
        }
        words.sort_unstable();
        words.dedup();
    }
    drop(rank);

    let m: usize = parse_integer(lines.next().unwrap().trim());
    let mut out = String::new();
    for _ in 0..m {
        let mut sets: Vec<&Vec<u32>> = lines
            .next()
            .unwrap()
            .split_whitespace()
            .map(|name| &known[name])
            .collect();
        sets.sort_unstable_by_key(|set| set.len());
        // the common associations are the intersection of the sets
        let mut common = sets[0].clone();
        for other in sets.into_iter().skip(1) {
            let mut at = 0;
            common.retain(|id| {
                while at < other.len() && other[at] < *id {
                    at += 1;
                }
                at < other.len() && other[at] == *id
            });
            if common.is_empty() {
                break;
            }
        }
        if common.is_empty() {
            out.push_str("No solution.\n");
        } else {
            for (index, id) in common.into_iter().enumerate() {
                if index != 0 {
                    out.push(' ');
                }
                out.push_str(vocabulary[id as usize]);
            }
            out.push('\n');
        }
    }
    io::stdout().write_all(out.as_bytes()).unwrap();
}

// Input bounds guarantee that each decimal token fits its destination integer.
// Accumulate negative values directly so the minimum signed integer also fits.
fn parse_integer<T>(word: &str) -> T
where
    T: From<u8> + std::ops::Add<Output = T> + std::ops::Sub<Output = T> + std::ops::Mul<Output = T>,
{
    let digits = word.as_bytes();
    let negative = digits[0] == b'-';
    let start = usize::from(negative || digits[0] == b'+');
    let mut value = T::from(0);
    for &byte in &digits[start..] {
        let digit = T::from(byte - b'0');
        let scaled = value * T::from(10);
        value = if negative {
            scaled - digit
        } else {
            scaled + digit
        };
    }
    value
}

// Run the algorithm directly and flush Rust's global output before returning to C.
#[no_mangle]
pub extern "C" fn main() -> i32 {
    solve_entry();
    std::io::Write::flush(&mut std::io::stdout()).unwrap();
    0
}
