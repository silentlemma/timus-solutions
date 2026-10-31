use std::collections::HashMap;
use std::io::{self, BufRead, Write};

const ALPHABET: usize = 26;
const WORD_COUNT: usize = 6;
const WORDS: [&[u8]; WORD_COUNT] = [b"out", b"output", b"puton", b"in", b"input", b"one"];

fn main() {
    let mut trie = vec![[None; ALPHABET]];
    let mut terminal = vec![false];
    for word in WORDS {
        let mut node = 0;
        for &letter in word {
            let c = (letter - b'a') as usize;
            if trie[node][c].is_none() {
                trie[node][c] = Some(trie.len());
                trie.push([None; ALPHABET]);
                terminal.push(false);
            }
            node = trie[node][c].unwrap();
        }
        terminal[node] = true;
    }
    // the six words have 24 letters in total, so all trie nodes fit in 32 bits.
    // bit zero permits a new word; other bits are unfinished matching prefixes.
    let mut masks = vec![1u32];
    let mut ids = HashMap::from([(1u32, 0usize)]);
    let mut table = Vec::new();
    let mut s = 0;
    while s < masks.len() {
        let mut row = [0; ALPHABET];
        for (c, target) in row.iter_mut().enumerate() {
            let mut mask = 0;
            for (node, edges) in trie.iter().enumerate() {
                if masks[s] & (1 << node) != 0 {
                    if let Some(to) = edges[c] {
                        mask |= 1 << to;
                        if terminal[to] {
                            mask |= 1;
                        }
                    }
                }
            }
            let count = masks.len();
            *target = *ids.entry(mask).or_insert_with(|| {
                masks.push(mask);
                count
            });
        }
        table.push(row);
        s += 1;
    }
    let stdin = io::stdin();
    let mut input = stdin.lock();
    let mut first = String::new();
    input.read_line(&mut first).unwrap();
    let n: usize = first.trim().parse().unwrap();
    let mut out = io::BufWriter::new(io::stdout().lock());
    let (mut state, mut lines, mut started) = (0, 0, false);
    // chunks are consumed fully even after rejection; no input line is retained.
    loop {
        let data = input.fill_buf().unwrap();
        if data.is_empty() {
            break;
        }
        for &c in data {
            if c.is_ascii_lowercase() {
                state = table[state][(c - b'a') as usize];
                started = true;
            } else if started {
                writeln!(out, "{}", if masks[state] & 1 != 0 { "YES" } else { "NO" }).unwrap();
                state = 0;
                started = false;
                lines += 1;
            }
        }
        let length = data.len();
        input.consume(length);
    }
    if started && lines < n {
        writeln!(out, "{}", if masks[state] & 1 != 0 { "YES" } else { "NO" }).unwrap();
    }
}
