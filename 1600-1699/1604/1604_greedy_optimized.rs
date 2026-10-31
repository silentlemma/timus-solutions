use std::collections::BinaryHeap;
use std::io::{self, BufWriter, Read, Write};

fn main() {
    let mut s = String::new();
    io::stdin().read_to_string(&mut s).unwrap();
    let v: Vec<usize> = s
        .split_ascii_whitespace()
        .map(|x| x.parse().unwrap())
        .collect();
    if v.is_empty() {
        return;
    }
    let k = v[0];
    // (signs left, kind), the most signs first
    let mut heap: BinaryHeap<(usize, usize)> = (1..=k).map(|t| (v[t], t)).collect();
    // streaming avoids one allocation per sign and the joined output copy.
    let stdout = io::stdout();
    let mut out = BufWriter::new(stdout.lock());
    let mut first = true;
    let mut prev = 0;
    while let Some(mut top) = heap.pop() {
        if top.1 == prev {
            if let Some(other) = heap.pop() {
                // the most plentiful kind was just used: take the next one
                heap.push(top);
                top = other;
            }
        }
        if !first {
            write!(out, " ").unwrap();
        }
        first = false;
        write!(out, "{}", top.1).unwrap();
        prev = top.1;
        if top.0 > 1 {
            heap.push((top.0 - 1, top.1));
        }
    }
    writeln!(out).unwrap();
}
