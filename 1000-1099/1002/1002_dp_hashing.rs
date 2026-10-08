use std::collections::HashMap;
use std::io::{self, Read, Write};

const MAX_WORD_LENGTH: usize = 50;
const KEYPAD: &[u8] = b"22233344115566070778889990";
const END_OF_INPUT: &str = "-1";

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut tokens = input.split_ascii_whitespace();
    let mut out = String::new();
    loop {
        let phone = tokens.next().unwrap();
        if phone == END_OF_INPUT {
            break;
        }
        let n: usize = tokens.next().unwrap().parse().unwrap();
        let words: Vec<&str> = (0..n).map(|_| tokens.next().unwrap()).collect();
        let mut by_digits: HashMap<Vec<u8>, usize> = HashMap::with_capacity(n);
        for (i, w) in words.iter().enumerate() {
            let digits: Vec<u8> = w.bytes().map(|c| KEYPAD[(c - b'a') as usize]).collect();
            by_digits.entry(digits).or_insert(i);
        }
        // best[i]: fewest words for the first i digits; how[i]: last word used
        let phone = phone.as_bytes();
        let m = phone.len();
        let mut best: Vec<Option<usize>> = vec![None; m + 1];
        let mut how = vec![0usize; m + 1];
        best[0] = Some(0);
        for i in 0..m {
            let cur = match best[i] {
                Some(cur) => cur,
                None => continue,
            };
            for end in i + 1..=m.min(i + MAX_WORD_LENGTH) {
                if let Some(&w) = by_digits.get(&phone[i..end]) {
                    if best[end].map_or(true, |b| cur + 1 < b) {
                        best[end] = Some(cur + 1);
                        how[end] = w;
                    }
                }
            }
        }
        if best[m].is_none() {
            out.push_str("No solution.\n");
            continue;
        }
        let mut used = Vec::new();
        let mut pos = m;
        while pos > 0 {
            used.push(words[how[pos]]);
            pos -= words[how[pos]].len();
        }
        used.reverse();
        out.push_str(&used.join(" "));
        out.push('\n');
    }
    io::stdout().write_all(out.as_bytes()).unwrap();
}
