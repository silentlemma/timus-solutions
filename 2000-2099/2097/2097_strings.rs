use std::io::{self, Read};

const WINDOW: usize = 3; // a second difference uses three heights

fn second_differences(h: &[i64]) -> Vec<i64> {
    h.windows(WINDOW).map(|w| w[2] - 2 * w[1] + w[0]).collect()
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut it = input.split_ascii_whitespace().map(|t| t.parse::<i64>().unwrap());
    let n = it.next().unwrap() as usize;
    let m = it.next().unwrap() as usize;
    let x: Vec<i64> = it.by_ref().take(m + 1).collect();
    // a section is similar exactly when the second differences agree, and then
    // a is the difference of the first steps of the two sections
    let pattern = second_differences(&x);
    let len = pattern.len();
    let mut pi = vec![0usize; len];
    for i in 1..len {
        let mut k = pi[i - 1];
        while k > 0 && pattern[i] != pattern[k] {
            k = pi[k - 1];
        }
        if pattern[i] == pattern[k] {
            k += 1;
        }
        pi[i] = k;
    }
    let mut best: Option<(i64, usize, usize)> = None; // |a|, slope, start
    for slope in 1..=n {
        let length = it.next().unwrap() as usize;
        let y: Vec<i64> = it.by_ref().take(length + 1).collect();
        if length < m {
            continue;
        }
        let text = second_differences(&y);
        let mut k = 0;
        for i in 0..=text.len() {
            if k == len {
                let start = i - len;
                let a = ((x[1] - x[0]) - (y[start + 1] - y[start])).abs();
                if best.map_or(true, |b| a < b.0) {
                    best = Some((a, slope, start));
                }
                if len > 0 {
                    k = pi[k - 1];
                }
            }
            if i == text.len() || len == 0 {
                continue;
            }
            while k > 0 && text[i] != pattern[k] {
                k = pi[k - 1];
            }
            if text[i] == pattern[k] {
                k += 1;
            }
        }
    }
    match best {
        Some((_, slope, start)) => println!("{} {}", slope, start),
        None => println!("-1"),
    }
}
