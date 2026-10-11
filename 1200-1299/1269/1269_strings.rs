use std::io::{self, Read};

fn main() {
    let mut input = Vec::new();
    io::stdin().read_to_end(&mut input).unwrap();
    // lines without their carriage returns
    let mut lines = input
        .split(|&c| c == b'\n')
        .map(|l| l.strip_suffix(b"\r").unwrap_or(l));
    let mut number = || -> usize {
        let line = lines.next().unwrap();
        String::from_utf8_lossy(line).trim().parse().unwrap()
    };
    let n = number();
    drop(number);
    let words: Vec<&[u8]> = (0..n).map(|_| lines.next().unwrap()).collect();
    let total = 1 + words.iter().map(|w| w.len()).sum::<usize>();
    // build the trie as first-child / next-sibling lists
    let (mut child, mut sibling) = (vec![-1i32; total], vec![-1i32; total]);
    let (mut ends, mut chars) = (vec![0i32; total], vec![0u8; total]);
    let mut nodes = 1usize;
    for w in &words {
        let mut v = 0usize;
        for &c in w.iter() {
            let mut u = child[v];
            while u >= 0 && chars[u as usize] != c {
                u = sibling[u as usize];
            }
            if u < 0 {
                u = nodes as i32;
                nodes += 1;
                chars[u as usize] = c;
                sibling[u as usize] = child[v];
                child[v] = u;
            }
            v = u as usize;
        }
        ends[v] = ends[v].max(w.len() as i32);
    }
    // renumber in breadth-first order: the children of v then take the
    // numbers first[v] .. first[v] + count[v] - 1, and label[u] is the
    // byte leading to u
    let (mut first, mut count) = (vec![0usize; nodes], vec![0usize; nodes]);
    let (mut longest, mut label) = (vec![0i32; nodes], vec![0u8; nodes]);
    let mut old = vec![0usize];
    for v in 0..nodes {
        first[v] = old.len();
        let mut u = child[old[v]];
        while u >= 0 {
            label[old.len()] = chars[u as usize];
            longest[old.len()] = ends[u as usize];
            old.push(u as usize);
            u = sibling[u as usize];
        }
        count[v] = old.len() - first[v];
    }
    // the child of v along byte c
    let walk = |v: usize, c: u8, label: &[u8]| {
        label[first[v]..first[v] + count[v]]
            .iter()
            .position(|&x| x == c)
            .map(|i| first[v] + i)
    };
    // failure links in the same order; a node also takes the longest word
    // of its failure node, which comes earlier
    let mut fail = vec![0usize; nodes];
    for v in 1..nodes {
        for u in first[v]..first[v] + count[v] {
            let mut f = fail[v];
            let g = loop {
                match walk(f, label[u], &label) {
                    Some(g) => break g,
                    None if f == 0 => break 0,
                    None => f = fail[f],
                }
            };
            fail[u] = g;
            longest[u] = longest[u].max(longest[g]);
        }
    }
    let m: usize = String::from_utf8_lossy(lines.next().unwrap())
        .trim()
        .parse()
        .unwrap();
    for (row, line) in lines.take(m).enumerate() {
        let (mut v, mut best) = (0usize, line.len() as i32 + 1);
        for (i, &c) in line.iter().enumerate() {
            v = loop {
                match walk(v, c, &label) {
                    Some(g) => break g,
                    None if v == 0 => break 0,
                    None => v = fail[v],
                }
            };
            if longest[v] > 0 {
                best = best.min(i as i32 + 2 - longest[v]);
            }
        }
        if best <= line.len() as i32 {
            println!("{} {}", row + 1, best);
            return;
        }
    }
    println!("Passed");
}
