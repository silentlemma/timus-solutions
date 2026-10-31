use std::io::{self, BufRead, Write};

fn main() {
    let stdin = io::stdin();
    let mut lines = stdin.lock().lines();
    let m: usize = lines.next().unwrap().unwrap().trim().parse().unwrap();
    let (mut left, mut right) = (vec![0i32; m], vec![0i32; m]);
    // starts at or below zero share bucket zero; only the farthest end matters.
    // m <= 5000 bounds storage independently of the number of intervals.
    for line in lines {
        let line = line.unwrap();
        let mut words = line
            .split_ascii_whitespace()
            .map(|w| w.parse::<i32>().unwrap());
        let (l, r) = (words.next().unwrap(), words.next().unwrap());
        if l == 0 && r == 0 {
            break;
        }
        if l >= m as i32 || r <= 0 {
            continue;
        }
        let at = l.max(0) as usize;
        if r > right[at] || (r == right[at] && l < left[at]) {
            left[at] = l;
            right[at] = r;
        }
    }
    let mut chosen = Vec::new();
    let (mut covered, mut at) = (0, 0);
    while covered < m as i32 {
        // among the segments that start inside the covered part, take the
        // one that reaches furthest; it is never worse than any other
        let mut best = None;
        while at < m && at as i32 <= covered {
            if best.map_or(true, |b| right[at] > right[b]) {
                best = Some(at);
            }
            at += 1;
        }
        match best {
            Some(b) if right[b] > covered => {
                chosen.push(b);
                covered = right[b];
            }
            _ => {
                println!("No solution");
                return;
            }
        }
    }
    let mut out = io::BufWriter::new(io::stdout().lock());
    writeln!(out, "{}", chosen.len()).unwrap();
    for b in chosen {
        writeln!(out, "{} {}", left[b], right[b]).unwrap();
    }
}
