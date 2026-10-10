use std::fmt::Write as _;
use std::io::{self, Read};

// identification numbers are positive and below this bound, so 0 means none
const LIMIT: usize = 65536;

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut tok = input
        .split_ascii_whitespace()
        .map(|t| t.parse::<usize>().unwrap());
    let n = tok.next().unwrap();
    let post: Vec<usize> = tok.take(n).collect();
    // read backwards, the odd-session order gives every chairman, then the
    // right wing, then the left wing; a stack of the open chairmen rebuilds the
    // tree from that
    let mut left = vec![0usize; LIMIT];
    let mut right = vec![0usize; LIMIT];
    let mut stack: Vec<usize> = Vec::new();
    for &v in post.iter().rev() {
        match stack.last() {
            Some(&top) if v > top => right[top] = v,
            Some(_) => {
                let mut parent = stack.pop().unwrap();
                while let Some(&top) = stack.last() {
                    if top < v {
                        break;
                    }
                    parent = stack.pop().unwrap();
                }
                left[parent] = v;
            }
            None => {}
        }
        stack.push(v);
    }
    // the even-session order is the plain order root, left, right reversed
    let mut order = Vec::new();
    stack = vec![post[n - 1]];
    while let Some(v) = stack.pop() {
        order.push(v);
        for child in [right[v], left[v]] {
            if child != 0 {
                stack.push(child);
            }
        }
    }
    let mut out = String::new();
    for v in order.iter().rev() {
        writeln!(out, "{}", v).unwrap();
    }
    print!("{}", out);
}
