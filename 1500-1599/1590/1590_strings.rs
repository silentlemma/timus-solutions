use std::io::{self, Read};

const LETTERS: usize = 26;
const NONE: usize = usize::MAX;

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let s = match input.split_ascii_whitespace().next() {
        Some(w) => w.as_bytes(),
        None => return,
    };
    let most = 2 * s.len() + 1;
    // suffix automaton: every state is a class of substrings with the same
    // end positions, from link-length + 1 up to length characters long
    let mut length = vec![0usize; most];
    let mut link = vec![NONE; most];
    let mut next = vec![[NONE; LETTERS]; most];
    let (mut size, mut last) = (1, 0);
    for &ch in s {
        let c = (ch - b'a') as usize;
        let cur = size;
        size += 1;
        length[cur] = length[last] + 1;
        let mut p = last;
        while p != NONE && next[p][c] == NONE {
            next[p][c] = cur;
            p = link[p];
        }
        if p == NONE {
            link[cur] = 0;
        } else {
            let q = next[p][c];
            if length[p] + 1 == length[q] {
                link[cur] = q;
            } else {
                // split q: the clone keeps the shorter strings
                let clone = size;
                size += 1;
                length[clone] = length[p] + 1;
                link[clone] = link[q];
                next[clone] = next[q];
                while p != NONE && next[p][c] == q {
                    next[p][c] = clone;
                    p = link[p];
                }
                link[q] = clone;
                link[cur] = clone;
            }
        }
        last = cur;
    }
    let total: usize = (1..size).map(|v| length[v] - length[link[v]]).sum();
    println!("{}", total);
}
