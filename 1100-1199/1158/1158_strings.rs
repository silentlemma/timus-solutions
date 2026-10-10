use std::collections::VecDeque;
use std::io::{self, Read};

// counts reach 50^50, so they are kept in limbs of nine decimal digits
const LIMB: u64 = 1_000_000_000;
const BYTES: usize = 256;

// lowest limb first
type Big = Vec<u64>;

fn add(a: &mut Big, b: &Big) {
    if a.len() < b.len() {
        a.resize(b.len(), 0);
    }
    let mut carry = 0;
    for i in 0..a.len() {
        let v = a[i] + b.get(i).copied().unwrap_or(0) + carry;
        a[i] = v % LIMB;
        carry = v / LIMB;
    }
    if carry > 0 {
        a.push(carry);
    }
}

fn text(a: &Big) -> String {
    match a.split_last() {
        None => "0".to_string(),
        Some((top, rest)) => {
            let mut out = top.to_string();
            for limb in rest.iter().rev() {
                out += &format!("{:09}", limb);
            }
            out
        }
    }
}

fn main() {
    // letters may be any bytes above 32, so the input is read as bytes
    let mut data = Vec::new();
    io::stdin().read_to_end(&mut data).unwrap();
    let lines: Vec<&[u8]> = data
        .split(|&b| b == b'\n')
        .map(|line| {
            let start = line.iter().position(|&b| b > b' ').unwrap_or(line.len());
            let end = line
                .iter()
                .rposition(|&b| b > b' ')
                .map_or(start, |e| e + 1);
            &line[start..end]
        })
        .collect();
    let head: Vec<usize> = String::from_utf8_lossy(lines[0])
        .split_ascii_whitespace()
        .map(|t| t.parse().unwrap())
        .collect();
    let (n, m, p) = (head[0], head[1], head[2]);
    let letters = lines[1];
    let mut index = [0usize; BYTES];
    for (k, &c) in letters.iter().take(n).enumerate() {
        index[c as usize] = k;
    }
    let words: Vec<&[u8]> = lines[2..]
        .iter()
        .filter(|w| !w.is_empty())
        .take(p)
        .copied()
        .collect();
    // Aho-Corasick automaton over the forbidden words; a state is bad when
    // some word ends there
    let mut go: Vec<Vec<Option<usize>>> = vec![vec![None; n]];
    let mut bad = vec![false];
    for w in &words {
        let mut s = 0;
        for &c in *w {
            let c = index[c as usize];
            if go[s][c].is_none() {
                go[s][c] = Some(go.len());
                go.push(vec![None; n]);
                bad.push(false);
            }
            s = go[s][c].unwrap();
        }
        bad[s] = true;
    }
    let mut next_of = vec![vec![0usize; n]; go.len()];
    let mut fail = vec![0usize; go.len()];
    let mut queue = VecDeque::new();
    for c in 0..n {
        match go[0][c] {
            Some(t) => {
                next_of[0][c] = t;
                queue.push_back(t);
            }
            None => next_of[0][c] = 0,
        }
    }
    while let Some(s) = queue.pop_front() {
        bad[s] = bad[s] || bad[fail[s]];
        for c in 0..n {
            match go[s][c] {
                Some(t) => {
                    fail[t] = next_of[fail[s]][c];
                    next_of[s][c] = t;
                    queue.push_back(t);
                }
                None => next_of[s][c] = next_of[fail[s]][c],
            }
        }
    }
    // count the sentences letter by letter, never stepping into a bad state
    let mut ways: Vec<Big> = vec![Vec::new(); go.len()];
    ways[0] = vec![1];
    for _ in 0..m {
        let mut next: Vec<Big> = vec![Vec::new(); go.len()];
        for (s, w) in ways.iter().enumerate() {
            if !w.is_empty() {
                for &t in &next_of[s] {
                    if !bad[t] {
                        add(&mut next[t], w);
                    }
                }
            }
        }
        ways = next;
    }
    let mut total = Vec::new();
    for w in &ways {
        add(&mut total, w);
    }
    println!("{}", text(&total));
}
