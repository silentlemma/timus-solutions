use std::io::{self, Read};

const ALPHABET: usize = 26;
const NONE: u32 = u32::MAX;

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut it = input.split_ascii_whitespace();
    it.next();
    let a = it.next().unwrap().as_bytes();
    let b = it.next().unwrap().as_bytes();
    // suffix automaton of a: every state is a class of substrings with the
    // same end positions; len is the longest of them, link the suffix link
    let mut next = vec![[NONE; ALPHABET]];
    let mut link = vec![NONE];
    let mut len = vec![0u32];
    let mut last = 0usize;
    for &ch in a {
        let c = (ch - b'A') as usize;
        let cur = next.len();
        next.push([NONE; ALPHABET]);
        link.push(0);
        len.push(len[last] + 1);
        let mut p = last as u32;
        while p != NONE && next[p as usize][c] == NONE {
            next[p as usize][c] = cur as u32;
            p = link[p as usize];
        }
        if p != NONE {
            let q = next[p as usize][c] as usize;
            if len[p as usize] + 1 == len[q] {
                link[cur] = q as u32;
            } else {
                let clone = next.len();
                next.push(next[q]);
                link.push(link[q]);
                len.push(len[p as usize] + 1);
                while p != NONE && next[p as usize][c] == q as u32 {
                    next[p as usize][c] = clone as u32;
                    p = link[p as usize];
                }
                link[q] = clone as u32;
                link[cur] = clone as u32;
            }
        }
        last = cur;
    }
    // walk b through the automaton, keeping the longest suffix of the read
    // part of b that occurs in a
    let (mut state, mut run, mut best, mut end) = (0usize, 0u32, 0u32, 0usize);
    for (i, &ch) in b.iter().enumerate() {
        let c = (ch - b'A') as usize;
        while state != 0 && next[state][c] == NONE {
            state = link[state] as usize;
            run = len[state];
        }
        if next[state][c] != NONE {
            state = next[state][c] as usize;
            run += 1;
        }
        if run > best {
            best = run;
            end = i + 1;
        }
    }
    println!("{}", String::from_utf8_lossy(&b[end - best as usize..end]));
}
