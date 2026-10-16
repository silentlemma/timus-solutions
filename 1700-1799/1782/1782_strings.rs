use std::collections::HashMap;
use std::io::{self, Read};

const MOST: usize = 100;
// how many letters may be taken off each end before undoing a doubling
const EDGE: usize = 5;

// the fewest phrases and the letters taken off the front and the back, with
// no cut for the letters one by one
type Plan = (usize, Option<(usize, usize)>);

// the word whose doubling is core, if core is a double
fn halve(core: &[u8]) -> Option<Vec<u8>> {
    let mut half = Vec::with_capacity(core.len() / 2);
    for pair in core.chunks(2) {
        if pair[0] == pair[1] {
            return None;
        }
        half.push(pair[0]);
    }
    Some(half)
}

// the fewest phrases that build s: either all letters one by one, or a few
// letters at each end around the double of a shorter word; a word free of
// these repeats always has that shape with short ends
fn plan(s: &[u8], best: &mut HashMap<Vec<u8>, Plan>) -> Plan {
    if let Some(&p) = best.get(s) {
        return p;
    }
    let n = s.len();
    let mut result: Plan = (n, None);
    for a in 0..=EDGE.min(n) {
        for b in 0..=EDGE.min(n - a) {
            let size = n - a - b;
            if size < 2 || size % 2 == 1 {
                continue;
            }
            if let Some(half) = halve(&s[a..n - b]) {
                let cost = a + b + 1 + plan(&half, best).0;
                if cost < result.0 {
                    result = (cost, Some((a, b)));
                }
            }
        }
    }
    best.insert(s.to_vec(), result);
    result
}

fn phrases(s: &[u8], best: &mut HashMap<Vec<u8>, Plan>, out: &mut Vec<String>) {
    let n = s.len();
    match plan(s, best).1 {
        None => out.extend(s.iter().map(|&c| format!("back {}", c as char))),
        Some((a, b)) => {
            let half = halve(&s[a..n - b]).unwrap();
            phrases(&half, best, out);
            out.push("double".to_string());
            out.extend(s[..a].iter().rev().map(|&c| format!("front {}", c as char)));
            out.extend(s[n - b..].iter().map(|&c| format!("back {}", c as char)));
        }
    }
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let word = input.trim().as_bytes();
    let mut best = HashMap::new();
    if plan(word, &mut best).0 > MOST {
        println!("-1");
        return;
    }
    let mut out = Vec::new();
    phrases(word, &mut best, &mut out);
    println!("{}\n{}", out.len(), out.join("\n"));
}
