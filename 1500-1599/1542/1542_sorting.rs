use std::collections::HashMap;
use std::io::{self, Read, Write};

const SHOWN: usize = 10; // suggestions per query

fn main() {
    let mut s = String::new();
    io::stdin().read_to_string(&mut s).unwrap();
    let mut it = s.split_ascii_whitespace();
    let n: usize = it.next().unwrap().parse().unwrap();
    let mut words: Vec<(i64, &str)> = (0..n)
        .map(|_| {
            let w = it.next().unwrap();
            let c: i64 = it.next().unwrap().parse().unwrap();
            (-c, w)
        })
        .collect();
    let m: usize = it.next().unwrap().parse().unwrap();
    let queries: Vec<&str> = (0..m).map(|_| it.next().unwrap()).collect();
    // query -> indices of its words
    let mut found: HashMap<&str, Vec<usize>> = queries.iter().map(|&q| (q, Vec::new())).collect();
    // the best words come first, so every queried prefix simply keeps the
    // first ten words that start with it
    words.sort();
    for (i, &(_, word)) in words.iter().enumerate() {
        for end in 1..=word.len() {
            if let Some(found_words) = found.get_mut(&word[..end]) {
                if found_words.len() < SHOWN {
                    found_words.push(i);
                }
            }
        }
    }
    let mut out = String::new();
    for (j, q) in queries.iter().enumerate() {
        if j > 0 {
            out.push('\n');
        }
        for &i in &found[q] {
            out.push_str(words[i].1);
            out.push('\n');
        }
    }
    io::stdout().write_all(out.as_bytes()).unwrap();
}
