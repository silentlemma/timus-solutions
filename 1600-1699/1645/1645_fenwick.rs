use std::fmt::Write as _;
use std::io::{self, Read};

fn main() {
    let mut text = String::new();
    io::stdin().read_to_string(&mut text).unwrap();
    let nums: Vec<usize> = text.split_ascii_whitespace().map(|w| w.parse().unwrap()).collect();
    let n = nums[0];
    let mut place = vec![0; n + 1]; // place[s]: finishing position of skier s
    for p in 1..=n {
        place[nums[p]] = p;
    }
    let mut tree = vec![0usize; n + 1]; // finishing positions of skiers who started before
    let mut out = String::new();
    for skier in 1..=n {
        let p = place[skier];
        let mut earlier = 0; // started and finished before: undecided
        let mut i = p - 1;
        while i > 0 {
            earlier += tree[i];
            i &= i - 1;
        }
        // started later yet finished before: surely faster
        let faster = p - 1 - earlier;
        // started before yet finished later: surely slower, the rest undecided
        writeln!(out, "{} {}", faster + 1, (n - skier) + earlier + 1).unwrap();
        let mut i = p;
        while i <= n {
            tree[i] += 1;
            i += i & i.wrapping_neg();
        }
    }
    print!("{}", out);
}
