use std::cmp::Reverse;
use std::collections::BinaryHeap;
use std::fmt::Write as _;
use std::io::{self, Read, Write};

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let code: Vec<usize> = input
        .split_ascii_whitespace()
        .map(|t| parse_integer(t))
        .collect();
    let n = code.len() + 1;
    // a vertex stays until all its neighbours but one are removed, and each
    // removed neighbour writes the vertex once
    let mut deg = vec![1usize; n + 1];
    for &c in &code {
        deg[c] += 1;
    }
    let mut leaves: BinaryHeap<Reverse<usize>> =
        (1..=n).filter(|&u| deg[u] == 1).map(Reverse).collect();
    let mut adj = vec![Vec::new(); n + 1];
    for &c in &code {
        let Reverse(leaf) = leaves.pop().unwrap();
        adj[leaf].push(c);
        adj[c].push(leaf);
        deg[c] -= 1;
        if deg[c] == 1 {
            leaves.push(Reverse(c));
        }
    }
    let mut out = String::new();
    for u in 1..=n {
        adj[u].sort_unstable();
        write!(out, "{}:", u).unwrap();
        for &x in &adj[u] {
            write!(out, " {}", x).unwrap();
        }
        out.push('\n');
    }
    io::stdout().write_all(out.as_bytes()).unwrap();
}

// Input bounds guarantee that each decimal token fits its destination integer.
// Accumulate negative values directly so the minimum signed integer also fits.
fn parse_integer<T>(word: &str) -> T
where
    T: From<u8> + std::ops::Add<Output = T> + std::ops::Sub<Output = T> + std::ops::Mul<Output = T>,
{
    let digits = word.as_bytes();
    let negative = digits[0] == b'-';
    let start = usize::from(negative || digits[0] == b'+');
    let mut value = T::from(0);
    for &byte in &digits[start..] {
        let digit = T::from(byte - b'0');
        let scaled = value * T::from(10);
        value = if negative {
            scaled - digit
        } else {
            scaled + digit
        };
    }
    value
}
