use std::io::{self, Read};

fn prefix_function(t: &[u8]) -> Vec<usize> {
    let mut p = vec![0; t.len()];
    let mut k = 0;
    for i in 1..t.len() {
        while k > 0 && t[i] != t[k] {
            k = p[k - 1];
        }
        if t[i] == t[k] {
            k += 1;
        }
        p[i] = k;
    }
    p
}

// the first occurrence of t in s[from..to], if any
fn find(s: &[u8], from: usize, to: usize, t: &[u8], p: &[usize]) -> Option<usize> {
    let mut k = 0;
    for i in from..to {
        while k > 0 && s[i] != t[k] {
            k = p[k - 1];
        }
        if s[i] == t[k] {
            k += 1;
            if k == t.len() {
                return Some(i + 1 - k);
            }
        }
    }
    None
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut lines = input.lines();
    let source = lines.next().unwrap().trim_end_matches('\r').as_bytes();
    let target: Vec<&[u8]> = lines
        .next()
        .unwrap()
        .trim_end_matches('\r')
        .split(' ')
        .map(|w| w.as_bytes())
        .collect();
    let mut keep = vec![false; source.len()];
    let mut j = 0;
    let mut p = prefix_function(target[0]);
    // each wanted word goes to its earliest place in the current word, at
    // least one erased letter after the previous one there; if it does not
    // fit, the next word of the source is tried
    let mut begin = 0;
    while begin < source.len() && j < target.len() {
        let end = source[begin..]
            .iter()
            .position(|&c| c == b' ')
            .map_or(source.len(), |e| e + begin);
        let mut pos = begin;
        while j < target.len() && pos <= end && end - pos >= target[j].len() {
            match find(source, pos, end, target[j], &p) {
                None => break,
                Some(at) => {
                    keep[at..at + target[j].len()].iter_mut().for_each(|k| *k = true);
                    pos = at + target[j].len() + 1;
                    j += 1;
                    if j < target.len() {
                        p = prefix_function(target[j]);
                    }
                }
            }
        }
        begin = end + 1;
    }
    if j < target.len() {
        println!("I HAVE FAILED!!!");
        return;
    }
    let out: String = source
        .iter()
        .zip(&keep)
        .map(|(&c, &k)| if c != b' ' && !k { '_' } else { c as char })
        .collect();
    println!("{}", out);
}
