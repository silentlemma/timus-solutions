use std::fmt::Write as _;
use std::io::{self, Read, Write};

const NEED: i32 = 2; // a run needs two generating intervals inside it to be split

// g[l][r]: columns l .. r-1 must be a union of chosen intervals inside them.
// Going right, an interval that two smaller chosen ones already cover is
// dropped, and those it leaned on move right: the smallest such family.
fn smallest_family(g: &mut [Vec<bool>], width: usize) {
    for right in 1..=width {
        loop {
            let mut count = vec![0i32; width + 1];
            let (mut covered, mut rest) = (0i32, 0i32); // inside [t, u), and starting before t
            let (mut u, mut t) = (right, right - 1);
            let mut redundant = true;
            while u > t {
                covered -= count[u];
                for left in 0..u {
                    if !g[left][u] {
                        continue;
                    }
                    count[left] += 1;
                    if left >= t {
                        covered += 1;
                    } else {
                        rest += 1;
                    }
                }
                if covered + rest < NEED {
                    redundant = false;
                    break;
                }
                while covered < NEED {
                    t -= 1;
                    covered += count[t];
                    rest -= count[t];
                }
                u -= 1;
            }
            if !redundant {
                break;
            }
            let mut w = u;
            while !g[w][right] {
                w += 1;
            }
            g[w][right] = false;
            let mut end = right - 1;
            while w > u {
                let mut x = u;
                while x < w && !g[x][end] {
                    x += 1;
                }
                if x < w {
                    g[x][end] = false;
                    g[w][end] = true;
                    w = x;
                }
                end -= 1;
            }
        }
    }
}

fn main() {
    let mut text = String::new();
    io::stdin().read_to_string(&mut text).unwrap();
    let mut words = text.split_ascii_whitespace();
    let n: usize = words.next().unwrap().parse().unwrap();
    let m: usize = words.next().unwrap().parse().unwrap();
    // the black pixels of a column form one run from top to bottom
    let (mut top, mut bottom) = (vec![n; m], vec![0usize; m]);
    let mut g = vec![vec![false; m + 1]; m + 1];
    for row in 0..n {
        let line = words.next().unwrap().as_bytes();
        let mut col = 0;
        while col < m {
            if line[col] == b'0' {
                col += 1;
                continue;
            }
            let left = col;
            while col < m && line[col] == b'1' {
                top[col] = top[col].min(row);
                bottom[col] = bottom[col].max(row);
                col += 1;
            }
            g[left][col] = true;
        }
    }
    smallest_family(&mut g, m);
    // a chosen interval of columns spans every row where all of them are black
    let mut out = String::new();
    let mut count = 0;
    for lo in 0..m {
        for hi in lo + 1..=m {
            if !g[lo][hi] {
                continue;
            }
            let first = top[lo..hi].iter().max().unwrap();
            let last = bottom[lo..hi].iter().min().unwrap();
            writeln!(out, "{} {} {} {}", first + 1, lo + 1, last + 1, hi).unwrap();
            count += 1;
        }
    }
    let mut stdout = io::stdout().lock();
    writeln!(stdout, "{}", count).unwrap();
    stdout.write_all(out.as_bytes()).unwrap();
}
