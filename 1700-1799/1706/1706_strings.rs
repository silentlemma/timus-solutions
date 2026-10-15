use std::io::{self, Read};

const COPIES: usize = 4; // the text repeated so that every comparison below stays inside it

fn main() {
    let mut text = String::new();
    io::stdin().read_to_string(&mut text).unwrap();
    let mut words = text.split_ascii_whitespace();
    let k: usize = words.next().unwrap().parse().unwrap();
    let s = words.next().unwrap().as_bytes();
    let n = s.len();
    let t = s.repeat(COPIES);
    // a substring is counted at its leftmost start j in the window [a, a + k):
    // its lengths up to a + k - j minus the longest common prefix of j with an
    // earlier start of the window, best[j]; going down over a adds start a
    let top = n + 2 * k;
    let mut common = vec![0usize; k]; // common[d] = lcp of positions a and a + d
    let mut best = vec![0usize; top + k];
    let mut answers = vec![0u64; n];
    for a in (0..=top).rev() {
        let ca = t[a];
        for d in 1..k {
            let j = a + d;
            if t[j] == ca {
                common[d] += 1;
                if common[d] > best[j] {
                    best[j] = common[d];
                }
            } else {
                common[d] = 0;
            }
        }
        if a < n {
            let end = a + k;
            answers[a] = (a..end)
                .map(|j| (end - j).saturating_sub(best[j]) as u64)
                .sum();
        }
    }
    let line: Vec<String> = answers.iter().map(|v| v.to_string()).collect();
    println!("{}", line.join(" "));
}
