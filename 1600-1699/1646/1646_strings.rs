use std::io::{self, Read};

const MOD: u64 = 1_000_000_007;

/// a sample: its count mod MOD and its first and last letters; the full
/// string can be 2^100 long
struct Sample {
    count: u64,
    head: String,
    tail: String,
}

fn main() {
    let mut text = String::new();
    io::stdin().read_to_string(&mut text).unwrap();
    let mut words = text.split_ascii_whitespace();
    let pattern = words.next().unwrap();
    let edge = pattern.len() - 1; // letters kept at each end of a sample
    let occurrences = |t: &str| (0..=t.len().saturating_sub(pattern.len()))
        .filter(|&i| t.len() >= pattern.len() && t[i..].starts_with(pattern))
        .count() as u64;
    let head = |s: &str| s[..s.len().min(edge)].to_string();
    let tail = |s: &str| s[s.len() - s.len().min(edge)..].to_string();
    let mut samples: Vec<Sample> = Vec::new();
    for _ in 0..2 {
        let s = words.next().unwrap();
        samples.push(Sample { count: occurrences(s), head: head(s), tail: tail(s) });
    }
    let m: usize = words.next().unwrap().parse().unwrap();
    for _ in 0..m {
        let i: usize = words.next().unwrap().parse().unwrap();
        let j: usize = words.next().unwrap().parse().unwrap();
        let (a, b) = (&samples[i - 1], &samples[j - 1]);
        // every new occurrence crosses the seam, so it lies in these letters
        let seam = occurrences(&(a.tail.clone() + &b.head));
        let next = Sample {
            count: (a.count + b.count + seam) % MOD,
            head: head(&(a.head.clone() + &b.head)),
            tail: tail(&(a.tail.clone() + &b.tail)),
        };
        samples.push(next);
    }
    println!("{}", samples.last().unwrap().count);
}
