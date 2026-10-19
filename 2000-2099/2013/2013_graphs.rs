use std::fmt::Write as FmtWrite;
use std::io::{self, Read};

const UNREACHED: i32 = -2;
const UNKNOWN: i32 = -1;
const MAX_EDGES: usize = 100000;

fn solve(values: &[i32], offsets: &[usize], edges: &[usize]) -> Vec<i32> {
    let mut entry = vec![UNREACHED; values.len()];
    entry[0] = 0;
    let mut pending = Vec::with_capacity(2 * values.len());
    pending.push(0);
    let mut head = 0;
    while head < pending.len() {
        let vertex = pending[head];
        head += 1;
        let offered = if values[vertex] != 0 {
            values[vertex]
        } else {
            entry[vertex]
        };
        for &target in &edges[offsets[vertex]..offsets[vertex + 1]] {
            let old = entry[target];
            let merged = if old == UNREACHED {
                offered
            } else if old == offered {
                old
            } else {
                UNKNOWN
            };
            if old != merged {
                entry[target] = merged;
                pending.push(target);
            }
        }
    }
    entry
}

fn word(value: i32) -> String {
    if value == UNKNOWN {
        "unknown".to_string()
    } else if value == 0 {
        "sober".to_string()
    } else {
        value.to_string()
    }
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut tokens = input
        .split_whitespace()
        .map(|s| s.parse::<usize>().unwrap());
    let n = tokens.next().unwrap();
    let mut values = Vec::with_capacity(n);
    let mut offsets = Vec::with_capacity(n + 1);
    let mut edges = Vec::with_capacity(MAX_EDGES);
    offsets.push(0);
    for _ in 0..n {
        values.push(tokens.next().unwrap() as i32);
        let degree = tokens.next().unwrap();
        edges.extend(tokens.by_ref().take(degree).map(|target| target - 1));
        offsets.push(edges.len());
    }
    let entry = solve(&values, &offsets, &edges);
    let mut output = String::new();
    for (i, &before) in entry.iter().enumerate() {
        let after = if values[i] != 0 { values[i] } else { before };
        writeln!(output, "{} {}", word(before), word(after)).unwrap();
    }
    print!("{}", output);
}
