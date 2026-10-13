use std::io::{self, Read};

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut lines = input.split('\n');
    let first: Vec<usize> = lines
        .next()
        .unwrap()
        .split_whitespace()
        .map(|x| x.parse().unwrap())
        .collect();
    let (n, m) = (first[0], first[1]);
    // read whole: the text may start with spaces
    let text = lines.next().unwrap_or("").trim_end_matches('\r').as_bytes();
    // run[i]: how many letters and spaces start at position i
    let mut run = vec![0usize; text.len() + 1];
    for i in (0..text.len()).rev() {
        if text[i].is_ascii_alphabetic() || text[i] == b' ' {
            run[i] = run[i + 1] + 1;
        }
    }
    // the farthest reach never moves back, so the longest message each time is best
    let (mut pos, mut count) = (0, 0);
    while pos < text.len() {
        pos += n.max(m.min(run[pos]));
        count += 1;
    }
    println!("{}", count);
}
