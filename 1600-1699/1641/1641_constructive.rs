use std::collections::HashSet;
use std::fmt::Write as _;
use std::io::{self, Read};

fn main() {
    let mut text = String::new();
    io::stdin().read_to_string(&mut text).unwrap();
    let mut nums = text.split_ascii_whitespace().map(|w| w.parse::<usize>().unwrap());
    let mut next = || nums.next().unwrap();
    let (n, k, m) = (next(), next(), next());
    // rooms in turn: every room gets someone, and the split is as even as
    // possible, which leaves the most pairs from different rooms
    let room: Vec<usize> = (0..n).map(|i| i % k).collect();
    // neighbours in this order always have different rooms
    let mut days: Vec<(usize, usize)> = (0..n / 2).map(|p| (2 * p, 2 * p + 1)).collect();
    if n % 2 == 1 {
        days.push((if room[n - 1] == room[0] { 1 } else { 0 }, n - 1));
    }
    let mut used: HashSet<(usize, usize)> = days.iter().cloned().collect();
    'fill: for i in 0..n {
        for j in i + 1..n {
            if days.len() == m {
                break 'fill;
            }
            if room[i] != room[j] && used.insert((i, j)) {
                days.push((i, j));
            }
        }
    }
    let mut out = String::new();
    for r in &room {
        writeln!(out, "{}", r + 1).unwrap();
    }
    for &(a, b) in &days[..m] {
        writeln!(out, "{} {}", a + 1, b + 1).unwrap();
    }
    print!("{}", out);
}
