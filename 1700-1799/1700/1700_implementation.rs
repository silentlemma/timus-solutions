use std::collections::{BTreeSet, HashMap};
use std::io::{self, Read, Write};

fn main() {
    let mut text = String::new();
    io::stdin().read_to_string(&mut text).unwrap();
    let mut lines = text.lines();
    let n: usize = lines.next().unwrap().trim().parse().unwrap();
    let mut known: HashMap<&str, BTreeSet<&str>> = HashMap::new();
    for _ in 0..n {
        let line = lines.next().unwrap();
        let colon = line.find(':').unwrap();
        known.insert(&line[..colon], line[colon + 1..].split_whitespace().collect());
    }
    let m: usize = lines.next().unwrap().trim().parse().unwrap();
    let mut out = String::new();
    for _ in 0..m {
        let names: Vec<&str> = lines.next().unwrap().split_whitespace().collect();
        // the common associations are the intersection of the sets
        let common: Vec<&str> = known[names[0]]
            .iter()
            .filter(|w| names.iter().all(|name| known[name].contains(*w)))
            .copied()
            .collect();
        if common.is_empty() {
            out.push_str("No solution.\n");
        } else {
            out.push_str(&common.join(" "));
            out.push('\n');
        }
    }
    io::stdout().write_all(out.as_bytes()).unwrap();
}
