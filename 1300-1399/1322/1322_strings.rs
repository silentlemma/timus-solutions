use std::io::{self, Read, Write};

const CHARS: usize = 128;

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut words = input.split_ascii_whitespace();
    let k: usize = words.next().unwrap().parse().unwrap();
    let last = words.next().unwrap().as_bytes();
    // a stable counting sort of the last column: row order[j] ends with
    // the j-th character of the sorted column, the first one of row j
    let mut start = vec![0usize; CHARS + 1];
    for &c in last {
        start[c as usize + 1] += 1;
    }
    for c in 0..CHARS {
        start[c + 1] += start[c];
    }
    let mut order = vec![0usize; last.len()];
    for (i, &c) in last.iter().enumerate() {
        order[start[c as usize]] = i;
        start[c as usize] += 1;
    }
    let mut row = k - 1;
    let mut text = Vec::with_capacity(last.len() + 1);
    for _ in 0..last.len() {
        row = order[row];
        text.push(last[row]);
    }
    text.push(b'\n');
    io::stdout().write_all(&text).unwrap();
}
