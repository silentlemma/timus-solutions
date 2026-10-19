use std::io::{self, Read};

const BASE: usize = 10;
const UNSEEN: usize = usize::MAX;

struct Machine {
    terminal: Vec<usize>,
    rows: Vec<[usize; BASE]>,
}

fn construct(old: &[[usize; BASE]], flags: &[usize], offset: usize) -> Machine {
    let n = old.len();
    let stride = n + 1;
    let mut identifiers = vec![UNSEEN; 2 * n * stride];
    let mut keys = vec![2 * n];
    identifiers[keys[0]] = 0;
    let mut result = Machine {
        terminal: Vec::new(),
        rows: Vec::new(),
    };
    let mut head = 0;
    while head < keys.len() {
        let key = keys[head];
        let pair = key / 2;
        let (normal, previous) = (pair / stride, pair % stride);
        result.terminal.push(key & 1);
        let mut row = [0; BASE];
        for digit in 0..BASE {
            let next_normal = old[normal][digit];
            let next_previous = if digit > 0 {
                old[normal][digit - 1]
            } else if previous == n {
                n
            } else {
                old[previous][BASE - 1]
            };
            let accepted = if digit >= offset {
                flags[old[normal][digit - offset]]
            } else if previous != n {
                flags[old[previous][digit + BASE - offset]]
            } else {
                0
            };
            let target = 2 * (next_normal * stride + next_previous) + accepted;
            if identifiers[target] == UNSEEN {
                identifiers[target] = keys.len();
                keys.push(target);
            }
            row[digit] = identifiers[target];
        }
        result.rows.push(row);
        head += 1;
    }
    result
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut tokens = input.split_whitespace();
    let offset: usize = tokens.next().unwrap().parse().unwrap();
    let n: usize = tokens.next().unwrap().parse().unwrap();
    let flags: Vec<usize> = (0..n)
        .map(|_| tokens.next().unwrap().parse().unwrap())
        .collect();
    let mut old = vec![[0; BASE]; n];
    for row in &mut old {
        for target in row {
            *target = tokens.next().unwrap().parse::<usize>().unwrap() - 1;
        }
    }
    let result = construct(&old, &flags, offset);
    let mut out = format!("Success\n{}\n", result.rows.len());
    for (i, value) in result.terminal.iter().enumerate() {
        if i > 0 {
            out.push(' ');
        }
        out.push_str(&value.to_string());
    }
    out.push('\n');
    for row in result.rows {
        for (d, target) in row.iter().enumerate() {
            if d > 0 {
                out.push(' ');
            }
            out.push_str(&(target + 1).to_string());
        }
        out.push('\n');
    }
    print!("{}", out);
}
