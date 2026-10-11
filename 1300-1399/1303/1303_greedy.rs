use std::io::{self, Read, Write};

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut it = input
        .split_ascii_whitespace()
        .map(|t| t.parse::<i32>().unwrap());
    let m = it.next().unwrap();
    let mut segments = Vec::new();
    while let (Some(left), Some(right)) = (it.next(), it.next()) {
        if left == 0 && right == 0 {
            break;
        }
        segments.push((left, right));
    }
    segments.sort();
    let mut chosen = Vec::new();
    let (mut covered, mut i) = (0, 0);
    while covered < m {
        // among the segments that start inside the covered part, take the
        // one that reaches furthest; it is never worse than any other
        let mut best: Option<(i32, i32)> = None;
        while i < segments.len() && segments[i].0 <= covered {
            if best.map_or(true, |b| segments[i].1 > b.1) {
                best = Some(segments[i]);
            }
            i += 1;
        }
        match best {
            Some(b) if b.1 > covered => {
                chosen.push(b);
                covered = b.1;
            }
            _ => {
                println!("No solution");
                return;
            }
        }
    }
    let mut out = io::BufWriter::new(io::stdout().lock());
    writeln!(out, "{}", chosen.len()).unwrap();
    for (left, right) in chosen {
        writeln!(out, "{} {}", left, right).unwrap();
    }
}
