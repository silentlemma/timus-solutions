use std::io::{self, Read, Write};

fn z_function(s: &[u8]) -> Vec<usize> {
    let n = s.len();
    let mut z = vec![0; n];
    let (mut left, mut right) = (0, 0);
    for i in 1..n {
        let mut k = if i < right { z[i - left].min(right - i) } else { 0 };
        while i + k < n && s[k] == s[i + k] {
            k += 1;
        }
        z[i] = k;
        if i + k > right {
            left = i;
            right = i + k;
        }
    }
    z
}

fn main() {
    let mut text = String::new();
    io::stdin().read_to_string(&mut text).unwrap();
    let mut words = text.split_ascii_whitespace();
    let word = words.next().unwrap();
    let last = words.next().unwrap();
    let (m, n) = (word.len(), last.len());
    let z = z_function(format!("{}#{}", word, last).as_bytes());
    // from a cut at position p the next piece can end anywhere in
    // p + 1 .. p + z[p]; so the reachable cuts are always 0 .. reach
    let mut parent = vec![0; n + 1];
    let mut reach = 0;
    let mut p = 0;
    while p <= reach && p < n {
        let far = p + z[m + 1 + p];
        for q in reach + 1..=far {
            parent[q] = p;
        }
        reach = reach.max(far);
        p += 1;
    }
    if reach < n {
        println!("Yes");
        return;
    }
    let mut pieces = Vec::new();
    let mut q = n;
    while q > 0 {
        pieces.push(&last[parent[q]..q]);
        q = parent[q];
    }
    pieces.reverse();
    let out = format!("No\n{}\n", pieces.join(" "));
    io::stdout().write_all(out.as_bytes()).unwrap();
}
