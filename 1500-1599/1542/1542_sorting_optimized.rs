use std::collections::HashMap;
use std::io::{self, BufWriter, Read, Write};

const SHOWN: usize = 10;
const MAX_WORD: usize = 15;
const LETTER_BITS: usize = 5;
const WORD_BITS: usize = MAX_WORD * LETTER_BITS;
const WORD_MASK: u128 = (1 << WORD_BITS) - 1;
const LETTER_MASK: u128 = (1 << LETTER_BITS) - 1;
const MAX_FREQUENCY: u128 = 1_000_000;

fn encode(word: &str) -> u128 {
    let packed = word.bytes().fold(0, |value, letter| {
        (value << LETTER_BITS) | u128::from(letter - b'a' + 1)
    });
    packed << ((MAX_WORD - word.len()) * LETTER_BITS)
}

fn append_word(mut word: u128, output: &mut Vec<u8>) {
    for _ in 0..MAX_WORD {
        let letter = (word >> (WORD_BITS - LETTER_BITS)) as u8;
        if letter == 0 {
            break;
        }
        output.push(b'a' + letter - 1);
        word = (word << LETTER_BITS) & WORD_MASK;
    }
    output.push(b'\n');
}

fn main() -> io::Result<()> {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input)?;
    let mut tokens = input.split_ascii_whitespace();
    let count: usize = tokens.next().unwrap().parse().unwrap();
    let mut entries = Vec::with_capacity(count);
    for _ in 0..count {
        let word = encode(tokens.next().unwrap());
        let frequency: u128 = tokens.next().unwrap().parse().unwrap();
        entries.push(((MAX_FREQUENCY - frequency) << WORD_BITS) | word);
    }
    let count: usize = tokens.next().unwrap().parse().unwrap();
    let mut queries = Vec::with_capacity(count);
    let mut index = HashMap::new();
    let mut suggestions = Vec::new();
    let mut lengths = 0usize;
    for query in tokens.take(count) {
        if query.len() > MAX_WORD {
            queries.push(None);
        } else {
            let id = *index.entry(encode(query)).or_insert_with(|| {
                suggestions.push((0, Vec::new()));
                suggestions.len() - 1
            });
            queries.push(Some(id));
            lengths |= 1 << (MAX_WORD - query.len());
        }
    }
    drop(input);

    // The high bits order by descending frequency, the low bits alphabetically.
    entries.sort_unstable();
    let mut remaining = suggestions.len();
    for entry in entries {
        if remaining == 0 {
            break;
        }
        let word = entry & WORD_MASK;
        let mut pending = lengths;
        while pending != 0 {
            let suffix = pending.trailing_zeros() as usize * LETTER_BITS;
            pending &= pending - 1;
            // A zero in the last letter slot means this prefix is too long.
            if (word >> suffix) & LETTER_MASK == 0 {
                continue;
            }
            let prefix = (word >> suffix) << suffix;
            if let Some(&id) = index.get(&prefix) {
                let (count, block) = &mut suggestions[id];
                if *count < SHOWN {
                    append_word(word, block);
                    *count += 1;
                    if *count == SHOWN {
                        remaining -= 1;
                    }
                }
            }
        }
    }
    let mut output = BufWriter::new(io::stdout().lock());
    for (i, query) in queries.into_iter().enumerate() {
        if i != 0 {
            output.write_all(b"\n")?;
        }
        if let Some(id) = query {
            output.write_all(&suggestions[id].1)?;
        }
    }
    output.flush()
}
