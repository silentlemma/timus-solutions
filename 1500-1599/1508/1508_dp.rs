use std::io::{self, Read};

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut it = input.split_ascii_whitespace();
    let n: usize = it.next().unwrap().parse().unwrap();
    let k: usize = it.next().unwrap().parse().unwrap();
    let groups: Vec<usize> = (0..k)
        .map(|_| it.next().unwrap().parse().unwrap())
        .collect();
    let line = it.next().unwrap().as_bytes();
    // dots[i]: known empty cells among the first i
    let mut dots = vec![0; n + 1];
    for i in 0..n {
        dots[i + 1] = dots[i] + (line[i] == b'.') as usize;
    }
    // whether a group can cover the cells s ... s + length - 1
    let fits = |s: usize, length: usize| s + length <= n && dots[s + length] == dots[s];
    // pre[i][j]: the first i cells can hold the first j groups
    let mut pre = vec![vec![false; k + 1]; n + 1];
    pre[0][0] = true;
    for i in 1..=n {
        for j in 0..=k {
            let mut ok = line[i - 1] != b'X' && pre[i - 1][j];
            if !ok && j > 0 && i >= groups[j - 1] && fits(i - groups[j - 1], groups[j - 1]) {
                let s = i - groups[j - 1];
                ok = if s == 0 {
                    j == 1
                } else {
                    line[s - 1] != b'X' && pre[s - 1][j - 1]
                };
            }
            pre[i][j] = ok;
        }
    }
    if !pre[n][k] {
        println!("Impossible");
        return;
    }
    // suf[i][j]: the cells from i on can hold the groups from j on
    let mut suf = vec![vec![false; k + 1]; n + 2];
    suf[n][k] = true;
    for i in (0..n).rev() {
        for j in (0..=k).rev() {
            let mut ok = line[i] != b'X' && suf[i + 1][j];
            if !ok && j < k && fits(i, groups[j]) {
                let end = i + groups[j];
                ok = if end == n {
                    j + 1 == k
                } else {
                    line[end] != b'X' && suf[end + 1][j + 1]
                };
            }
            suf[i][j] = ok;
        }
    }
    // difference array of the cells some group can cover
    let mut cover = vec![0i32; n + 1];
    for (j, &length) in groups.iter().enumerate() {
        for s in 0..(n + 1).saturating_sub(length) {
            if !fits(s, length) {
                continue;
            }
            let end = s + length;
            let left = if s == 0 {
                j == 0
            } else {
                line[s - 1] != b'X' && pre[s - 1][j]
            };
            let right = if end == n {
                j + 1 == k
            } else {
                line[end] != b'X' && suf[end + 1][j + 1]
            };
            if left && right {
                cover[s] += 1;
                cover[end] -= 1;
            }
        }
    }
    let mut run = 0;
    let out: String = (0..n)
        .map(|c| {
            run += cover[c];
            let white = line[c] != b'X' && (0..=k).any(|j| pre[c][j] && suf[c + 1][j]);
            match (white, run > 0) {
                (true, true) => '?',
                (true, false) => '.',
                _ => 'X',
            }
        })
        .collect();
    println!("{}", out);
}
