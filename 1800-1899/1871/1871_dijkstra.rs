use std::collections::HashMap;
use std::io::{self, Read, Write};

const LONGEST: usize = 140;
const PREFIX: usize = "RT @: ".len();

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut lines = input.split('\n');
    let n: usize = lines.next().unwrap().trim().parse().unwrap();
    let mut names: Vec<&str> = Vec::with_capacity(n);
    let mut follow_names: Vec<Vec<&str>> = Vec::with_capacity(n);
    for _ in 0..n {
        // a description is a name, a count and that many names
        let mut words: Vec<&str> = Vec::new();
        while words.len() < 2 || words.len() < 2 + words[1].parse::<usize>().unwrap() {
            words.extend(lines.next().unwrap().split_whitespace());
        }
        names.push(words[0]);
        follow_names.push(words[2..].to_vec());
    }
    let tweet = lines.next().unwrap_or("").trim_end_matches('\r');
    let index: HashMap<&str, usize> = names.iter().enumerate().map(|(i, &s)| (s, i)).collect();
    // length[u] is the shortest message u can hold; a retweet of u's message
    // is longer by the prefix and u's name
    let mut length = vec![LONGEST + 1; n];
    length[0] = tweet.len();
    let mut done = vec![false; n];
    loop {
        let u = (0..n).filter(|&i| !done[i]).min_by_key(|&i| length[i]);
        let u = match u {
            Some(u) if length[u] <= LONGEST => u,
            _ => break,
        };
        done[u] = true;
        let longer = length[u] + PREFIX + names[u].len();
        for f in &follow_names[u] {
            let v = index[f];
            length[v] = length[v].min(longer);
        }
    }
    // everybody who holds a message shows it to all followers
    let mut knows = vec![false; n];
    for u in 0..n {
        if done[u] {
            knows[u] = true;
            for f in &follow_names[u] {
                knows[index[f]] = true;
            }
        }
    }
    let told: Vec<&str> = (0..n).filter(|&i| knows[i]).map(|i| names[i]).collect();
    let mut out = format!("{}\n", told.len());
    for name in told {
        out.push_str(name);
        out.push('\n');
    }
    io::stdout().write_all(out.as_bytes()).unwrap();
}
