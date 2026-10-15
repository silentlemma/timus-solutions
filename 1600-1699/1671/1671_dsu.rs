use std::io::{self, Read};

fn find(parent: &mut [usize], v: usize) -> usize {
    let mut root = v;
    while parent[root] != root {
        root = parent[root];
    }
    let mut v = v;
    while parent[v] != root {
        let next = parent[v];
        parent[v] = root;
        v = next;
    }
    root
}

fn main() {
    let mut text = String::new();
    io::stdin().read_to_string(&mut text).unwrap();
    let v: Vec<usize> = text.split_ascii_whitespace().map(|w| w.parse().unwrap()).collect();
    let (n, m) = (v[0], v[1]);
    let ends = &v[2..2 + 2 * m];
    let start = 2 + 2 * m;
    let q = v[start];
    let cuts: Vec<usize> = v[start + 1..start + 1 + q].iter().map(|c| c - 1).collect();
    let mut cut = vec![false; m];
    for &c in &cuts {
        cut[c] = true;
    }
    let mut parent: Vec<usize> = (0..=n).collect();
    let mut pieces = n;
    let mut join = |i: usize, parent: &mut Vec<usize>| {
        let (a, b) = (find(parent, ends[2 * i]), find(parent, ends[2 * i + 1]));
        if a != b {
            parent[a] = b;
            pieces -= 1;
        }
        pieces
    };
    // run backwards: start from the web after all cuts and put the threads
    // back one by one, last cut first
    let mut now = n;
    for i in 0..m {
        if !cut[i] {
            now = join(i, &mut parent);
        }
    }
    let mut answers = vec![0; q];
    for k in (0..q).rev() {
        answers[k] = now;
        now = join(cuts[k], &mut parent);
    }
    let words: Vec<String> = answers.iter().map(|a| a.to_string()).collect();
    println!("{}", words.join(" "));
}
