use std::io::{self, Read};

// cut > 0: split before s[cut]; < 0: -cut is the period
fn fold(s: &[u8], cut: &[Vec<i32>], i: usize, j: usize, out: &mut String) {
    let c = cut[i][j];
    if c > 0 {
        fold(s, cut, i, c as usize - 1, out);
        fold(s, cut, c as usize, j, out);
    } else if c < 0 {
        let p = (-c) as usize;
        out.push_str(&((j - i + 1) / p).to_string());
        out.push('(');
        fold(s, cut, i, i + p - 1, out);
        out.push(')');
    } else {
        out.push_str(std::str::from_utf8(&s[i..=j]).unwrap());
    }
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let s = input.trim().as_bytes();
    let n = s.len();
    let mut best = vec![vec![0usize; n]; n];
    let mut cut = vec![vec![0i32; n]; n];
    for size in 1..=n {
        for i in 0..=n - size {
            let j = i + size - 1;
            best[i][j] = size;
            for k in i + 1..=j {
                if best[i][k - 1] + best[k][j] < best[i][j] {
                    best[i][j] = best[i][k - 1] + best[k][j];
                    cut[i][j] = k as i32;
                }
            }
            // a period p repeats when the segment equals itself shifted by p
            for p in 1..size {
                if size % p != 0 || s[i..=j - p] != s[i + p..=j] {
                    continue;
                }
                let l = (size / p).to_string().len() + 2 + best[i][i + p - 1];
                if l < best[i][j] {
                    best[i][j] = l;
                    cut[i][j] = -(p as i32);
                }
            }
        }
    }
    let mut out = String::new();
    fold(s, &cut, 0, n - 1, &mut out);
    println!("{}", out);
}
