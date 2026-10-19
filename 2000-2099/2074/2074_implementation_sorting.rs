use std::collections::{BTreeMap, BTreeSet};
use std::io::{self, Read};

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut path: Vec<String> = Vec::new(); // names of the current topic and its ancestors
    let mut topics: BTreeMap<u32, BTreeSet<String>> = BTreeMap::new(); // problem -> its topics
    let mut current = String::new();
    for line in input.lines() {
        let words: Vec<&str> = line.split_whitespace().collect();
        if words.is_empty() {
            continue;
        }
        if words[0].ends_with('.') {
            // a heading "1.2. name": its depth is the number of dots
            let depth = words[0].matches('.').count();
            path.truncate(depth - 1);
            path.push(words[1..].join(" "));
            current = path.join(".");
        } else {
            for w in &words {
                topics.entry(w.parse().unwrap()).or_default().insert(current.clone());
            }
        }
    }
    // problems are visited in increasing order
    let mut groups: BTreeMap<String, Vec<u32>> = BTreeMap::new();
    for (problem, own) in &topics {
        let key = own.iter().cloned().collect::<Vec<_>>().join(", ");
        groups.entry(key).or_default().push(*problem);
    }
    let mut lines: Vec<String> = groups
        .iter()
        .map(|(key, problems)| {
            let numbers: Vec<String> = problems.iter().map(|p| p.to_string()).collect();
            format!("{} : {}", numbers.join(", "), key)
        })
        .collect();
    lines.sort();
    let mut out = lines.join("\n");
    out.push('\n');
    print!("{}", out);
}
