use std::io::{self, Read};

#[derive(Clone, Copy, PartialEq)]
enum State {
    New,
    Path,
    Good,
}

fn consistent(names: &[usize]) -> bool {
    if names.iter().filter(|&&k| k == 0).count() != 1 {
        return false;
    }
    let mut state = vec![State::New; names.len() + 1];
    let mut path = Vec::new();
    for start in 1..=names.len() {
        // follow the accusations until a confessor or a child already known
        // to lead to one; meeting the current path again means a ring
        path.clear();
        let mut v = start;
        while v != 0 && state[v] == State::New {
            state[v] = State::Path;
            path.push(v);
            v = names[v - 1];
        }
        if v != 0 && state[v] == State::Path {
            return false;
        }
        for &u in &path {
            state[u] = State::Good;
        }
    }
    true
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut it = input
        .split_ascii_whitespace()
        .map(|t| t.parse::<usize>().unwrap());
    let t = it.next().unwrap();
    let mut out = String::new();
    for _ in 0..t {
        let n = it.next().unwrap();
        let names: Vec<usize> = (0..n).map(|_| it.next().unwrap()).collect();
        out += if consistent(&names) { "YES\n" } else { "NO\n" };
    }
    print!("{}", out);
}
