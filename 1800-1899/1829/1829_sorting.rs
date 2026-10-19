use std::io::{self, Read};

const FULL: i64 = (1 << 32) - 1;
const BYTE: u32 = 8;

// a dotted address read byte by byte
fn address(text: &str) -> i64 {
    text.split('.').fold(0, |value, part| value << BYTE | part.parse::<i64>().unwrap())
}

// adjacent pieces with one gateway merge, so equal routing gives equal
// lists
fn emit(out: &mut Vec<(i64, i64, i64)>, lo: i64, hi: i64, gate: i64) {
    if lo > hi {
        return;
    }
    match out.last_mut() {
        Some(last) if last.1 + 1 == lo && last.2 == gate => last.1 = hi,
        _ => out.push((lo, hi, gate)),
    }
}

// each row covers one aligned block of addresses, and two blocks are
// nested or apart; sweeping them by start, larger first, with a stack of
// open blocks cuts the line into pieces routed by the innermost one
fn pieces(mut blocks: Vec<(i64, i64, i64)>) -> Vec<(i64, i64, i64)> {
    blocks.sort_by(|x, y| x.0.cmp(&y.0).then(y.1.cmp(&x.1)));
    blocks.push((FULL + 1, FULL + 1, -1));
    let mut out = Vec::new();
    let mut stack: Vec<(i64, i64, i64)> = Vec::new();
    let mut pos = 0;
    for b in blocks {
        while let Some(&top) = stack.last() {
            if top.1 >= b.0 {
                break;
            }
            stack.pop();
            emit(&mut out, pos, top.1, top.2);
            pos = top.1 + 1;
        }
        if let Some(&top) = stack.last() {
            emit(&mut out, pos, b.0 - 1, top.2);
        }
        pos = b.0;
        stack.push(b);
    }
    out
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut it = input.split_ascii_whitespace();
    let mut tables = Vec::new();
    for _ in 0..2 {
        let count: usize = match it.next() {
            Some(t) => t.parse().unwrap(),
            None => return,
        };
        let blocks = (0..count)
            .map(|_| {
                let d = address(it.next().unwrap());
                let m = address(it.next().unwrap());
                let g = address(it.next().unwrap());
                (d & m, (d & m) | (FULL ^ m), g)
            })
            .collect();
        tables.push(pieces(blocks));
    }
    println!("{}", if tables[0] == tables[1] { "YES" } else { "NO" });
}
